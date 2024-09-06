# presentation.py

# Author: Meet Maheta

def display_menu():
    """
    Display the main menu to the user.
    """
    print("\nProgram by Meet Maheta")
    print("1. Reload data")
    print("2. Save data")
    print("3. Display records")
    print("4. Add a new record")
    print("5. Edit a record")
    print("6. Delete a record")
    print("7. Demonstrate polymorphism")  # Added new option
    print("0. Exit")

def get_user_choice():
    """
    Get the user's menu choice.

    Returns
    -------
    int or None
        The user's choice as an integer, or None if the input is invalid.
    """
    try:
        choice = int(input("Enter your choice: "))
        if choice in range(8):  # Updated range to include the new option
            return choice
    except ValueError:
        pass
    print("Invalid choice, please try again.")
    return None

def display_records(records, num_records): 
    """
    Display a specified number of traffic records.

    Parameters
    ----------
    records : list of TrafficRecord
        The list of TrafficRecord objects to display.
    num_records : int
        The number of records to display.
    """
    for record in records[:num_records]:
        print(f"SECTION ID: {record.section_id}, HIGHWAY: {record.highway}, SECTION: {record.section}, "
              f"SECTION LENGTH: {record.section_length}, SECTION DESCRIPTION: {record.section_description}, "
              f"DATE: {record.date}, DESCRIPTION: {record.description}, GROUP: {record.group}, TYPE: {record.type_}, "
              f"COUNTY: {record.county}, PTRUCKS: {record.ptrucks}, ADT: {record.adt}, AADT: {record.aadt}, "
              f"DIRECTION: {record.direction}, 85PCT: {record.pct85}, PRIORITY_POINTS: {record.priority_points}")

def get_record_details():
    """
    Get the details of a traffic record from the user.

    Returns
    -------
    tuple
        A tuple containing the details of the traffic record.
    """
    section_id = input("Enter SECTION ID: ")
    highway = input("Enter HIGHWAY: ")
    section = input("Enter SECTION: ")
    section_length = input("Enter SECTION LENGTH: ")
    section_description = input("Enter SECTION DESCRIPTION: ")
    date = input("Enter Date: ")
    description = input("Enter DESCRIPTION: ")
    group = input("Enter GROUP: ")
    type_ = input("Enter TYPE: ")
    county = input("Enter COUNTY: ")
    ptrucks = input("Enter PTRUCKS: ")
    adt = input("Enter ADT: ")
    aadt = input("Enter AADT: ")
    direction = input("Enter DIRECTION: ")
    pct85 = input("Enter 85PCT: ")
    priority_points = input("Enter PRIORITY_POINTS: ")
    return section_id, highway, section, section_length, section_description, date, description, group, type_, county, ptrucks, adt, aadt, direction, pct85, priority_points

def display_message(message):
    """
    Display a message to the user.

    Parameters
    ----------
    message : str
        The message to display.
    """
    print(message)
