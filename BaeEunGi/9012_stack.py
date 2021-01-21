class Node:
    def __init__(self, data):
        self.data = data  #self. 를 사용하며 클래스 자기 자신을 가르킴
        self.next = None  #자신과 연결된 다음 Node를 가르킴

class Stack:
    def __init__(self):  #생성자(__  __)를 사용해서 객체를 선언할 때 자동적으로 가장 먼저 수행 됨
        self.head = None

    def is_empty(self):
        if not self.head:  #head 노드가 비어있으면 True
            return True
        else:
            return False
    
    def push(self, data):
        node = Node(data) #-> __init__(data) -> self.data = data, node.next = None
        node.next = self.head #head는 나중에 들어온 node가 된다.
        self.head = node #head에 입력받은 data값 할당
    
    def pop(self):
        if self.is_empty():
            return None
        result = self.head.data # 현재 head의 data를 반환
        self.head = self.head.next # head를 바꿔줍니다.
        return result
    
    
stack = Stack()#객체 생성
c=[]
T = int(input()) #입력 받는 괄호 문자열 개수
for j in range(T):
    stack.push(str(input())) #괄호 문자열을 push
for p in range(T):
    a = stack.pop()
    b = 0
    for i in range(len(a)): #기본적인 매커니즘은 '(' = +1, ')' = -1
        if a[i] == '(':
                b = b+1
        elif a[i] == ')':
            if b == 0:    #예외처리
                b = b+50
            else:
                b = b-1
    if b == 0:
        c.append(1) #YES
    else:
        c.append(0) #NO
c.reverse() #스택 특성 상 거꾸로 pop이 되기 때문에 재정렬 해준다.
for i in c:
    if i == 1:
        print("YES")
    else:
        print("NO")
