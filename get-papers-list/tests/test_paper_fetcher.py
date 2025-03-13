import unittest
from unittest.mock import patch
from paper_fetcher import fetch_papers, fetch_paper_info

class TestPaperFetcher(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_papers(self, mock_get):
        mock_response = {
            "esearchresult": {
                "idlist": ["12345", "67890"]
            }
        }
        mock_get.return_value.json.return_value = mock_response
        papers = fetch_papers("query", "api_key")
        self.assertEqual(len(papers), 2)

    @patch('requests.get')
    def test_fetch_paper_info(self, mock_get):
        mock_response = {
            "PubmedArticle": [
                {
                    "MedlineCitation": {
                        "Article": {
                            "ArticleTitle": "Title",
                            "Journal": {
                                "JournalIssue": {
                                    "PubDate": "2022-01-01"
                                }
                            },
                            "AuthorList": [
                                {
                                    "LastName": "Last",
                                    "ForeName": "First"
                                }
                            ]
                        }
                    }
                }
            ]
        }
        mock_get.return_value.json.return_value = mock_response
        paper_info = fetch_paper_info("12345", "api_key")
        self.assertEqual(paper_info["title"], "Title")
        self.assertEqual(paper_info["publication_date"], "2022-01-01")
        self.assertEqual(paper_info["authors"], ["Last, First"])

if __name__ == '__main__':
    unittest.main()
