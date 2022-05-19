import pymysql


# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='91raf2e5', db='bestproducts', charset='utf8')
# cursor = db.cursor()

# sql = '''

# '''

# cursor.execute(sql)

# db.commit()
# db.close()

### main category 정보 가져오기

import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers/')
soup = BeautifulSoup(res.content, 'html.parser')

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    print( 'http://corners.gmarket.co.kr/' + category['href'] + category.get_text())

def get_category()