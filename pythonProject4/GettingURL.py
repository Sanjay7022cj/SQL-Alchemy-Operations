import requests

# Example URL with student details
url = 'https://jsonplaceholder.typicode.com/users/1'  # Change this to your needs

# Send a GET request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    student_data = response.json()  # Assuming the response is JSON formatted
    print(student_data)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
