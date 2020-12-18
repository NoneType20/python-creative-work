













    


import requests
from bs4 import BeautifulSoup
import time

choice = 1
while choice == 1 :
    choice = 0


    print("=" * 100)
    Answer =input("""
    롤 랭킹 : a
    롤 개인전적 검색 : b
    대답 :""")
    print("=" * 100)

    # Answer = int(Answer)

    





#   랭킹검색 
    if Answer == "a" :
        ranking = 1
        while  ranking == 1 :
            ranking = 0

            page = 0
            page =input("몇페이지를 검색할까요? :")
            allow = page.isdigit()
            allow = str(allow)
            if  allow == "True"  :
                page = int(page)

                
                url = 'https://www.op.gg/ranking/ladder/page={}'.format(page)
                html = requests.get(url).text
                soup = BeautifulSoup(html,'html.parser')


                table = soup.find('table' , class_='ranking-table')

                rows = table.find_all('tr',class_='ranking-table__row')
                print("=" * 100)
                for row in rows : 
                    rank = row.find('td' , class_='ranking-table__cell ranking-table__cell--rank').get_text()
                    name = row.find('span').get_text()
                    Tier = row.find('td' , class_='ranking-table__cell ranking-table__cell--tier').get_text().strip()
                    LP   = row.find('td' , class_='ranking-table__cell ranking-table__cell--lp').get_text().strip()
                    level= row.find('td' , class_='ranking-table__cell ranking-table__cell--level').get_text().strip()
                    win  = row.find('span' , class_='winratio__text').get_text()



                    print("랭크 : {0} | 소환사 이름 : {1} | 티어 : {2}  | 점수 : {3}  | 레벨 : {4}  | 승률 : {5}".format(rank , name , Tier , LP , level , win))
                print("=" * 100)
                answer_rank =input("""
                다른 페이지 검색  : a
                선택화면 돌아가기 : 아무키나 누르시오
                대답 : """)
                print("=" * 100)
                if answer_rank == "a" :
                    ranking = 1
                else : 
                    # print("선택화면으로 돌아갑니다...")
                    choice = 1
                    break
                
            elif allow == "False" :
                print("정수로 적어주세요 ..")
                ranking= 1
                









