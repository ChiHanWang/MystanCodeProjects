"""
File: webcrawler.py
Name: Michelle
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)  # requests向伺服器請求網頁資料
        html = response.text  # get the website's text
        # Beautiful Soup 會透過解析 HTML 原始碼，將其轉換成 Beautiful Soup 物件，利用這個物件就可以輕鬆找到網頁中的內容
        # features="html.parser"的用意就是幫BeautifulSoup指定一個HTML解析器
        soup = BeautifulSoup(html, features="html.parser")  # bs4將html轉成物件方便處理

        # ----- Write your code below this line ----- #

        tags = soup.tbody.text
        # print(tags)
        babys = tags.split()  # 以空格來切割，元素以list[]方式儲存
        # print(babys)

        # 以男女生數量的位置來設計
        malenum_index = 2
        femalenum_index = 4
        malenum = 0
        femalenum = 0
        for i in range(len(babys)):
            if babys[i] == 'Source:':
                break
            elif not babys[i].isalpha():
                if i == malenum_index:
                    malenum += int(babys[i].replace(',', ''))
                    malenum_index += 5
                elif i == femalenum_index:
                    femalenum += int(babys[i].replace(',', ''))
                    femalenum_index += 5
        print('Male number: ' + str(malenum))
        print('Female number: ' + str(femalenum))

        # # 以開關來設計
        # flag = False  # 判斷資料是否為英文名
        # added = False  # 判斷malenum += int(baby)是否已被執行一次
        # malenum = 0
        # femalenum = 0
        # for baby in babys:
        #     if baby == 'Source:':
        #         break
        #     elif baby.isalpha():
        #         flag = True
        #     elif flag:
        #         baby = baby.replace(',', '')  # 把number裡的逗號移除，替換成''
        #         if not added:
        #             malenum += int(baby)
        #             added = True
        #         else:
        #             femalenum += int(baby)
        #             added = False
        #         flag = False
        # print(f'Male Number: {malenum}')
        # print(f'Female Number: {femalenum}')


if __name__ == '__main__':
    main()