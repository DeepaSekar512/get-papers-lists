import requests
from src.config import API_KEY, BASE_URL

def search_pubmed(query: str, max_results: int = 20):
    """Search PubMed for papers using a query and return PubMed IDs."""
    search_url = f"{BASE_URL}/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
        "api_key": API_KEY
    }
    
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["esearchresult"]["idlist"]
    else:
        print("Error fetching data:", response.status_code)
        return []

def fetch_paper_details(pubmed_ids: list):
    """Fetch detailed information about papers from PubMed IDs using EFetch."""
    if not pubmed_ids:
        return []
    
    details_url = f"{BASE_URL}/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml",  # Use XML since EFetch returns structured data
        "api_key": API_KEY
    }
    
    response = requests.get(details_url, params=params)
    if response.status_code == 200:
        return response.text  # Return raw XML for parsing
    else:
        print("Error fetching paper details:", response.status_code)
        return ""
