import qrcode
import os

# Define the folder to save QR codes
qr_folder = "qr_codes"

# Ensure the folder exists
os.makedirs(qr_folder, exist_ok=True)

# Iterate through each device and generate a QR code
for index, row in df.iterrows():
    device_name = str(row.get("Device Name", "")).strip()  # Convert to string & remove spaces

    if not device_name or device_name.lower() == "nan":
        print(f"⚠ Skipping row {index}: Invalid device name")
        continue  

    # QR code content (device details)
    qr_content = f"Device Name: {device_name}\nStatus: Working or Not?"

    # Generate QR code
    qr = qrcode.make(qr_content)

    # Save the QR code as an image
    qr_filename = os.path.join(qr_folder, f"{device_name}.png")
    qr.save(qr_filename)

    print(f"✅ QR code saved: {qr_filename}")

print("🎉 All QR codes have been generated successfully!")

