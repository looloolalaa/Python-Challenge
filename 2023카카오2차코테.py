# 전체적인 API 호출 흐름 파악
import requests
import json


base_url = 'https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/'
x_auth_token = '277c9db033ae4a4b13371fde'

def start(problem):
    headers = {'X-Auth-Token': x_auth_token, 'Content-Type': 'application/json'}
    data = {'problem': problem}
    return requests.post(url=base_url+'start', headers=headers, data=json.dumps(data)).json()

auth_key = 'a51ea8eb-f8b1-4d82-b2a3-9d6375ef30b4'
# auth_key = start(1)['auth_key']


def get_requests():
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=base_url+'new_requests', headers=headers).json()

def simulate():
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'room_assign': [
        {'id': 867284, 'room_number': 1001},
        {'id': 867284, 'room_number': 1002},
        {'id': 867284, 'room_number': 1003},
        {'id': 867284, 'room_number': 1004}
    ]}
    return requests.put(url=base_url+'simulate', headers=headers, data=json.dumps(data)).json()

def score_response():
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    return requests.get(url=base_url+'score', headers=headers).json()

while score_response()['score'] == 0:
    # get_requests() 호텔 예약 요청을 받아서
    # ~내부 데이터로 승낙할지말지 정하고~

    # reply_api(): 승낙 or 거절 보내기
    # simulate(): 손님을 호텔방에 등록시키고, 하루(1일) 진행시키기
    print(score_response())

print('done!')
print(score_response())

