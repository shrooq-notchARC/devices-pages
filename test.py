import requests

GOOGLE_SHEET_WEBHOOK = "https://script.google.com/macros/s/AKfycbwhXiBCmB9P1BEYlu-bJOH0InZ7MzOhvrUSUsuraROBw9do9UDasqRbQIXKSkvT2oVa/exec"

test_payload = {
    "device_name": "TEST-DEVICE",
    "assigned_to": "Test User",
    "issue_type": "Test Issue",
    "last_updated": "2025-03-14 12:00:00"
}

response = requests.post(GOOGLE_SHEET_WEBHOOK, json=test_payload)

print(f"📡 Response from Google Sheets: {response.text}")
print(f"✅ HTTP Status Code: {response.status_code}")


