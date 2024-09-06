# Meet Maheta
import csv

class TrafficRecord:
    def __init__(self, data):
        """Initializes a TrafficRecord with a dictionary of data.
        
        Args:
            data (dict): A dictionary containing the data for the traffic record.
        """
        self.data = {key: (value if value != '' else 'N/A') for key, value in data.items()}
        

    def __str__(self):
        """Returns a string representation of the TrafficRecord.
        
        Returns:
            str: A formatted string representation of the traffic record.
        """
        return '\n'.join(f"{key}: {value}" for key, value in self.data.items())
    

def read_csv(file_path):
    """Reads the CSV file and returns a list of TrafficRecord objects.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        list: A list of TrafficRecord objects.
    """
    records = []
    try:
        with open(file_path, newline='') as csvfile: # Meet Maheta
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = TrafficRecord(row)
                records.append(record)
    except FileNotFoundError:
        print("The file is not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return records

def display_records(records):
    """Displays the data of each TrafficRecord.
    
    Args:
        records (list): A list of TrafficRecord objects.
    """
    for record in records:
        print(record)
        print() 
        # Meet Maheta

if __name__ == "__main__":
    file_path = 'Traffic_Volumes_-_Provincial_Highway_System.csv'
    records = read_csv(file_path) # Meet Maheta
    if records:
        display_records(records[:5])  # Display first 5 records
    print("\nFull Name: Meet Maheta")  # Meet Maheta
