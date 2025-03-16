import os
import pandas as pd
import requests

# Load the Excel file
file_path = "/Users/shurooqalamoudi/Documents/Notch/Projects_Devices_Project/devices.xlsx"
df = pd.read_excel(file_path)

# Folder to store HTML pages
html_folder = "device_pages"
os.makedirs(html_folder, exist_ok=True)

# GitHub-hosted logo URL
logo_url = "https://shrooq-notcharc.github.io/devices-pages/logo-01.png"

# Google Apps Script Webhook (Replace with your actual Web App URL)
GOOGLE_SHEET_WEBHOOK = "https://script.google.com/macros/s/AKfycbwhXiBCmB9P1BEYlu-bJOH0InZ7MzOhvrUSUsuraROBw9do9UDasqRbQIXKSkvT2oVa/exec"

# Function to create an issue reporting button
def generate_issue_button(issue_type, color, device_name):
    return f'''
        <a href="#" onclick="submitIssue('{device_name}', '{issue_type}');" 
        class="button" style="background-color: {color};">{issue_type}</a>
    '''

# Generate an HTML file for each device
for index, row in df.iterrows():
    device_name = str(row["Device Name"]).strip()
    device_type = str(row.get("Device Type", "Unknown")).strip()
    assigned_to = str(row.get("Assigned To", "Unassigned")).strip()

    if not device_name or device_name.lower() in ["nan", "nat"]:
        print(f"⚠ Skipping row {index}: Invalid device name '{device_name}'")
        continue

    # HTML content with the logo and ticketing system
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{device_name} Details</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 20px; }}
            .container {{ max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }}
            h1 {{ color: #333; }}
            img.logo {{ width: 200px; margin-bottom: 20px; }}
            .button {{
                display: inline-block;
                margin: 10px;
                padding: 10px 20px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            input[type=email] {{
                width: 80%;
                padding: 8px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
        </style>
        <script>
            function submitIssue(deviceName, issueType) {{
                var employeeEmail = document.getElementById("employeeEmail").value;
                if (!employeeEmail) {{
                    alert("❌ Please enter your email before submitting.");
                    return;
                }}

                var data = {{
                    device_name: deviceName,
                    issue_type: issueType,
                    employee_email: employeeEmail
                }};

                fetch("{GOOGLE_SHEET_WEBHOOK}", {{
                    method: "POST",
                    body: JSON.stringify(data),
                    headers: {{ "Content-Type": "application/json" }}
                }})
                .then(response => response.text())
                .then(response => alert("✅ Ticket Created: " + response))
                .catch(error => alert("❌ Error creating ticket: " + error));
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <img class="logo" src="{logo_url}" alt="Company Logo">
            <h1>Device: {device_name}</h1>
            <p><strong>Type:</strong> {device_type}</p>
            <p><strong>Assigned To:</strong> {assigned_to}</p>
            
            <h2>Report an Issue</h2>
            <p><strong>Your Email:</strong></p>
            <input type="email" id="employeeEmail" placeholder="Enter your email" required>
            
            {generate_issue_button("Lagging", "#f4b400", device_name)}
            {generate_issue_button("Needs Maintenance", "#4285F4", device_name)}
            {generate_issue_button("Needs Repair", "#DB4437", device_name)}
        </div>
    </body>
    </html>
    """

    # Save the HTML file
    html_filename = os.path.join(html_folder, f"{device_name}.html")
    with open(html_filename, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"✅ HTML page created: {html_filename}")

print("🎉 All HTML pages have been regenerated successfully!")

