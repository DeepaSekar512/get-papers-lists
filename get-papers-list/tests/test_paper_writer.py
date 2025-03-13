import unittest
from paper_writer import write_papers
import csv
import os

class TestPaperWriter(unittest.TestCase):
    def test_write_papers(self):
        papers = [
            {
                "title": "Title",
                "publication_date": "2022-01-01",
                "authors": ["Last, First"],
                "non_academic_authors": [],
                "company_affiliations": []
            }
        ]
        filename = "output.csv"
        write_papers(papers, filename)
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["title"], "Title")
            self.assertEqual(rows[0]["publication_date"], "2022-01-01")
            self.assertEqual(rows[0]["authors"], "Last, First")
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
