import requests
import json

# Define the URL of the Flask service
url = 'http://api.cyaxios.com/process_payment'  # Update with your actual URL

# Define the payment data as a dictionary
payment_data = {
    "card_number": "1234567890123456",
    "amount": 100.00,
    "currency": "USD"
}

# Convert the payment data to JSON
headers = {'Content-type': 'application/json'}
json_data = json.dumps(payment_data)

# Make the POST request
response = requests.post(url, data=json_data, headers=headers)

# Check the response
if response.status_code == 200:
    result = response.json()
    print("Payment processed successfully:")
    print(result)
else:
    print("Payment processing failed. Response code:", response.status_code)
    print("Error message:", response.text)