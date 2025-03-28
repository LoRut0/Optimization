from myfunction import *

f = open("function.csv", "w")
f.write("x,y\n")
for i in range(a * 10**6, b * 10**6):
    x = i/10**6
    string = str(x) + "," + str(function(x)) + "\n"
    f.write(string)
f.close()
