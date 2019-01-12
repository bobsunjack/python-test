import sklearn
import pandas as pd
import fun.fun1 as pp
import json

name="   test organge  "
age=10

dogs=["one","two"]
for item in dogs:
    print(item)

for value in range(2,3):
    print(value)

nums=list(range(1,6))
print(nums)

print(3**2)

dogs=[value*3 for value in range(1,5)]
print(dogs)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
p2=players[-1:]
p2.append("qxb")

print(p2)
if "qxb2" in p2:
    print("include")

requsts=[1]
if requsts:
    print("null")

infos={"name":"mongo"}
infos["1"]="one"
print(infos)

del infos["1"]
print(infos)

for key,value in infos.items():
    print(key+":"+value)

for key in infos.keys():
    print(infos[key])
for value in infos.values():
    print(value)

dogs=["one","one"]
dog_=set(dogs)
print(dog_)

##message=input("input")
##print(message)

def show(name,age):
    print(age)

show(age=10,name="this")

def test(*t):
    print(t)
test("one","two",1)
num1=pp.add(3,4)

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(self.name)


myDog=Dog("ane",200)
print(myDog.age)
with open("c://a.txt") as file_obect:
    contents=file_obect.read()
    print(contents)
with open("c://a.txt") as file_obect:
    lines=file_obect.readlines()

with open("c://a.txt") as file_obect:
    for line in file_obect:
        print(line.strip())

with open("d://a2.txt",'w') as file_obect:
    file_obect.write("i love programming")

try:
    print(5/0)
except :
    print("exception")
list_one=list(range(1,40))


with open("d://json1.json",'w') as file_obect:
    json.dump(list_one,file_obect)
with open("d://json1.json",'r') as file_obect:
    list_two=json.load(file_obect)
    print(list_two)