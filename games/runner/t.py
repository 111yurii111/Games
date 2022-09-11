import os

name = input("Name of file: ")

a = (str(name) + ".py")

t = ("touch " + str(name) + ".py")
o = ("open " + str(name) + ".py")
os.system(str(t))
os.system(str(o))
