import requests
url = 'https://newsapi.org/v2/everything?domains=thehindu.com&apiKey=0ffeb62d7f0b4bfd99974ec4e58434e8'
response = requests.get(url)
print(response.json())
