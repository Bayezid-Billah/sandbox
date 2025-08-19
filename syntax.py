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
