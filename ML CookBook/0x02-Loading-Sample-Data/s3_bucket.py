# Import libraries
import pandas as pd
# S3 path to CSV
s3_uri = "s3://machine-learning-python-cookbook/data.csv"
# Set AWS credentials (replace with your own)
ACCESS_KEY_ID = "xxxxxxxxxxxxx"
SECRET_ACCESS_KEY = "xxxxxxxxxxxxxxxx"
# Read the CSV into a dataframe
dataframe = pd.read_csv(s3_uri,storage_options={
"key": ACCESS_KEY_ID,
"secret": SECRET_ACCESS_KEY,
}
)
# View first two rows
dataframe.head(2)
