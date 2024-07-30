# Import libraries
import pymysql
import pandas as pd
# Create a DB connection
# Use the following example to start a DB instance
# https://github.com/kylegallatin/mysql-db-example
conn = pymysql.connect(
host='localhost',
user='root',
password = "",
db='db',
)
# Read the SQL query into a dataframe
dataframe = pd.read_sql("select * from data", conn)
# View the first two ro