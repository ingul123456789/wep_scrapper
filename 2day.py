#함수
print("hello world") #이 함수는 파이썬에 기본적으로 포함되어 있음
def say_hello(): # 함수 이름은 변수 이름 지을 때와 같음/ 함수를 정의함
    print("hello how r u?") # 중간에 띄어쓰기는 이 코드가 어떤 함수에 해당하는지 알려주는 역할
say_hello() # 함수 사용(호출,call) () <- 함수안의 코드를 실행하는 버튼
def say_bye():
    print("bye bye")
 #  say_hello() say_bye 안에 say_hello를 넣은게 됨(띄어쓰기의 중요성) 
def test():
#print(test) 이코드만 썼을때 동작이 안되는 이유는 함수 안에 실행할 코드가 없어서임
    print(test)
