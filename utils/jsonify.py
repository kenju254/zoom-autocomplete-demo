import os
import pandas as pd

# General File and Base Directories
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_DIR, "assets/data")

#Opening the Files to read and to write
productlistCsv = open(os.path.join(DATA_DIR, 'productlist.csv'))
productlistJson = open(os.path.join(DATA_DIR, 'productlist.json'))

df = pd.read_csv('productlistCsv')
df.to_json('productlistJson')