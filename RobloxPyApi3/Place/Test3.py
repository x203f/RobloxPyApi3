import requests

site_token = requests.post(
    'https://auth.roblox.com/v1/usernames/validate'
).headers['x-csrf-token']
print(site_token)