import pandas as pd

# Load the Excel file
file_path = "/Users/shurooqalamoudi/Documents/Notch/Projects_Devices_Project/devices.xlsx"
df = pd.read_excel(file_path)

# Print the first 10 rows of the 'Device Name' column
print(df[["Device Name"]].head(10))

