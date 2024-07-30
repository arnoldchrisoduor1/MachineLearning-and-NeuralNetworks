# Import libraries
import pandas as pd
# Google Sheet URL that downloads the sheet as a CSV
url = "https://docs.google.com/spreadsheets/d/"\
"1ehC-9otcAuitqnmWksqt1mOrTRCL38dv0K9UjhwzTOA/export?format=csv"
# Read the CSV into a dataframe
dataframe = pd.read_csv(url)
# View the first two