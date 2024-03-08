import sys

input = sys.stdin.readline

class Product:
    def __init__(self,name="codetree",code=50):
        self.name = name
        self.code = code
name,code = map(str,input().split())

pro = Product(name,int(code))
pro1 = Product()

print("product",pro1.code,"is",pro1.name)
print("product",pro.code,"is",pro.name)