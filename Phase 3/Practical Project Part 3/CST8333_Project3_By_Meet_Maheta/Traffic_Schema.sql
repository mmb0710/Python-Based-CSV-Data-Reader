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