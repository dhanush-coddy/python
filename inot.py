def num1(a):
    def num2(n):
        res = a * n
        print(res)
        return num2 
    return num2  

obj = num1(10)
print(obj(5))      
