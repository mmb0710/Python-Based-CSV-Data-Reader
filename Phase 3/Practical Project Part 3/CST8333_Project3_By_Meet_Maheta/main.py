# main.py

# Author: Meet Maheta

from traffic_manager import TrafficManager
from presentation import display_records, display_menu, get_user_choice, get_record_details, display_message

def main():
    """
    The main function to run the traffic data management program.
    It initializes the TrafficManager and provides a menu-driven interface for user interaction.
    """
   
    host = "localhost"  # e.g., "localhost"
    database = "traffic"  # e.g., "traffic_db"
    user = "mmb0702"  # e.g., "root"
    password = "System #1234"  # e.g., "password123"

    manager = TrafficManager(host, database, user, password)  # Initialize the TrafficManager with the given database parameters
    manager.create_table()  # Create the table if it does not exist

    while True:
        display_menu()  # Display the main menu
        choice = get_user_choice()  # Get the user's choice from the menu
        
        if choice is None:
            continue

        if choice == 1:
            display_message("Reloading data...")
            manager.reload_data()  # Reload data from the database
            display_message(f"Successfully loaded {len(manager.records)} records.")
        
        elif choice == 2:
            display_message("Saving data...")
            manager.save_data()  # Save data to the database
            display_message("Data saved successfully.")
        
        elif choice == 3:
            num_records = int(input("Enter the number of records to display: "))
            display_records(manager.records, num_records)  # Display the specified number of records
        
        elif choice == 4:
            display_message("Adding a new record...")
            details = get_record_details()  # Get new record details from the user
            manager.add_record({
                'section_id': details[0],
                'highway': details[1],
                'section': details[2],
                'section_length': float(details[3]),
                'section_description': details[4],
                'date': details[5],
                'description': details[6],
                'group': details[7],
                'type_': details[8],
                'county': details[9],
                'ptrucks': details[10],
                'adt': float(details[11]),
                'aadt': float(details[12]),
                'direction': details[13],
                'pct85': details[14],
                'priority_points': details[15]
            })  # Add the new record to the manager
            display_message("Record added successfully.")
        
        elif choice == 5:
            display_message("Editing a record...")
            id = int(input("Enter the index of the record to edit: "))
            details = get_record_details()  # Get updated record details from the user
            if manager.edit_record(id, {
                'section_id': details[0],
                'highway': details[1],
                'section': details[2],
                'section_length': float(details[3]),
                'section_description': details[4],
                'date': details[5],
                'description': details[6],
                'group': details[7],
                'type_': details[8],
                'county': details[9],
                'ptrucks': details[10],
                'adt': float(details[11]),
                'aadt': float(details[12]),
                'direction': details[13],
                'pct85': details[14],
                'priority_points': details[15]
            }):
                display_message("Record edited successfully.")
            else:
                display_message("Record not found.")
        
        elif choice == 6:
            display_message("Deleting a record...")
            id = int(input("Enter the index of the record to delete: "))
            if manager.delete_record(id):
                display_message("Record deleted successfully.")
            else:
                display_message("Record not found.")
        
        elif choice == 7:
            display_message("Demonstrating polymorphism...")
            manager.demonstrate_polymorphism()  # Demonstrate polymorphic method calls
        
        elif choice == 0:
            display_message("Exiting program.")
            break
        
        else:
            display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
