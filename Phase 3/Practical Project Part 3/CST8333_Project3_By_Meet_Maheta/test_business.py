# test_business.py

# Author: Meet Maheta

import unittest
from traffic_manager import TrafficManager

class TestTrafficManager(unittest.TestCase):
    """
    Unit tests for the TrafficManager class.
    """

    def setUp(self):
        """
        Set up the test environment by initializing a TrafficManager instance
        and clearing the traffic_volumes table.
        """
        self.manager = TrafficManager('localhost', 'traffic', 'mmb0702', 'System #1234')
        self.manager.create_table()
        if self.manager.conn:
            cursor = self.manager.conn.cursor()
            cursor.execute("DELETE FROM traffic_volumes")
            self.manager.conn.commit()

    def test_add_record(self):
        """
        Test the add_record method to ensure it correctly adds a new record.
        """
        initial_count = len(self.manager.load_data())
        self.manager.add_record({
            'section_id': '9999', 'highway': 'H', 'section': 'S', 'section_length': 1.0,
            'section_description': 'Desc', 'date': '2023-01-01', 'description': 'Desc',
            'group': 'G', 'type_': 'T', 'county': 'C', 'ptrucks': 'P', 'adt': 1000.0,
            'aadt': 2000.0, 'direction': 'D', 'pct85': '85', 'priority_points': 'PP'
        })
        self.assertEqual(len(self.manager.load_data()), initial_count + 1)

    def test_reload_data(self):
        """
        Test the reload_data method to ensure it correctly reloads the data from the database.
        """
        self.manager.add_record({
            'section_id': '9999', 'highway': 'H', 'section': 'S', 'section_length': 1.0,
            'section_description': 'Desc', 'date': '2023-01-01', 'description': 'Desc',
            'group': 'G', 'type_': 'T', 'county': 'C', 'ptrucks': 'P', 'adt': 1000.0,
            'aadt': 2000.0, 'direction': 'D', 'pct85': '85', 'priority_points': 'PP'
        })
        self.manager.reload_data()
        self.assertGreater(len(self.manager.records), 0)

    def test_edit_record(self):
        """
        Test the edit_record method to ensure it correctly edits an existing record.
        """
        self.manager.add_record({
            'section_id': '9999', 'highway': 'H', 'section': 'S', 'section_length': 1.0,
            'section_description': 'Desc', 'date': '2023-01-01', 'description': 'Desc',
            'group': 'G', 'type_': 'T', 'county': 'C', 'ptrucks': 'P', 'adt': 1000.0,
            'aadt': 2000.0, 'direction': 'D', 'pct85': '85', 'priority_points': 'PP'
        })
        cursor = self.manager.conn.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        id = cursor.fetchone()[0]
        self.manager.edit_record(id, {
            'section_id': '9999', 'highway': 'H', 'section': 'S', 'section_length': 1.0,
            'section_description': 'Desc', 'date': '2023-01-01', 'description': 'Desc',
            'group': 'G', 'type_': 'T', 'county': 'C', 'ptrucks': 'P', 'adt': 2000.0,
            'aadt': 2000.0, 'direction': 'D', 'pct85': '85', 'priority_points': 'PP'
        })
        self.assertEqual(self.manager.get_record(id).adt, 2000.0)

    def test_delete_record(self):
        """
        Test the delete_record method to ensure it correctly deletes a record.
        """
        self.manager.add_record({
            'section_id': '9999', 'highway': 'H', 'section': 'S', 'section_length': 1.0,
            'section_description': 'Desc', 'date': '2023-01-01', 'description': 'Desc',
            'group': 'G', 'type_': 'T', 'county': 'C', 'ptrucks': 'P', 'adt': 1000.0,
            'aadt': 2000.0, 'direction': 'D', 'pct85': '85', 'priority_points': 'PP'
        })
        cursor = self.manager.conn.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        id = cursor.fetchone()[0]
        self.manager.delete_record(id)
        self.assertIsNone(self.manager.get_record(id))

    def test_demonstrate_polymorphism(self):
        """
        Test the demonstrate_polymorphism method to ensure it displays the correct output.
        """
        self.manager.demonstrate_polymorphism()

if __name__ == "__main__":
    unittest.main()
