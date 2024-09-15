import unittest
from backend.query_translator import translate_query

class TestQueryTranslator(unittest.TestCase):
    def test_translate_query(self):
        parsed_query = {
            "attributes": ["assigned", "priority"],
            "values": ["Alice", "high"]
        }
        result = translate_query(parsed_query)
        expected = "assignee = 'Alice' AND priority = 'high'"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
