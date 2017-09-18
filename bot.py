import korbit
import time
import privateInfo
import timeHelper

publicAPI = korbit.PublicAPI()
myID = privateInfo.myID()

privateAPI = korbit.PrivateAPI(client_id=myID.key,  #Key
                        secret=myID.secret)    #Secret
'''
코빗 사이트 로그인
'''
# 아이디와 비밀번호 입력
# 사용자 인증 결과로 Access Token, Refresh Token 발급됨. 접근 권한 같은 것.
# 이후 작업에는 아이디와 비밀번호 대신 Access Token을 사용한다.
# 매번 아이디와 비밀번호를 입력하는 수고를 덜어준다.
# 1시간후 자동 로그아웃됨 ( Access Token이 만료됨)
# Access Token 만료 전 Refresh Token을 이용하여 Access Token을 갱신할 수 있음
privateAPI.create_token_directly(username=myID.username,
                                 password=myID.password)
# 사용자 정보 가져오기
myInfo = privateAPI.get_user_info()
print(myInfo)

timeHelper = timeHelper.TimeHelper()

while True:
    timeHelper.tick()
    if timeHelper.timeConnected() % 600 == 0:
        privateAPI.refresh_token()

    if timeHelper.timeFromLastBidOrder() > 3600*24: # 매일 1회 5000원 매수
        status = privateAPI.bid_order(bid_type='market',fiat_amount=5000, currency_pair='btc_krw')
        timeHelper.record(ordertype='bid')
        print(timeHelper.printableLocalTime() + ' Bid order | Price: ' + publicAPI.ticker()['last'] + 'KRW/BTC | Amount: 5000KRW')


