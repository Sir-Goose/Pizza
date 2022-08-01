import csv
import sys

import tabulate

# menu = sys.argv[1]
menu = "regular.csv"

with open(menu) as file:
    reader = csv.DictReader(file)
    print(reader)
    




