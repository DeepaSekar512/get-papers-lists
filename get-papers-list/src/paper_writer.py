import pandas as pd

def save_to_csv(papers, filename="output.csv"):
    """Save extracted paper details to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
