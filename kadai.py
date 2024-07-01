from PIL.Image import Image
import streamlit as st
import numpy as np
import time

#タイトルとサイドバー
st.title("スキマ時間にやる気を出す💪")
st.write("ついゴロゴロしちゃう・・・そんな時間を有効活用！")
st.write("少しずつでもタスクをこなしていこう😍")
name = st.sidebar.text_input("名前を入力してください")

#プルダウンで頑張る時間を選択する
options=["5分","10分","15分"]
selected_option=st.selectbox("何分頑張ってみる？:",options)

#5分、10分、15分でできるタスクをリスト化
task5=["ゴミ出し","保育園の準備","お茶を作る","机の上を拭く","お米を炊く"]
task10=["掃除機","洗面台の掃除","玄関の掃除","靴磨き","アイロン"]
task15=["風呂掃除","トイレ掃除","皿洗い","洗濯物を干す","おかずを1品作る"]

#5分を選択したときの実行後の動作
if selected_option=="5分"and st.button("今日はなにする？") :
   st.write(f" {name}さん、頑張ろうという気持ちがすごいです👏")
   time.sleep(3)
   index =np.random.randint(0,4)
   task = task5[index]
   st.write(f"## {task}")
   st.text("やればできるよ！")
   st.image("fight5.png")

#10分を選択したときの実行後の動作
if selected_option=="10分"and st.button("今日はなにする？") :
   st.write(f" {name}さん、10分も頑張れるって素敵💮")
   time.sleep(3)
   index = np.random.randint(0,4)
   task = task10[index]
   st.write(f"## {task}")
   st.text("やり始めるとすぐにできるよ！")
   st.image("fight10.png")

#15分を選択したときの実行後の動作
if selected_option=="15分"and st.button("今日はなにする？") :
   st.write(f" {name}さん、15分も頑張れるのはもはや天才😊")
   time.sleep(3)
   index = np.random.randint(0,4)
   task = task15[index]
   st.write(f"## {task}")
   st.text("ちょっと大変だけど、絶対にできるよ！")
   st.image("fight15.png")

# リセット
if st.button("TOPに戻る"):
  placeholder = st.empty()
  placeholder.empty()









