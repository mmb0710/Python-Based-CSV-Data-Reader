# special_traffic_record.py

# Author: Meet Maheta

from record_base import RecordBase

class SpecialTrafficRecord(RecordBase):
    """
    A subclass of RecordBase representing a special type of traffic record.
    """

    def __init__(self, section_id, highway, section, section_length, section_description, date, description, group, type_, county, ptrucks, adt, aadt, direction, pct85, priority_points):
        """
        Initialize a SpecialTrafficRecord object with the provided attributes by calling the superclass initializer.
        
        Parameters:
        -----------
        section_id : str
            The ID of the section.
        highway : str
            The name of the highway.
        section : str
            The section of the highway.
        section_length : float
            The length of the section.
        section_description : str
            The description of the section.
        date : str
            The date of the record.
        description : str
            The description of the record.
        group : str
            The group associated with the record.
        type_ : str
            The type of the record.
        county : str
            The county where the section is located.
        ptrucks : str
            The percentage of trucks in the traffic.
        adt : float
            The average daily traffic.
        aadt : float
            The annual average daily traffic.
        direction : str
            The direction of the traffic.
        pct85 : str
            The 85th percentile speed.
        priority_points : str
            The priority points of the section.
        """
        super().__init__(section_id, highway, section, section_length, section_description, date, description, group, type_, county, ptrucks, adt, aadt, direction, pct85, priority_points)

    def display(self):
        """
        Return a string representation of the special traffic record.
        
        Returns:
        --------
        str
            A string containing the type of the record and all its attributes in a special format.
        """
        return f"Special Traffic Record - {super().display()} [SPECIAL FORMAT]"
