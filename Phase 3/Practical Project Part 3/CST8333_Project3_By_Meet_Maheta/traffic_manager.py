# traffic_manager.py

# Author: Meet Maheta

import mysql.connector
from mysql.connector import Error
from record import TrafficRecord
from special_traffic_record import SpecialTrafficRecord

class TrafficManager:
    """
    The TrafficManager class manages traffic records using MySQL database.
    """

    def __init__(self, host, database, user, password):
        """
        Initialize the TrafficManager with database connection details.

        Parameters:
        -----------
        host : str
            The hostname of the MySQL database.
        database : str
            The name of the MySQL database.
        user : str
            The username for the MySQL database.
        password : str
            The password for the MySQL database.
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = self.connect_to_db()  # Connect to the database
        self.records = self.load_data() if self.conn else []  # Load data if connection is successful

    def connect_to_db(self):
        """
        Establish a connection to the MySQL database.

        Returns:
        --------
        conn : mysql.connector.connection.MySQLConnection or None
            The MySQL connection object if successful, None otherwise.
        """
        try:
            conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if conn.is_connected():
                print("Connected to MySQL database")
            return conn
        except Error as e:
            print(f"Error: {e}")
            return None

    def create_table(self):
        """
        Create the traffic_volumes table if it does not exist.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS traffic_volumes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    section_id VARCHAR(255),
                    highway VARCHAR(255),
                    section VARCHAR(255),
                    section_length FLOAT,
                    section_description VARCHAR(255),
                    date DATE,
                    description VARCHAR(255),
                    group_ VARCHAR(255),
                    type_ VARCHAR(255),
                    county VARCHAR(255),
                    ptrucks VARCHAR(255),
                    adt FLOAT,
                    aadt FLOAT,
                    direction VARCHAR(255),
                    pct85 VARCHAR(255),
                    priority_points VARCHAR(255)
                )
            ''')
            self.conn.commit()
        except Error as e:
            print(f"Database error: {e}")

    def load_data(self):
        """
        Load data from the traffic_volumes table into the records list.

        Returns:
        --------
        records : list of TrafficRecord
            A list of TrafficRecord objects loaded from the database.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return []
        try:
            records = []
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM traffic_volumes")
            rows = cursor.fetchall()
            for row in rows:
                record = TrafficRecord(*row[1:])  # Exclude the auto-incremented ID
                records.append(record)
            return records
        except Error as e:
            print(f"Database error: {e}")
            return []

    def save_data(self):
        """
        Save the records list to the traffic_volumes table.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM traffic_volumes")  # Clear existing records
            for record in self.records:
                cursor.execute('''
                    INSERT INTO traffic_volumes (
                        section_id, highway, section, section_length, section_description,
                        date, description, group_, type_, county, ptrucks, adt, aadt,
                        direction, pct85, priority_points
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    record.section_id, record.highway, record.section, record.section_length,
                    record.section_description, record.date, record.description, record.group,
                    record.type_, record.county, record.ptrucks, record.adt, record.aadt,
                    record.direction, record.pct85, record.priority_points
                ))
            self.conn.commit()
        except Error as e:
            print(f"Database error: {e}")

    def add_record(self, record_data):
        """
        Add a new record to the records list and the database.

        Parameters:
        -----------
        record_data : dict
            A dictionary containing the data for the new record.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return
        record = TrafficRecord(**record_data)
        self.records.append(record)
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO traffic_volumes (
                    section_id, highway, section, section_length, section_description,
                    date, description, group_, type_, county, ptrucks, adt, aadt,
                    direction, pct85, priority_points
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                record.section_id, record.highway, record.section, record.section_length,
                record.section_description, record.date, record.description, record.group,
                record.type_, record.county, record.ptrucks, record.adt, record.aadt,
                record.direction, record.pct85, record.priority_points
            ))
            self.conn.commit()
        except Error as e:
            print(f"Database error: {e}")

    def edit_record(self, record_id, new_data):
        """
        Edit an existing record in the database.

        Parameters:
        -----------
        record_id : int
            The ID of the record to edit.
        new_data : dict
            A dictionary containing the updated data for the record.
        
        Returns:
        --------
        bool
            True if the record was successfully edited, False otherwise.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                UPDATE traffic_volumes SET
                    section_id=%s, highway=%s, section=%s, section_length=%s,
                    section_description=%s, date=%s, description=%s, group_=%s, type_=%s,
                    county=%s, ptrucks=%s, adt=%s, aadt=%s, direction=%s, pct85=%s, priority_points=%s
                WHERE id=%s
            ''', (
                new_data['section_id'], new_data['highway'], new_data['section'], new_data['section_length'],
                new_data['section_description'], new_data['date'], new_data['description'], new_data['group'],
                new_data['type_'], new_data['county'], new_data['ptrucks'], new_data['adt'], new_data['aadt'],
                new_data['direction'], new_data['pct85'], new_data['priority_points'], record_id
            ))
            self.conn.commit()
            return cursor.rowcount > 0  # Return True if a record was updated
        except Error as e:
            print(f"Database error: {e}")
            return False

    def delete_record(self, record_id):
        """
        Delete a record from the database.

        Parameters:
        -----------
        record_id : int
            The ID of the record to delete.
        
        Returns:
        --------
        bool
            True if the record was successfully deleted, False otherwise.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM traffic_volumes WHERE id=%s", (record_id,))
            self.conn.commit()
            return cursor.rowcount > 0  # Return True if a record was deleted
        except Error as e:
            print(f"Database error: {e}")
            return False

    def get_record(self, record_id):
        """
        Retrieve a record from the database by ID.

        Parameters:
        -----------
        record_id : int
            The ID of the record to retrieve.
        
        Returns:
        --------
        TrafficRecord or None
            The TrafficRecord object if found, None otherwise.
        """
        if not self.conn:
            print("Failed to connect to the database.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM traffic_volumes WHERE id=%s", (record_id,))
            row = cursor.fetchone()
            if row:
                return TrafficRecord(*row[1:])  # Exclude the auto-incremented ID
            return None
        except Error as e:
            print(f"Database error: {e}")
            return None

    def reload_data(self):
        """
        Reload the records list from the database.
        """
        self.records = self.load_data()

    def demonstrate_polymorphism(self):
        """
        Demonstrate polymorphism with TrafficRecord and SpecialTrafficRecord.
        """
        sample_records = [
            TrafficRecord("1", "Highway1", "Section1", "10", "Description1", "2023-01-01", "Desc1", "Group1", "Type1", "County1", "10", "1000", "2000", "North", "85", "10"),
            SpecialTrafficRecord("2", "Highway2", "Section2", "20", "Description2", "2023-01-02", "Desc2", "Group2", "Type2", "County2", "20", "2000", "3000", "South", "90", "20")
        ]
        for record in sample_records:
            print(record.display())
