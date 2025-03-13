import argparse
import re
from .paper_fetcher import search_pubmed, fetch_paper_details
from .paper_parser import extract_paper_info
from .paper_writer import save_to_csv

def sanitize_filename(query):
    """Sanitize query to create a valid filename"""
    return re.sub(r'\W+', '_', query).strip('_') + ".csv"

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Output filename (CSV)")

    args = parser.parse_args()

    if args.debug:
        print("Debug mode enabled")

    print(f"Searching PubMed for: {args.query}")
    pubmed_ids = search_pubmed(args.query)

    if not pubmed_ids:
        print("No results found.")
        return

    print(f"Fetching details for {len(pubmed_ids)} papers...")
    paper_data = fetch_paper_details(pubmed_ids)
    extracted_data = extract_paper_info(paper_data)

    # print("Fetch paper Details",paper_data)
    print("Extract Paper Info",extracted_data)
    # Use provided filename or generate one from query
    output_file = args.file if args.file else sanitize_filename(args.query)

    save_to_csv(extracted_data, output_file)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
