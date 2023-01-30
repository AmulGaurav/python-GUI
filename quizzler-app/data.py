import requests

# paramters for the api in dictionary format
parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

# requesting Open-Trivia api for the data
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
# raise exception if response status code is not 200
response.raise_for_status()

# storing data in the form of dictionary in 'data' variable using .json() method
data = response.json()

# get hold of value from dictionary having key as "results"
question_data = data["results"]