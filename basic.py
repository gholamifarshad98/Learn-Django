import requests

# URL for the API endpoint
url = "localhost:8040/helloworld"

# Data for the POST request
post_data = {
    "name": "farshad",
}

# Perform POST request
response_post = requests.post(url, json=post_data)

# Check the status code and print the result
if response_post.status_code == 201:
    print("POST request successful!")
    print("Response:", response_post.json())
else:
    print(f"POST request failed with status code {response_post.status_code}")
