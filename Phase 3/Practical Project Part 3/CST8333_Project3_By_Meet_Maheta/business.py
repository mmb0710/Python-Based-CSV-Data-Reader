# business.py

# Author: Meet Maheta

import csv
from record import TrafficRecord
from special_traffic_record import SpecialTrafficRecord

class TrafficManager:
    """
    The TrafficManager class manages a collection of RecordBase objects.
    It provides methods to load, save, add, edit, delete, and retrieve records.
    """

    def __init__(self, filename):
        """
        Initialize the TrafficManager with the given filename.
        
        :param filename: The path to the CSV file containing traffic data.
        """
        self.filename = filename
        self.records = self.load_data(filename)

    def load_data(self, filename):
        """
        Load data from a CSV file and create TrafficRecord objects.
        
        :param filename: The path to the CSV file containing traffic data.
        :return: A list of TrafficRecord objects.
        """
        try:
            records = []
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    record = TrafficRecord(
                        row['SECTION ID'], row['HIGHWAY'], row['SECTION'], row['SECTION LENGTH'], 
                        row['SECTION DESCRIPTION'], row['Date'], row['DESCRIPTION'], row['GROUP'], 
                        row['TYPE'], row['COUNTY'], row['PTRUCKS'], row['ADT'], row['AADT'], 
                        row['DIRECTION'], row['85PCT'], row['PRIORITY_POINTS']
                    )
                    records.append(record)
            return records
        except FileNotFoundError:
            print("File not found.")
            return []

    def save_data(self):
        """
        Save the current list of TrafficRecord objects to a CSV file.
        """
        with open(self.filename, mode='w', newline='') as csvfile:
            fieldnames = ['SECTION ID', 'HIGHWAY', 'SECTION', 'SECTION LENGTH', 'SECTION DESCRIPTION', 
                          'Date', 'DESCRIPTION', 'GROUP', 'TYPE', 'COUNTY', 'PTRUCKS', 'ADT', 'AADT', 
                          'DIRECTION', '85PCT', 'PRIORITY_POINTS']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.records:
                writer.writerow({
                    'SECTION ID': record.section_id,
                    'HIGHWAY': record.highway,
                    'SECTION': record.section,
                    'SECTION LENGTH': record.section_length,
                    'SECTION DESCRIPTION': record.section_description,
                    'Date': record.date,
                    'DESCRIPTION': record.description,
                    'GROUP': record.group,
                    'TYPE': record.type_,
                    'COUNTY': record.county,
                    'PTRUCKS': record.ptrucks,
                    'ADT': record.adt,
                    'AADT': record.aadt,
                    'DIRECTION': record.direction,
                    '85PCT': record.pct85,
                    'PRIORITY_POINTS': record.priority_points
                })

    def add_record(self, record_data):
        """
        Add a new TrafficRecord to the list of records.
        
        :param record_data: A dictionary containing the data for the new record.
        """
        record = TrafficRecord(**record_data)
        self.records.append(record)

    def edit_record(self, index, new_data):
        """
        Edit an existing TrafficRecord in the list of records.
        
        :param index: The index of the record to edit.
        :param new_data: A dictionary containing the updated data for the record.
        :return: True if the record was successfully edited, False otherwise.
        """
        if 0 <= index < len(self.records):
            for key, value in new_data.items():
                setattr(self.records[index], key, value)
            return True
        return False

    def delete_record(self, index):
        """
        Delete a TrafficRecord from the list of records.
        
        :param index: The index of the record to delete.
        :return: True if the record was successfully deleted, False otherwise.
        """
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False

    def get_record(self, index):
        """
        Retrieve a TrafficRecord from the list of records.
        
        :param index: The index of the record to retrieve.
        :return: The TrafficRecord object if found, None otherwise.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def reload_data(self):
        """
        Reload the data from the CSV file.
        """
        self.records = self.load_data(self.filename)

    def demonstrate_polymorphism(self):
        """
        Demonstrate polymorphic method calls using different types of records.
        """
        sample_records = [
            TrafficRecord("1", "Highway1", "Section1", "10", "Description1", "2023-01-01", "Desc1", "Group1", "Type1", "County1", "10", "1000", "2000", "North", "85", "10"),
            SpecialTrafficRecord("2", "Highway2", "Section2", "20", "Description2", "2023-01-02", "Desc2", "Group2", "Type2", "County2", "20", "2000", "3000", "South", "90", "20")
        ]
        for record in sample_records:
            print(record.display())
