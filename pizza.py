import csv
import sys

import tabulate as tabulate

if len(sys.argv) != 2:
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

extension = sys.argv[1]
extension = extension.split('.')
if extension[1] != "csv":
    sys.exit("Not a CSV file")

try:

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
