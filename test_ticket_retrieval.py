import unittest
from backend.ticket_retriever import get_tickets

class TestTicketRetriever(unittest.TestCase):
    def test_get_tickets(self):
        filter_query = "assignee = 'Alice' AND priority = 'high'"
        result = get_tickets(filter_query)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)  # Ensure that at least one ticket is returned
        self.assertEqual(result[0][1], 'Alice')  # Ensure that the first ticket’s assignee is Alice
        self.assertEqual(result[0][2], 'high')  # Ensure that the first ticket’s priority is high

if __name__ == '__main__':
    unittest.main()
