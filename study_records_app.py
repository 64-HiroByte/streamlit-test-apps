import os
from datetime import datetime

import pandas as pd
import streamlit as st


current_dir = os.getcwd()
files = [f for f in os.listdir(current_dir) if f.endswith('.py')]
files.insert(0, '-----')

CSV_FILE = 'study_records.csv'

mode_options = ['学習記録を残す', '学習記録を閲覧する']

mode = st.selectbox('どちらかを選択してください', options=mode_options)

# 学習記録を残す
if mode == mode_options[0]:
    selected_file = st.selectbox(':memo:ファイルを選択してください', options=files)

    if selected_file != files[0]:
        if selected_file:
            file_path = os.path.abspath(selected_file)
            with open(file_path, 'r') as f:
                code = f.read()
                st.code(code, language='python')
        note = st.text_area('学習した感想やメモを入力してください', height=300)
        
        if st.button('保存'):
            formatted_datetime = datetime.now().strftime('%Y-%m-%d_%H:%M')
            new_data = pd.DataFrame(
                {
                    'date_time': [formatted_datetime],
                    'file_name': [selected_file],
                    'code': [code],
                    'note': [note]
                }
            )
                
            if os.path.isfile(CSV_FILE):
                df = pd.read_csv(CSV_FILE)
                df = pd.concat([df, new_data])
            else:
                df = new_data
                
            df.to_csv(CSV_FILE, index=False)
            st.success('学習記録が保存されました')

# 学習記録を閲覧する            
elif mode == mode_options[1]:
    
    if os.path.isfile(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df['datetime_file'] = df['date_time'] + ' - ' + df['file_name']
        view_options = ['-----'] + df['datetime_file'].tolist()
        selected_data = st.selectbox(
            '閲覧するデータを選んで下さい', 
            options=view_options
            )
        if selected_data != view_options[0]:
            selected_datetime = selected_data.split(' - ')[0]
            selected_row = df[df['date_time'] == selected_datetime].iloc[0]
            
            st.code(selected_row['code'], language='python')
            st.markdown('---')
            st.write(selected_row['note'])
