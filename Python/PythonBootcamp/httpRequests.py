import requests
# url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers = {"Accept" : "application/json"})
# data = response.json()

# print(data["joke"])


url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers = {"Accept" : "application/json"},
    params={"term" : "cat"})

data = response.json()

print(data["results"])