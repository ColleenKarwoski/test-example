import os
import csv

cereal_csv=os.path.join("Resources","cereal.csv")

with open(cereal_csv) as cerealfile:
    reader = csv.reader(cerealfile)

    for row in reader: 
        print(row)
