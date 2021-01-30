from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)]) #1~N까지 리스트 생성

while(not (len(deque) == 1)): #원소의 개수가 1개가 아닌 동안
    deque.popleft()  #맨 왼쪽 pop
    move_num = deque.popleft() #그다음 왼쪽 pop
    deque.append(move_num) #오른쪽으로 넣어주기

print(deque[0])
