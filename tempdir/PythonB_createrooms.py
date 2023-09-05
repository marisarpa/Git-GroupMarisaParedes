import requests
access_token = 'MjRkNjA3NzUtMjJmMi00YzQ2LWJmMWUtMjg3NDMxMzhjYmQ4M2Y0OTU5OWUtNDc2_P0A1_b7e3ec15-6d63-442e-9ee4-f9d3a59ed831'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'title': 'Devnet-GroupMarisaParedes'}
res = requests.post(url, headers=headers, json=params)
print(res.json())

