def say_hello(user_name="anonymous"):    #user_name에 기본값을 설정해줌
    print("hello",user_name)

say_hello("seoungmin") #원래는 1개의 argument를 받아야 함
say_hello()     #아무것도 받지 않으면 user_name을 anonymous로 설정

def plus(a="test",b=2):
    if a=="test":
        print("plus 안에 제대로 된 2개의 argument 값을 주세요")
    else:
        print(a+b)

def minus(a="test",b=2):
   if a=="test":
        print("minus 안에 제대로 된 2개의 argument 값을 주세요")
   else:
        print(a-b)
def multiply(a="test",b=2):
    if a=="test":
        print("multiply 안에 제대로 된 2개의 argument 값을 주세요")
    else:
        print(a*b)
def divide(a="test",b=2):
    if a=="test":
        print("divide 안에 제대로 된 2개의 argument 값을 주세요")
    else:
        print(a/b)
def square(a="test",b=2):
    if a=="test":
        print("square 안에 제대로 된 2개의 argument 값을 주세요")
    else:
        print(a**b)

plus(2,3)
plus()
minus(2,3)
minus()
multiply(2,3)
multiply()
divide(2,3)
divide()
square(2,3)
square()

# +++++ps 1개의 parameter안에 default 값을 설정해주면 나머지 parameter들에게도 default 값을 설정해줘야함

def tax_calc(money):
    return money*0.35 # return -> 함수로부터 값을 받아내는 것
tax_pay = tax_calc(1500000)
print(tax_pay)