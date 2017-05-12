import sys
import csv
import _collections
import math

#inputcsv = str(sys.argv[1])
#data = csv.reader(open(inputcsv,"rb"))

def ReadCSVfile(filename):
    line = csv.reader(open(filename,"rb"))
    dataset = list(line)
    for count in range(len(dataset)):
        dataset[count]=[(x) for x in dataset[count]]
    return dataset

#filename = "mushroom_data.csv"
filename = str(sys.argv[1])
countp=0
counte=0
mydata = ReadCSVfile(filename)
for i in range(len(mydata)):
    if mydata[i][0]== "p":
        countp+=1
    if mydata[i][0]== "e":
        counte+=1
#print countp
#print counte
##print '%.3f' % (countp // len(mydata))
#print '%.3f' % (countp / (len(mydata)*1.0))
openfile = str(sys.argv[2])
file=open(openfile,"w")
file.write("%.3f  %.3f\n" % (countp / (len(mydata)*1.0), 1 - countp / (len(mydata)*1.0)))
e1 =[]
e1.append("b")
e1.append("c")
e1.append("x")
e1.append("f")
e1.append("k")
e1.append("s")

e2 = []
e2.append("f")
e2.append("g")
e2.append("y")
e2.append("s")

e3 = []
e3.append("n")
e3.append("b")
e3.append("c")
e3.append("g")
e3.append("r")
e3.append("p")
e3.append("u")
e3.append("e")
e3.append("w")
e3.append("y")

e4 = []
e4.append("t")
e4.append("f")

e5 = []
e5.append("a")
e5.append("l")
e5.append("c")
e5.append("y")
e5.append("f")
e5.append("m")
e5.append("n")
e5.append("p")
e5.append("s")

e6 = []
e6.append("a")
e6.append("d")
e6.append("f")
e6.append("n")

e7 = []
e7.append("c")
e7.append("w")
e7.append("d")

e8 = []
e8.append("b")
e8.append("n")

e9 = []
e9.append("k")
e9.append("n")
e9.append("b")
e9.append("h")
e9.append("g")
e9.append("r")
e9.append("o")
e9.append("p")
e9.append("u")
e9.append("e")
e9.append("w")
e9.append("y")

e10 = []
e10.append("e")
e10.append("t")

e11 = []
e11.append("b")
e11.append("c")
e11.append("u")
e11.append("e")
e11.append("z")
e11.append("r")
e11.append("?")

e12 = []
e12.append("f")
e12.append("y")
e12.append("k")
e12.append("s")

e13 = []
e13.append("f")
e13.append("y")
e13.append("k")
e13.append("s")

e14 = []
e14.append("n")
e14.append("b")
e14.append("c")
e14.append("g")
e14.append("o")
e14.append("p")
e14.append("e")
e14.append("w")
e14.append("y")

e15 = []
e15.append("n")
e15.append("b")
e15.append("c")
e15.append("g")
e15.append("o")
e15.append("p")
e15.append("e")
e15.append("w")
e15.append("y")

e16 = []
e16.append("p")
e16.append("u")

e17 = []
e17.append("n")
e17.append("o")
e17.append("w")
e17.append("y")

e18 = []
e18.append("n")
e18.append("o")
e18.append("t")

e19 = []
e19.append("c")
e19.append("e")
e19.append("f")
e19.append("l")
e19.append("n")
e19.append("p")
e19.append("s")
e19.append("z")

e20 = []
e20.append("k")
e20.append("n")
e20.append("b")
e20.append("h")
e20.append("r")
e20.append("o")
e20.append("u")
e20.append("w")
e20.append("y")

e21 = []
e21.append("a")
e21.append("c")
e21.append("n")
e21.append("s")
e21.append("v")
e21.append("y")


e22 = []
e22.append("g")
e22.append("l")
e22.append("m")
e22.append("p")
e22.append("u")
e22.append("w")
e22.append("d")


# Element 1
for k in range(len(e1)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][1] == e1[k] and mydata[i][0] == "p":
            countelementp+=1;
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e1)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][1] == e1[k] and mydata[i][0] == "e":
            countelemente+=1;
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")

# Element 2
for k in range(len(e2)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][2] == e2[k] and mydata[i][0] == "p":
            countelementp+=1;
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e2)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][2] == e2[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 3
for k in range(len(e3)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][3] == e3[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e3)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][3] == e3[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 4
for k in range(len(e4)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][4] == e4[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e4)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][4] == e4[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0))) 
file.write("\n")
# Element 5
for k in range(len(e5)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][5] == e5[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e5)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][5] == e5[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 6
for k in range(len(e6)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][6] == e6[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e6)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][6] == e6[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")    
# Element 7
for k in range(len(e7)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][7] == e7[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e7)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][7] == e7[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")    
# Element 8
for k in range(len(e8)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][8] == e8[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e8)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][8] == e8[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 9
for k in range(len(e9)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][9] == e9[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e9)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][9] == e9[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 10
for k in range(len(e10)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][10] == e10[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e10)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][10] == e10[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 11
for k in range(len(e11)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][11] == e11[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e11)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][11] == e11[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 12
for k in range(len(e12)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][12] == e12[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e12)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][12] == e12[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 13
for k in range(len(e13)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][13] == e13[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e13)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][13] == e13[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 14
for k in range(len(e14)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][14] == e14[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e14)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][14] == e14[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 15
for k in range(len(e15)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][15] == e15[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e15)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][15] == e15[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 16
for k in range(len(e16)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][16] == e16[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e16)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][16] == e16[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 17
for k in range(len(e17)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][17] == e17[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e17)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][17] == e17[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 18
for k in range(len(e18)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][18] == e18[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e18)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][18] == e18[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 19
for k in range(len(e19)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][19] == e19[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e19)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][19] == e19[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 20
for k in range(len(e20)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][20] == e20[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e20)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][20] == e20[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 21
for k in range(len(e21)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][21] == e21[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e21)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][21] == e21[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))
file.write("\n")
# Element 22
for k in range(len(e22)):
    countelementp = 0
    for i in range(len(mydata)):
        if mydata[i][22] == e22[k] and mydata[i][0] == "p":
            countelementp+=1;
    
    file.write("%.3f " % (countelementp/(countp*1.0)))
file.write("\n")

for k in range(len(e22)):
    countelemente = 0
    for i in range(len(mydata)):
        if mydata[i][22] == e22[k] and mydata[i][0] == "e":
            countelemente+=1;
    
    file.write("%.3f " % (countelemente/(counte*1.0)))

file.close()