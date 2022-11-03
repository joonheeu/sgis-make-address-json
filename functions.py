import requests

def get_access_token(consumer_key, consumer_secret):
  url = f'https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json?consumer_key={consumer_key}&consumer_secret={consumer_secret}'
  response = requests.get(url)
  response = response.json()
  access_token = response['result']['accessToken']
  return access_token

def get_address_data(access_token, cd=None):
  result = []
  url = f'https://sgisapi.kostat.go.kr/OpenAPI3/addr/stage.json?pg_yn=0&accessToken={access_token}'
  
  if cd:
    url += f'&cd={cd}'
    
  response = requests.get(url)
  response = response.json()
  for item in response['result']:
    code = item['cd']
    address_name = item['addr_name']
    result.append((code, address_name))
  return result