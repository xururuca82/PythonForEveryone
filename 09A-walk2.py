## 마음대로 걷는 거북이2

import turtle as t
import random

t.shape("turtle")               # '거북이' 모양의 거북이 그래픽을 사용합니다.
t.speed(0)

for x in range(500):            # 거북이를 500번 움직입니다.
    a = random.randint(1, 360)  # 1~360에서 아무 수나 골라 a에 저장합니다.
    t.setheading(a)             # 거북이 방향을 a 각도로 돌립니다.
    b = random.randint(1, 20)   # 1~20 사이에 있는 아무 수나 골라 b에 저장합니다.
    t.forward(b)
