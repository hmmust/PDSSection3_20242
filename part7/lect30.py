import requests

google = requests.get(url="https://www.google.com/search",
                      params={"q":"khalid abdeen"})
print(google.status_code)
print(google.url)
print(google.text)


