import korbit
import time

publicAPI = korbit.PublicAPI()



privateAPI = korbit.PrivateAPI(client_id='',  #Key
                        secret='')    #Secret
'''
코빗 사이트 로그인
'''
# 아이디와 비밀번호 입력
# 사용자 인증 결과로 Access Token, Refresh Token 발급됨. 접근 권한 같은 것.
# 이후 작업에는 아이디와 비밀번호 대신 Access Token을 사용한다.
# 매번 아이디와 비밀번호를 입력하는 수고를 덜어준다.
# 1시간후 자동 로그아웃됨 ( Access Token이 만료됨)
# Access Token 만료 전 Refresh Token을 이용하여 Access Token을 갱신할 수 있음
privateAPI.create_token_directly(username='',
                                 password='')
# 사용자 정보 가져오기
myInfo = privateAPI.get_user_info()
print(myInfo)

prevTime = time.mktime(time.localtime())
timeConnected = 0
bidOrderCount=0
while True:
    localTime = time.localtime()
    localTime_printable = "[{}.{}.{} | {}:{}]".format(localTime.tm_year, localTime.tm_mon, localTime.tm_mday, localTime.tm_hour, localTime.tm_sec)
    nowTime = time.mktime(localTime)
    timeDiff = nowTime - prevTime
    prevTime = nowTime
    timeConnected += timeDiff
    if timeConnected % 600 == 0:
        privateAPI.refresh_token()
    time.sleep(1)
    print(timeDiff)
    if timeConnected % 3600*24 == 0: # 매일 1회 5000원 매수

        if bidOrderCount > 0:
            status = privateAPI.bid_order(bid_type='market',fiat_amount=5000, currency_pair='btc_krw')
            print(status)
        bidOrderCount += 1


