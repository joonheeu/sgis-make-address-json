# SGIS API를 통해 주소 JSON 만들기

### Key 발급
- [SGIS API](https://sgis.kostat.go.kr/)에 가입하여 인증키를 발급받고 `서비스 ID`와 `보안 Key`를 `consumer_info.py`에 넣습니다.
- (인증키발급센터 > 나의 인증키)
``` python
# consumer_info.py

consumer_key = 'SGIS에서 발급받은 서비스 ID'
consumer_secret = 'SGIS에서 발급받은 보안 Key'
```

### Functions
 - get_access_token 은 consumer 정보를 통해 access_toten을 반환 받는 함수입니다.
 - 참고로 받급받은 access_toten 은 4시간 마다 만료됩니다.
``` python
# functions.py
def get_access_token(consumer_key, consumer_secret):
  url = f'https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json?consumer_key={consumer_key}&consumer_secret={consumer_secret}'
  response = requests.get(url)
  response = response.json()
  access_token = response['result']['accessToken']
  return access_token
```

 - get_address_data 는 발급받은 access_token을 통해 address data를 반환받는 함수입니다.
``` python
# functions.py
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
```

