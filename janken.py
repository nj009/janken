# -*- coding: utf-8 -*-
import random

dic = {"a": "グー", "b": "チョキ", "c": "パー"}

print("じゃんけーん")
print("a=グー, b=チョキ, c=パー,a,b,cのいずれかを入力")
word = input()
print("your input: {}".format(word))

try:
    user_choice = dic.get(word)

    choice_list = ["a", "b", "c"]
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
    print(judge)
    print("ありがとうございました。また！")

except:
    print("a,b,cのいずれかを入力してください。")
