import unittest
from paper_parser import parse_papers, is_academic_author, is_company_affiliation

class TestPaperParser(unittest.TestCase):
    def test_parse_papers(self):
        papers = [
            {
                "title": "Title",
                "publication_date": "2022-01-01",
                "authors": ["Last, First"]
            }
        ]
        parsed_papers = parse_papers(papers)
        self.assertEqual(len(parsed_papers), 1)
        self.assertEqual(parsed_papers[0]["title"], "Title")
        self.assertEqual(parsed_papers[0]["publication_date"], "2022-01-01")
        self.assertEqual(parsed_papers[0]["authors"], ["Last, First"])

    def test_is_academic_author(self):
        self.assertTrue(is_academic_author("University of California"))
        self.assertFalse(is_academic_author("Google"))

    def test_is_company_affiliation(self):
        self.assertTrue(is_company_affiliation("Pharmaceutical Company"))
        self.assertFalse(is_company_affiliation("University of California"))

if __name__ == '__main__':
    unittest.main()
