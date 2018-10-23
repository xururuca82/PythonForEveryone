## 태극 모양을 그리는 프로그램

import turtle as t

t.bgcolor("black")      # 배경색을 검은색으로 지정합니다.
t.speed(3)              # 거북이 속도를 가장 바르게 지정합니다.

for x in range(200):    # for 반복 블록을 200번 실행합니다.
    if x%3 == 0:
        t.color("red")
    if x%3 == 1:
        t.color("yellow")
    if x%3 == 2:
        t.color("blue")
    t.forward(x*2)
    t.left(119)
