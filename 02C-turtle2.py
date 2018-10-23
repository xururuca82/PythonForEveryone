## 거북이 그래픽으로 도형을 그리는 프로그램(선 색 변경)

import turtle as t

# 삼각형 그리기
t.color("red")          # 펜 색상을 빨간색으로 바꿈니다.
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
t.color("green")        # 펜 색상을 녹색으로 바꿉니다.
t.pensize(3)            # 펜 굵기를 3으로 바꿉니다.
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

#원 그리기
t.color("blue")         # 펜 색상을을 파간색으로 바꿉니다.
t.pensize(5)            # 펜 굵기를 5로 바꿉니다.
t.circle(50)