# 전적 확인
    if Answer == "b" :
        Usertier = 1
        while Usertier == 1 :
            Usertier == 0
            user = input("검색할 소환사 이름 :")


            url2 = "https://www.op.gg/summoner/userName={0}".format(user)

            html2 = requests.get(url2).text
            soup2 = BeautifulSoup(html2,'html.parser')

            finder = soup2
            finder = str(finder)
            if 'SideContent' in finder :

                table2   = soup2.find('div' , class_='SideContent')



                sRank_table = table2.find('div' , class_='TierRankInfo')
                subrank_table = table2.find('div' , class_='sub-tier')
                most_content = table2.find_all('div' , class_='ChampionBox Ranked')
                
                
                



                srank     = sRank_table.find('div' , class_='TierRank') #솔랭티어
                subrank   = subrank_table.find('div' , class_='sub-tier__rank-tier') #자유랭 티어 

                srank_lp  = sRank_table.find('span' , class_='LeaguePoints') #솔랭점수

                subrank_LP= subrank_table.find('div' , class_='sub-tier__league-point') # 자유랭 점수

                srank_win = sRank_table.find('span' , class_='wins') # 솔랭 이긴판

                srank_lose = sRank_table.find('span' , class_='losses')  # 솔랭 진판 

                srank_percent = sRank_table.find('span' , class_='winratio') # 솔랭 승률

                subrank_percent = subrank_table.find('div' , class_='sub-tier__gray-text') # 자유랭 승률


                check = table2
                check = str(check)

                if check.count("ChampionName") >= 5 : 
                    A_most = most_content[0].find('div' , class_='ChampionName').get_text().strip()
                    B_most = most_content[1].find('div' , class_='ChampionName').get_text().strip()
                    C_most = most_content[2].find('div' , class_='ChampionName').get_text().strip()
                    D_most = most_content[3].find('div' , class_='ChampionName').get_text().strip()
                    E_most = most_content[4].find('div' , class_='ChampionName').get_text().strip()
                elif check.count("ChampionName") == 4 :
                    A_most = most_content[0].find('div' , class_='ChampionName').get_text().strip()
                    B_most = most_content[1].find('div' , class_='ChampionName').get_text().strip()
                    C_most = most_content[2].find('div' , class_='ChampionName').get_text().strip()
                    D_most = most_content[3].find('div' , class_='ChampionName').get_text().strip()
                    E_most = "전적이 없습니다."
                elif check.count("ChampionName") == 3 :
                    A_most = most_content[0].find('div' , class_='ChampionName').get_text().strip()
                    B_most = most_content[1].find('div' , class_='ChampionName').get_text().strip()
                    C_most = most_content[2].find('div' , class_='ChampionName').get_text().strip()
                    D_most = E_most = "전적이 없습니다."
                elif check.count("ChampionName") == 2 :
                    A_most = most_content[0].find('div' , class_='ChampionName').get_text().strip()
                    B_most = most_content[1].find('div' , class_='ChampionName').get_text().strip()
                    C_most =D_most =E_most = "전적이 없습니다."

                elif check.count("ChampionName") == 1 :
                    A_most = most_content[0].find('div' , class_='ChampionName').get_text().strip()
                    B_most =C_most =D_most =E_most = "전적이 없습니다."
                else :
                    A_most =B_most =C_most =D_most =E_most = "전적이 없습니다."


               
                
                
                
                srank , subrank , srank_lp , subrank_LP , srank_win , srank_lose , srank_percent , subrank_percent = map(str , [srank , subrank , srank_lp , subrank_LP , srank_win , srank_lose , srank_percent , subrank_percent])
                  
              
 
                 
                  
                  
                  
                 


                # srank
                srank = srank.replace("</div>" , "")
                srank = srank.replace('<div class="TierRank">' , "")
                srank = srank.replace('<div class="TierRank unranked">' , "")
                srank = srank.replace(" " , "")
                srank = srank.strip()


                subrank = subrank.replace("</div>" , "")
                subrank = subrank.replace('<div class="sub-tier__rank-tier unranked">' , "")
                subrank = subrank.replace('<div class="sub-tier__rank-tier">' , "")
                subrank = subrank.replace(" " , "")
                subrank = subrank.strip()

                srank_lp = srank_lp.replace('<span class="LeaguePoints">' , "")
                srank_lp = srank_lp.replace('</span>' , "")
                srank_lp = srank_lp.replace(" " , "")
                srank_lp = srank_lp.strip()


                subrank_LP = subrank_LP.replace('<div class="sub-tier__league-point">' , "")
                subrank_LP = subrank_LP.replace('<span class="sub-tier__gray-text">' , "")
                subrank_LP = subrank_LP.replace("</div>" , "")
                subrank_LP = subrank_LP.replace("</span>" , "")
                subrank_LP = subrank_LP.replace("/" , " , 승률 : ")


                srank_win = srank_win.replace('<span class="wins">' , "")
                srank_win = srank_win.replace('</span>' , "")

                srank_lose = srank_lose.replace('<span class="losses">' , "")
                srank_lose = srank_lose.replace('</span>' , "")

                srank_percent = srank_percent.replace('<span class="winratio">' , "")
                srank_percent = srank_percent.replace('</span>' , "")
                srank_percent = srank_percent.replace('Win Ratio' , "")

                subrank_percent = subrank_percent.replace('<div class="sub-tier__gray-text">' , "")
                subrank_percent = subrank_percent.replace('</div>' , "")
                subrank_percent = subrank_percent.replace(" " , "")
                subrank_percent = subrank_percent.strip()
                subrank_percent = subrank_percent.replace('WinRate' , "")

                
               
               
                print("=" * 100)
                print("""
                솔로랭크 티어 :{0}
                솔로랭크 정보 -> 점수 : {1} , 승률 : {4} {5} / {6}

                자유랭크 티어 :{2}
                자유랭크 정보 -> 점수 : {3} / {7}
                모스트 챔피언 순위 
                 1 : {8}
                 2 : {9}
                 3 : {10}
                 4 : {11}
                 5 : {12}
                """.format(srank , srank_lp , subrank , subrank_LP , srank_win , srank_lose , srank_percent , subrank_percent ,A_most , B_most , C_most , D_most , E_most ))
                print("=" * 100)
                
                answer_tier = input("""
                다른 소환사 검색하기 : a
                선택화면 돌아가기    : 아무키나 누르시오
                대답 : """)
                print("=" * 100)
                if answer_tier == "a" :
                    Usertier = 1
                    

                else  : 
                    # print("선택화면으로 돌아갑니다...")
                    choice = 1
                    break
            else : 
                print("없는 소환사 입니다 ...")
                Usertier = 1

    if Answer != "a" or "b" :  
        print("선택화면으로 돌아갑니다...")      
        choice = 1




















