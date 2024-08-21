# **Streamlit을 사용한 Yes24 도서 목록 웹사이트 ( 크롤링 )**

<br>

<div align="center">

![image](https://github.com/user-attachments/assets/afb5fdb1-5ec0-4690-8c65-4a287a627fb0)

</div>

<br>

## **Yse24 도서목록 크롤링**

```
react_book_urls = book_search('리액트')
python_book_urls = book_search('파이썬')
java_book_urls = book_search('자바')
c_book_urls = book_search('c언어')
Javascript_book_urls = book_search('자바스크립트')
```
<br>

"리액트", "파이썬", "자바", "C언어", "자바스크립트" 제목이 포함된 도서를 검색 및 크롤링

<br>

```
def book_search(keyword):
    driver = webdriver.Chrome()
    book_urls = []

    for page in range(1, 4):
        url = f'https://www.yes24.com/Product/Search?domain=ALL&query={keyword}&page={page}'
        driver.get(url)
        time.sleep(2)  # 페이지 로딩 대기
        
        soup = bs(driver.page_source, "html.parser")
        table = soup.find('ul', {'id': 'yesSchList'})
        
        for cont in table.find_all('a', {'class': 'gd_name'}):
            link = 'http://www.yes24.com' + cont.get('href')
            book_urls.append(link)
    
    return book_urls

def book_info(book_urls):
    dic = []
    for index, book_url in enumerate(book_urls):
        html = urlopen(book_url)
        soup = bs(html, "html.parser")
        img = soup.find('img', {'class':'gImg'}).get('src')
        title = soup.find('h2', {'class':'gd_name'}).text
        
        author_elem = soup.find('span', {'class': 'gd_auth'})
        author = author_elem.find('a').text if author_elem and author_elem.find('a') else "No Author"
        
        pub_elem = soup.find('span', {'class': 'gd_pub'})
        pub = pub_elem.text if pub_elem else "No Publisher"
        
        price = soup.find('span', {'class':'nor_price'}).text
        # price = int(price.replace(',', '').replace('원', '')) 

        sales_elem = soup.find('span', {'class':'gd_sellNum'})
        if sales_elem is not None:
            try:
                salesIndex_str = sales_elem.text.strip()
                salesIndex = int(''.join(re.findall(r'\d', salesIndex_str)))  # 숫자만 추출하여 문자열로 변환 후 합쳐서 정수로 변환
            except AttributeError:
                salesIndex = 0
        else:
            salesIndex = 0
        
        print(img, title, author, price, salesIndex)
        dic.append({'이미지': img, '제목':title,'저자' : author,'출판사' : pub, '가격':price, 'Link':book_url, '판매지수': salesIndex})
    pd.DataFrame(dic)
    
    return dic

```

<br>

크롤링한 도서 정보를 MongoDB에 저장
해당 Data를 바탕으로 Streamlit을 사용하여 웹사이트 제작

- 도서제목 카레고리별 도서 목록
- 판매지수, 가격순위 top10 목록
- 베스트셀러 120

<br>

<div align="center">

![image](https://github.com/user-attachments/assets/dc31f3fa-693b-478a-877c-a3cdd97296e0)

</div>

<br>

---



