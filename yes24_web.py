import pandas as pd
import streamlit as st
from pymongo import MongoClient
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

mongo_url = 'mongodb+srv://axz1420:dlgusdn113!@store.jvq4o15.mongodb.net/?retryWrites=true&w=majority&appName=store'
client = MongoClient(mongo_url)
db = client['yes24']

javascript_book = db['Javascript_book']
c_book = db['c_book']
java_book = db['java_book']
python_book = db['python_book']
react_book = db['react_book']

best_seller_120 = db['yes24_best_seller_120']

#--------------------------------

logo_url = "https://image.yes24.com/sysimage/renew/gnb/logoN4.svg"
st.markdown(f"<div style='text-align: center; margin-bottom: 50px;'><img src='{logo_url}' width='200'></div>", unsafe_allow_html=True)


col1, blank, col2 = st.columns([2, 1,5])

#--------------------------------

# col 1



with col1:
    st.markdown("<h3 style='margin-bottom: -40px'>메뉴</h2>", unsafe_allow_html=True)
    st.write("---")
    category = st.selectbox('카테고리', ['자바스크립트', 'C언어', '자바', '파이썬', '리액트'])
    st.write("---")
    sales_rank_button = st.button('판매지수 top 10')
    price_rank_button = st.button('가격순위 top 10')
    st.write("---")
    best_seller_button = st.button('베스트셀러120')


#--------------------------------


# col 2

with col2:
    if best_seller_button:
        if sales_rank_button:
            data = best_seller_120.find()
            df = pd.DataFrame(data)
            df = df.drop(columns=['_id'])
            df['제목'] = df['제목'].apply(lambda x: '\n'.join(x[i:i + 12] for i in range(0, len(x), 12)))
            top10_sales = df.nlargest(10, '판매지수').reset_index(drop=True).drop(columns=['이미지'])

            st.markdown("<h4 style='text-align: center; margin-bottom: -20px'>베스트셀러120 판매지수 top 10</h4>", unsafe_allow_html=True)
            st.write("---")
            st.dataframe(top10_sales)

            fig, ax = plt.subplots(figsize=(20, 10))
            top10_sales.plot(kind='bar', x='제목', y='판매지수', ax=ax, legend=False)
            plt.xticks(rotation=0)
            st.pyplot(fig)

        elif price_rank_button:
            data = best_seller_120.find()
            df = pd.DataFrame(data)
            df = df.drop(columns=['_id'])
            df['가격'] = df['가격'].str.replace('원', '').str.replace(',', '').astype(float)
            df['제목'] = df['제목'].apply(lambda x: '\n'.join(x[i:i + 12] for i in range(0, len(x), 12)))

            top10_price = df.nlargest(10, '가격').reset_index(drop=True).drop(columns=['이미지'])
            st.markdown("<h4 style='text-align: center; margin-bottom: -20px'>베스트셀러120 가격순위 top 10</h4>", unsafe_allow_html=True)
            st.write("---")
            st.dataframe(top10_price)

            fig, ax = plt.subplots(figsize=(20, 10))
            top10_price.plot(kind='bar', x='제목', y='가격', ax=ax, legend=False)
            plt.xticks(rotation=0)
            st.pyplot(fig)

        else:
            data = best_seller_120.find()
            df = pd.DataFrame(data)
            df = df.drop(columns=['_id'])

            st.markdown("<h3 style='text-align: center; margin-bottom: -40px'>베스트셀러120 도서 목록 조회</h3>", unsafe_allow_html=True)
            st.write("---")

            for index, row in df.iterrows():
                st.image(row['이미지'], width=100)
                st.write(f"**제목 :** {row['제목']}")
                st.write(f"**저자 :** {row['저자']}")
                st.write(f"**출판사 :** {row['출판사']}")
                st.write(f"**가격 :** {row['가격']}")
                st.write(row['Link'])
                st.write("---")


    else:
        if sales_rank_button:
            data = None
            if category == '자바스크립트':
                data = javascript_book.find()
            elif category == 'C언어':
                data = c_book.find()
            elif category == '자바':
                data = java_book.find()
            elif category == '파이썬':
                data = python_book.find()
            elif category == '리액트':
                data = react_book.find()
            else:
                pass
            if data:
                df = pd.DataFrame(data)
                df = df.drop(columns=['_id'])
                df['제목'] = df['제목'].apply(lambda x: '\n'.join(x[i:i + 12] for i in range(0, len(x), 12)))
                top10_sales = df.nlargest(10, '판매지수').reset_index(drop=True).drop(columns=['이미지'])

                st.markdown(f"<h4 style='text-align: center; margin-bottom: -20px'>{category} 판매지수 top 10</h4>", unsafe_allow_html=True)
                st.write("---")
                top10_sales.index = top10_sales.index + 1
                st.dataframe(top10_sales)

                fig, ax = plt.subplots(figsize=(20, 10))
                top10_sales.plot(kind='bar', x='제목', y='판매지수', ax=ax, legend=False)
                plt.xticks(rotation=0)
                st.pyplot(fig)

        elif price_rank_button:
            data = None
            if category == '자바스크립트':
                data = javascript_book.find()
            elif category == 'C언어':
                data = c_book.find()
            elif category == '자바':
                data = java_book.find()
            elif category == '파이썬':
                data = python_book.find()
            elif category == '리액트':
                data = react_book.find()
            else:
                pass

            if data:
                df = pd.DataFrame(data)
                df = df.drop(columns=['_id'])
                df['가격'] = df['가격'].str.replace('원', '').str.replace(',', '').astype(float)
                df['제목'] = df['제목'].apply(lambda x: '\n'.join(x[i:i + 12] for i in range(0, len(x), 12)))

                top10_price = df.nlargest(10, '가격').reset_index(drop=True).drop(columns=['이미지'])
                st.markdown(f"<h4 style='text-align: center; margin-bottom: -20px'>{category} 가격순위 top 10</h4>", unsafe_allow_html=True)
                st.write("---")
                top10_price.index = top10_price.index + 1
                st.dataframe(top10_price)

                fig, ax = plt.subplots(figsize=(20, 10))
                top10_price.plot(kind='bar', x='제목', y='가격', ax=ax, legend=False)
                plt.xticks(rotation=0)
                st.pyplot(fig)

        else:
            data = None
            if category == '자바스크립트':
                data = javascript_book.find()
            elif category == 'C언어':
                data = c_book.find()
            elif category == '자바':
                data = java_book.find()
            elif category == '파이썬':
                data = python_book.find()
            elif category == '리액트':
                data = react_book.find()
            else:
                pass

            if data:
                df = pd.DataFrame(data)
                df = df.drop(columns=['_id'])

                st.markdown(f"<h3 style='text-align: center; margin-bottom: -40px'>{category} 도서 목록 조회</h3>", unsafe_allow_html=True)
                st.write("---")

                for index, row in df.iterrows():
                    st.image(row['이미지'], width=100)
                    st.write(f"**제목 :** {row['제목']}")
                    st.write(f"**저자 :** {row['저자']}")
                    st.write(f"**출판사 :** {row['출판사']}")
                    st.write(f"**가격 :** {row['가격']}")
                    st.write(row['Link'])
                    st.write("---")

#--------------------------------