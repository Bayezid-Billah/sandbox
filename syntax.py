import sys



print("Hello world")
print(11, 2, 12)
print("A", "yo", "c", sep = "; ")
print("Line without newline", end="")
print("First line\nSecond line")
name = "Homie"
age = 21
print(f"wassup {name}, heard you are {age} now.")
print("wassup {}, heard you are {} now.".format("homie", 21))
print("wassup %s, heard you are %d now." %(name,age))

with open("output.txt", "w") as f:
    print("This goes to a file", file=f)
print("This goes to stdout", file=sys.stdout)
print("This goes to stdrr", file=sys.stderr)
hello = "hello"
world = "World"
print(hello+" "+world)
a,b = 3,2
print(a,b)
a,b = b,a
print(a,b)

mylist = []
mylist.append(2)
mylist.append(10)
mylist.append(a)
mylist.append(b)
mylist.append("Y")
print(mylist[0])
for x in mylist:
    print(x)

calculate = 2+a/(5)
print(calculate)
print("\n")
calculate = calculate * 10
print(calculate)
print(12**2)
print(17%5)
mylist2 = [1,5,6,7,8]
mylist3 = mylist + mylist2
print(mylist3)

print(len(name))
print(name.count("m"))
print(name[1:3])

print(a == 2)
print(a ==3)
if a==2 and b==3:
    print("A = 2 and B = 3")
else: print("A is not 2")
if name in ["Homie", "wassup"]:
    print("wassup homie")
for x in range(5):
    print(x)
print("-------------")
for x in range(3,6):
    print(x)
print("-------------")
for x in range(3,8,2):
    print(x)
print("-------------")
count = 0
while count <5:
    print(count)
    count +=1
print("-------------")

def my_function():
    print("Wassup function")
def myfunc_arguments(name,age):
    print("wassup %s, how you doing"%(name))
myfunc_arguments("KIM", 14)
my_function()

class MyClass:
    variable = "Blah"

    def function(self):
        print("This is from inside the class")

myobjetx = MyClass()
print(myobjetx.variable)
myobjetx.function()

phonebook = {}
phonebook["yeah"] = 102930
phonebook["no"] = 12312907
phonebook["maybe"] = 123123
print(phonebook)
for name, number in phonebook.items():
    print("Phone number of %s is %d" %(name,number))

print("input a string: ")
string = input()
