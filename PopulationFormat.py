# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:11:18 2024

@author: LENOVO
"""

import csv as cs

path = r"C:\Users\LENOVO\Desktop\pyprojects\world_population_data.csv"

with open('edited_population.csv', 'w', encoding='utf-8', newline='') as workable: 
    head_titles = ['Rank', 'Initials', 'Country', 'Continent', '2023', '2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970', 'Total']
    new_workable = cs.writer(workable)
    
    # Write the header row to the CSV file
    new_workable.writerow(head_titles)
    
    with open(path, 'r', encoding='utf-8') as pop_doc:
        # Create a CSV reader object
        reader = cs.reader(pop_doc)
        
        # Skip the header row
        next(reader)
        
        # Iterate over each row and write it to the new CSV file
        for row in reader:
            Rank = row[0]
            Initials = row[1]
            Country = row[2]
            Continent = row[3]
            Year_2023 =int(row[4])
            Year_2022 =int(row[5])
            Year_2020 =int(row[6])
            Year_2015 =int(row[7])
            Year_2010 =int(row[8])
            Year_2000 =int(row[9])
            Year_1990 =int(row[10])
            Year_1980 =int(row[11])
            Year_1970 =int(row[12])
            Total = Year_2023+Year_2022+Year_2020+Year_2015+Year_2010+Year_2000+Year_1990+Year_1980+Year_1970
            what_to_write = [Rank, Initials, Country, Continent, Year_2023, Year_2022, Year_2020, Year_2015, Year_2010, Year_2000, Year_1990, Year_1980, Year_1970,Total]
            
            # Write the current row to the new CSV file
            new_workable.writerow(what_to_write)
    
        
        
        
    