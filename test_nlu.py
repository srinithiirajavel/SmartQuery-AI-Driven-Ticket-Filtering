# tests/test_nlu.py

import unittest
from backend.nlu_module import parse_query

class TestNLUModule(unittest.TestCase):
    """
    Unit tests for the NLU module's query parsing function.
    """

    def test_parse_query_valid(self):
        """
        Test the query parser with a valid input.
        """
        result = parse_query("Show me tickets assigned to Alice with priority high")
        self.assertIn("tickets", result["attributes"])
        self.assertIn("assigned", result["attributes"])
        self.assertIn("Alice", result["values"])
        self.assertIn("high", result["operators"])

    def test_parse_query_no_operator(self):
        """
        Test query parser when no operators (adjectives/adverbs) are present.
        """
        result = parse_query("List tickets created by Bob")
        self.assertIn("tickets", result["attributes"])
        self.assertIn("created", result["attributes"])
        self.assertIn("Bob", result["values"])
        self.assertEqual(result["operators"], [])

    def test_parse_query_with_date(self):
        """
        Test query parser when a date is included.
        """
        result = parse_query("Show tickets due on 2024-09-15")
        self.assertIn("tickets", result["attributes"])
        self.assertIn("2024-09-15", result["values"])

    def test_parse_empty_query(self):
        """
        Test with an empty query string.
        """
        result = parse_query("")
        self.assertEqual(result["attributes"], [])
        self.assertEqual(result["values"], [])
        self.assertEqual(result["operators"], [])

if __name__ == '__main__':
    unittest.main()
