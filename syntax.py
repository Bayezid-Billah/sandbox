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
