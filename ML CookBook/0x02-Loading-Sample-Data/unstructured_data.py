# Import libraries
import requests
# URL to download the txt file from
txt_url = "https://machine-learning-python-cookbook.s3.amazonaws.com/text.txt"
# Get the txt file
r = requests.get(txt_url)
# Write it to text.txt locally
with open('text.txt', 'wb') as f:
f.write(r.content)
# Read in the file
with open('text.txt', 'r') as f:
text = f.read()
# Print the content
print(text)
