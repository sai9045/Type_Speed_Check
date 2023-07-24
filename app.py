from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import random
import time
import re

global start, stop, l_list, text, l,t_len,p_len
df = pd.read_csv('texts_typing.csv', encoding="cp1252")
df = df.dropna()
print(df)
L = df['Text']
l=""
test_list=[]
app = Flask(__name__)


@app.route('/')
def home():
    global start, stop, l_list, l
    start = time.time()
    l = random.choice(L)
    l_list = l.split(' ')
    print(l_list)
    return render_template("home.html")


@app.route('/play', methods=['POST', 'GET'])
def play():
    global stop, start, L, text, l,t_len,p_len

    text = request.form.get('text_typed')
    print(text)
    stop = time.time()
    if text is not None:
        return redirect(url_for('check_results'))
    return render_template("play.html", l=l)

@app.route('/Check_the_results')
def check_results():
    global start, stop, l_list, text,t_len,p_len
    print("hello")
    text_list = text.split()
    count = 0
    for i in text_list:
        if i in l_list:
            count = count + 1
    accuracy = count / len(l_list)
    total_time_taken = stop - start
    total_time_taken_min = total_time_taken / 60
    total_time_taken_min_round = round(total_time_taken_min)
    speed = len(text_list) / total_time_taken_min
    speed_round = round(speed)
    accuracy_100 = accuracy * 100
    accuracy_100_round=round(accuracy_100,1)
    print(l_list)
    print(text_list)
    print(total_time_taken_min)
    print(speed)
    print(speed_round)

    return render_template("check_r.html", accuracy=accuracy_100_round, total_time_taken=total_time_taken_min_round,
                           speed=speed_round,)


if __name__ == "__main__":
    app.run(debug=True)
