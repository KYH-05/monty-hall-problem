import random
import matplotlib.pyplot as plt
import numpy as np

print("Monty Hall problem")
size = int(input("Size:"))
repeat=[]
for i in range(1,size+1):
  repeat.append(i)
success_notchange = [0 for i in range(0,size)]
success_change  = [0 for i in range(0,size)]

for k in range(0,size):
  for i in range(repeat[k]):

      # 초기 설정(문 설정)
      d1, d2, d3 = 0, 0, 0
      ds = [d1, d2, d3]
      select_sportcar = random.randint(0, 2)
      ds[select_sportcar] = "sportcar"
      select_goat = [0, 1, 2]
      del select_goat[select_sportcar]
      ds[select_goat[0]] = "goat"
      ds[select_goat[1]] = "goat"

      # 문 선택
      first_door = random.randint(0, 2)

      # 바꾸지 않을 경우
      K = 0
      if ds[first_door] == "sportcar":
          K = 1
          success_notchange[k] = success_notchange[k] + 1  # 성공횟수

      # 바꿀경우(첫선택=spo면 바꿀때 무조건 실패, 첫선택=go면 바꿀때 무조건 성공)
      if K == 0:
          success_change[k] = success_change[k] + 1  # 성공횟수

for i in range(len(repeat)):
    success_change[i]=success_change[i]/size*100
    success_notchange[i] = success_notchange[i] / size*100

x = repeat
y1 = success_change
y2= success_notchange
y66=[(66+(2/3))for i in range(len(repeat))]
y33=[(33+(1/3))for i in range(len(repeat))]

plt.plot(x, y1,color='blue')
plt.plot(x, y2,color='orange')
plt.plot(x,y66,color='green')
plt.plot(x,y33,color='red')

plt.xlabel('repeat')
plt.ylabel('probability')
plt.legend(('change','not change','66.666..','33.333..'))
plt.xlim(0,len(repeat))
plt.ylim(0,100)
plt.show()
