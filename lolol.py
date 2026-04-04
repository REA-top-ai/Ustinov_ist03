import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
basic = HTTPBasicAuth('user', 'pass')
qqq = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
print(qqq.json())

bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzMzMzMzMzMzMzIiwibmFtZSI6ItCQ0LvQtdC60YHQsNC90LTRgCDQo9GB0YLQuNC90L7QsiIsImFkbWluIjp0cnVlLCJpYXQiOjE1MTYyMzkwMjJ9.w8fWG6vtMBQ1mniBvs74T1IPMqPgIKIU7pMKbfwDNIA"
headers = {"Authorization": f"Bearer {bearer_token}"}
response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())

url = 'https://httpbin.org/digest-auth/auth/user/pass'
resp = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
print(resp.json())