import qrcode
import os
import pandas as pd

# Define the new public base URL
BASE_URL = "https://shrooq-notcharc.github.io/devices-pages/"

# Load the Excel file with device info
file_path = "devices.xlsx"  # Make sure this path is correct
df = pd.read_excel(file_path)

# Create folder for QR codes
output_folder = "qr_codes"
os.makedirs(output_folder, exist_ok=True)

# Generate QR codes for each device
for index, row in df.iterrows():
    device_name = str(row["Device Name"]).strip()
    
    if not device_name or device_name.lower() in ["nan", "nat"]:
        print(f"⚠ Skipping row {index}: Invalid device name '{device_name}'")
        continue

    # Generate the full URL
    qr_content = f"{BASE_URL}{device_name}.html"

    # Generate QR code
    qr = qrcode.make(qr_content)

    # Save QR code
    qr_filename = os.path.join(output_folder, f"{device_name}.png")
    qr.save(qr_filename)

    print(f"✅ QR code saved: {qr_filename}")

print("🎉 All QR codes have been regenerated with public links!")

