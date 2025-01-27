import requests
import time

API_KEY = "UQWc4yHAdnwYsz9527TIxabPJueCNrXM"
URL = "https://core.ac.uk/contact"

user_request = input("Enter the subject of the journal, article and research papers you are looking for: \n")

header = {
    'Authorisation': f'Bearer {API_KEY}',
    'Accept': 'application/json'
}

params ={
    'q':user_request,
    'language':"en",
    'journals': user_request,
    'sort': 'relevance'
}

max_retries = 5
retry_delay = 5

for attempt in range(max_retries):
    response = requests.get(url=URL, headers=header, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        break
    elif response.status_code == 530:
        print(f'Error {response.status_code}: Server Unavailable. Retrying in a {retry_delay}seconds')
        time.sleep(retry_delay)
    else:
        print(f'Error: {response.status_code}')
else:
    print("Oops! Service not available")
