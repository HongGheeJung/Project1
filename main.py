## 함수 선언부
def add_func(n1, n2):
    retVal = n1 + n2
    return retVal

def sub_func(n1, n2):
    retVal = n1 - n2
    return retVal

def multwo_func(n1, n2):
    retVal = n1 ** n2
    return retVal

## 변수부

num1, num2, res = 10, 2, 0


## 메인 코드부

res = add_func(num1, num2)
print(num1, '+', num2, '=', res)


res = sub_func(num1, num2)
print(num1, '-', num2,'=', res)

res = multwo_func(num1, num2)
print(num1, '**', num2,'=', res)
