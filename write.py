import streamlit as st

# 文字列
st.write('Hello World')

# 絵文字
st.write(':smile:')

# HTMLの許可
st.write('<a href="https://www.google.com/">Google</a>', unsafe_allow_html=True)

# cssスタイル
st.write('<p style="font-size:24px">フォントサイズ 24px</p>', unsafe_allow_html=True)
