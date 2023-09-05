import requests
access_token = 'MjRkNjA3NzUtMjJmMi00YzQ2LWJmMWUtMjg3NDMxMzhjYmQ4M2Y0OTU5OWUtNDc2_P0A1_b7e3ec15-6d63-442e-9ee4-f9d3a59ed831'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjI2NjA3NzAtNGI5OC0xMWVlLWI0NTktNWQ4ODNmY2VmNGY4'
person_email = 'fernando.urena@sistemas.edu.bo'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())