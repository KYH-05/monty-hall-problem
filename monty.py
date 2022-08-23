import random
print("Monty Hall problem")
repeat=int(input("반복 횟수:"))
success_notchange=0
success_change=0

for i in range(repeat):
  
  
  #초기 설정(문 설정)
  d1,d2,d3=0,0,0
  ds=[d1,d2,d3]
  select_sportcar=random.randint(0,2)
  ds[select_sportcar]="sportcar"
  select_goat=[0,1,2]
  del select_goat[select_sportcar]
  ds[select_goat[0]]="goat"
  ds[select_goat[1]]="goat"
  

  #문 선택
  first_door=random.randint(0,2)
  
  
  #바꾸지 않을 경우
  K=0  
  if ds[first_door]=="sportcar":
    K=1
    success_notchange=success_notchange+1 #성공횟수

    
  #바꿀경우(첫선택=spo면 바꿀때 무조건 실패, 첫선택=go면 바꿀때 무조건 성공)
  if K==0:
    success_change=success_change+1 #성공횟수
    
    
  

print()

  

print("바꾸지 않을 경우의 성공확률",round((success_notchange/repeat)*100,2))
print("바꿀 경우의 성공확률",round((success_change/repeat)*100,2))