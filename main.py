import json
from consumer_info import consumer_key, consumer_secret


if __name__ == '__main__':
  access_token = get_access_token(consumer_key, consumer_secret)
  si_list = get_address_data(access_token)

  output = {}

  for si in si_list:
    gu_list = get_address_data(access_token, si[0])
    
    output[si[1]] = {}
    
    for gu in gu_list:
      dong_list = get_address_data(access_token, gu[0])
      
      output[si[1]][gu[1]] = []
      
      for dong in dong_list:
        output[si[1]][gu[1]].append(dong[1])
        
        with open('output.json', 'w', encoding="UTF-8") as f:
          json.dump(output, f, ensure_ascii=False)
          
        print(si[1], gu[1], dong[1])
      