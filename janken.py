# -*- coding: utf-8 -*-
word = input()
print("your input: {}".format(word))

#ランダムに、グー、チョキ、パー、を決める
#こっちが、グーのとき、相手がグー、の時は、アイコ。チョキ、の時は、勝ち。パー、の時は、負け。
#こっちが、パーのとき、相手がグー、の時は、勝ち。チョキの時は、負け。パー、の時は、アイコ。
#こっちが、チョキの時、相手がグー、の時は、負け、チョキの時、アイコ、パーの時は、勝ち
#あいこの場合、もう一回 改めて、最初に戻る
#random, if, try

import random

dic = {"a": "グー", "b": "チョキ", "c": "パー"}

print("じゃんけーん")
print("a=グー, b=チョキ, c=パー,a,b,cのいずれかを入力")

try:
    user_choice: str = dic[user]
    
    choice_list = ["a", "b", "C"]
    pc = dic[random.choice(choice_list)]
    
    draw = 'ドロー'
    win = '勝ち！'
    lose = '負け'
    
    if user_choice == pc:
        judge = draw

    else:
        if user_choice == "グー":
            if pc == "チョキ":
                judge = win
            else:
                judge = lose


elif user_choice == "チョキ":
    if pc == "パー":
        judge = win
            else:
                judge = lose

    else:
        if pc == "グー":
            judge = win
            else:
                judge = lose

print("ありがとうございました。また！")

except:
    print("a,b,cのいずれかを入力してください。")

