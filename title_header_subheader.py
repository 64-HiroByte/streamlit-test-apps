# タイトル・見出しをつけよう（st.title, st.header, st.subheader）
import streamlit as st

# タイトルの表示
st.title('これは *タイトル* です:smile:')

# 文字色の指定（Streamlit独自の書き方）
st.title('これは *:red[タイトル]* :blue[です]:smile:')
st.write(
    """
    指定できる色は 
    blue, green, orange, red, violet
    """
    )

# ヘッダーの表示（タイトルと同じ）
st.header('これは *:red[ヘッダー]* :blue[です]:smile:')

# サブヘッダーの表示（タイトルと同じ）
st.subheader('これは *:red[サブヘッダー]* :blue[です]:smile:')




# anchorの使い方は、序盤で取り扱うと受講者が混乱するかも・・・
# 後半のセクションで取り扱うか検討

# # 引数 anchor の使い方
# # ナビゲーションメニュー
# st.markdown("""
#     - [Section 1](#section1)
#     - [Section 2](#section2)
# """)

# # セクション1
# st.title("Section 1", anchor="section1")
# st.write("This is section 1.")
# import math

# # モジュールの説明
# st.write(math)

# # セクション2
# st.title("Section 2", anchor="section2")
# st.write("This is section 2.")
