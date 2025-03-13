import xml.etree.ElementTree as ET
import re

def is_company_affiliated(affiliation):
    """Check if the affiliation is a company rather than an academic institution."""
    company_keywords = ["Inc", "Ltd", "LLC", "Corporation", "Company", "GmbH", "Pvt", "S.A.", "Co."]
    return any(keyword in affiliation for keyword in company_keywords)

def extract_paper_info(xml_data):
    """Extract required fields from PubMed EFetch XML response."""
    extracted_data = []

    try:
        # Parse XML safely
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        print("Error: Invalid XML format")
        return []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID", default="N/A")
        title = article.findtext(".//ArticleTitle", default="N/A")
        pub_date = article.findtext(".//PubDate/Year", default="N/A")

        non_academic_authors = []
        company_affiliations = []
        corresponding_emails = []

        # Find all authors
        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName", default="N/A")
            first_name = author.findtext("ForeName", default="")
            full_name = f"{first_name} {last_name}".strip()

            # 🔥 Fix: Extract AffiliationInfo correctly
            for aff in author.findall("AffiliationInfo/Affiliation"):
                affiliation_text = aff.text.strip() if aff is not None else ""
                
                # Debug: Print affiliation to check
                print(f"Author: {full_name}, Affiliation: {affiliation_text}")

                if is_company_affiliated(affiliation_text):
                    non_academic_authors.append(full_name)
                    company_affiliations.append(affiliation_text)

                # 🔥 Fix: Extract multiple emails if available
                email_matches = re.findall(r'[\w\.-]+@[\w\.-]+', affiliation_text)
                corresponding_emails.extend(email_matches)

        extracted_data.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(set(non_academic_authors)) or "N/A",
            "Company Affiliation(s)": "; ".join(set(company_affiliations)) or "N/A",
            "Corresponding Author Email": "; ".join(set(corresponding_emails)) or "N/A"
        })

    return extracted_data
