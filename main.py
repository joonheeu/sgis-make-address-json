import json, requests

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

consumer_key = 'db21a3b2cf1e49af9d90'
consumer_secret = '715b5bcfa2614367a3d6'

access_token = get_access_token(consumer_key, consumer_secret)
result = get_address_data(access_token)

output = {}

for item in result:
  result_2 = get_address_data(access_token, item[0])
  
  output[item[1]] = {}
  
  for item_2 in result_2:
    result_3 = get_address_data(access_token, item_2[0])
    
    output[item[1]][item_2[1]] = []
    
    for item_3 in result_3:
      output[item[1]][item_2[1]].append(item_3[1])
      print(output)
      with open('output.json', 'w', encoding="UTF-8") as f:
        json.dump(output, f, ensure_ascii=False)
    