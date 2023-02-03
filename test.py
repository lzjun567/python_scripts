import requests

url = "http://210.1.227.58:9001/api/setcallback.php"

payload = "{\"wid\": \"33758168184\", \"callback_url\": \"http://43.153.104.20:5000/api/callback\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "c59c7e50-06e8-c3a0-6090-2f9861e7e03d"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.status_code)
print(response.text)