import os
import csv , json

# General File and Base Directories
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, "assets/data")

#Opening the Files to read and to write
productlistCsv = open(os.path.join(DATA_DIR, 'productlist.csv'),'r')
productlistJson = open(os.path.join(DATA_DIR, 'productlist.json'),'w')

fieldNames = ("SKU", "Title", "Description")
reader = csv.DictReader(productlistCsv, fieldNames)
for row in reader:
    json.dump(row, productlistJson, encoding="latin1")
    productlistJson.write('\n')
