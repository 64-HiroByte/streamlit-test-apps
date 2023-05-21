# ブラウザに文字を表示させよう（st.write）
import streamlit as st

# 文字列
st.write('Hello *World!*')

# 絵文字（Streamlit独自の書き方）
st.write(':smile:')


# ↓↓↓　以下の内容は、こんなことも出来るといった紹介に留める

# # 関数の情報
# def my_func():
#     """This is a function."""
#     return "Hello, Streamlit!"

# st.write(my_func)

# # モジュールの表示
# import math

# st.write(math)


# # クラスの表示
# class MyClass:
#     """This is a class."""
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, {self.name}!"

# my_object = MyClass("Streamlit User")
# st.write(my_object)

# # 辞書の表示
# my_dict = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }

# st.write(my_dict)

# ↑↑↑　ここまでの内容を紹介に留める 


# 様々なオブジェクトの表示（例：データフレーム）
import pandas as pd

st.write('Pandas DataFrameの描画')
st.write(pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}))


# HTMLの許可
st.write(
    '<a href="https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/">絵文字ショートコード</a>',
    unsafe_allow_html=True
    )

# cssスタイル
st.write(
    '<p style="font-size:24px">フォントサイズ 24px</p>',
    unsafe_allow_html=True
    )
