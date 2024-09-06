# record_base.py

# Author: Meet Maheta

class RecordBase:
    """
    A base class representing a traffic record.
    
    Attributes:
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
    
    def __init__(self, section_id, highway, section, section_length, section_description, date, description, group, type_, county, ptrucks, adt, aadt, direction, pct85, priority_points):
        """
        Initialize a RecordBase object with the provided attributes.
        
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
        self.section_id = section_id
        self.highway = highway
        self.section = section
        self.section_length = section_length
        self.section_description = section_description
        self.date = date
        self.description = description
        self.group = group
        self.type_ = type_
        self.county = county
        self.ptrucks = ptrucks
        self.adt = adt
        self.aadt = aadt
        self.direction = direction
        self.pct85 = pct85
        self.priority_points = priority_points

    def display(self):
        """
        Return a string representation of the traffic record.
        
        Returns:
        --------
        str
            A string containing all the attributes of the traffic record.
        """
        return f"SECTION ID: {self.section_id}, HIGHWAY: {self.highway}, SECTION: {self.section}, SECTION LENGTH: {self.section_length}, SECTION DESCRIPTION: {self.section_description}, DATE: {self.date}, DESCRIPTION: {self.description}, GROUP: {self.group}, TYPE: {self.type_}, COUNTY: {self.county}, PTRUCKS: {self.ptrucks}, ADT: {self.adt}, AADT: {self.aadt}, DIRECTION: {self.direction}, 85PCT: {self.pct85}, PRIORITY_POINTS: {self.priority_points}"
