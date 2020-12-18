#######################################################
# 5분간격으로 corona-live.com(코로나 라이브) 에서 확진자 정보를 가져와 그래프 생성
# select_time 다른 숫자로 바꿔 시간 조정 가능  , 60 = 5시간 ( 5분 * 61)
select_time = 60
from matplotlib import pyplot as plt
import time
import requests
from bs4 import BeautifulSoup
plus = 0
finish_num = 0
list_y= [] # 그래프 x
list_x = [] # 그래프 y
time_xy = [] # 시간 
while finish_num <= select_time  : 
    req = requests.get("https://apiv2.corona-live.com/stats.json?timestamp=")
    src = req.content 
    soup = str(BeautifulSoup(src,'html.parser'))
    result = soup[soup.index('{"current":[') + 12 : soup.index('"recovered"') -2]
    ing = result[0:result.index(',')]
    ed = result[result.index(',')+1 :]
    finish_num += 1 
    if int(ing) >= int(plus) : 
        plus = int(ing) - int(plus)
    print(str(finish_num) + ': 현재 : ' + str(ing) + ', 전 기록 + ' + str(plus) , ' , 어제 동시간 대비 : ' + ed)
    plus = ing
    list_y.append(int(ing))
    secs_ = time.time()
    tm = time.localtime(secs_)
    time_li = str(tm.tm_hour) + ':' + str(tm.tm_min)
    time_xy.append(time_li)
    time.sleep(300) 
for i in range(1 , len(list_y)+1): 
    list_x.append(int(i*5))
print('==========================')
print('result')
print(list_x)
print(list_y) 
print(time_xy)
print('==========================')
plt.plot(list_x , list_y) 
plt.show()





# 결과 표시줄 ---
# (ex)  첫줄 = list_x (5분간격 시간 , 그래프 x축) 둘째줄 = list_y ( 코로나 현황 , 그래프 y축 ) 셋째줄 = time_xy( 코로나 확진자 현황의 시간 )
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]
# [139, 139, 139, 139, 145, 153, 153, 153, 153, 156, 158, 163, 170, 172, 174, 179, 179, 214, 214, 220, 233, 234, 235, 235, 248, 252, 253, 254, 258, 258, 264, 264, 264, 271, 273, 273, 279, 280, 290, 291, 294, 295, 318, 318, 335, 335, 335, 336, 336, 365, 375, 378, 379, 384, 395, 409, 409, 410, 410, 423]
# ['12:15', '12:20', '12:25', '12:31', '12:36', '12:41', '12:46', '12:51', '12:56', '13:1', '13:6', '13:11', '13:16', '13:21', '13:26', '13:31', '13:36', '13:41', '13:46', '13:51', '13:56', '14:1', '14:6', '14:11', '14:16', '14:21', '14:26', '14:31', '14:36', '14:41', '14:46', '14:51', '14:56', '15:1', '15:6', '15:11', '15:16', '15:21', '15:26', '15:31', '15:36', '15:41', '15:46', '15:51', '15:56', '16:1', '16:6', '16:11', '16:16', '16:21', '16:26', '16:31', '16:36', '16:41', '16:46', '16:51', '16:56', '17:1', '17:6', '17:11']