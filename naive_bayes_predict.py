#with open(sys.argv[1]) as f:
#	tmp = f.readlines()
#	f.close()

with open("model.txt") as f:
	tmp = f.readlines()
	f.close()

float_num = []
string = ""
for i in range(len(tmp[0])):
	if (tmp[0][i] != " " and tmp[0][i] != "\n"):
		string = string + tmp[0][i]
	else:
		num = float(string)
		float_num.append(num)
		string = ""
p = float_num[0]
e = float_num[1]
data.append(float_num);
for i in range(1, len(tmp), 2):
	t = []
	float_num = []
	number = ""
	for j in range(len(tmp[i])):
		if (tmp[i][j] == "\n"):
			break		
		if (tmp[i][j] != " " and tmp[i][j] != "\n"):
			number = number + tmp[i][j]
		else:
			num = float(number)
			float_num.append(num)
			number = ""
	t.append(float_num)
		
	float_num = []
	number = ""
	for j in range(len(tmp[i + 1])):
		if (tmp[i+1][j] == "\n"):
			break
		if (tmp[i + 1][j] != " " and tmp[i + 1][j] != "\n"):
			number = number + tmp[i + 1][j]
		else:
			num = float(number)
			float_num.append(num)
			number = ""
	t.append(float_num)
	data.append(t)

def ReadCSVfile(filename):
    line = csv.reader(open(filename,"rb"))
    dataset = list(line)
    for count in range(len(dataset)):
        dataset[count]=[(x) for x in dataset[count]]
    return dataset
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

filename = "test.csv"
mydata=ReadCSVfile(filename)
file=open("153057.txt","w")
for i in range(len(mydata)):
    file.write(mydata[i][0])
    j = 1
    stap=1
    stae=1
    for j in range(len(mydata[i])):
        valp = 1;
        vale = 1;
        if mydata[i][0] == "p":
            m = 0
            while (data[i][0][m] != mydata[0][j]):
                m+=1            
            valp = data[i][0][m]
        if mydata[i][0] == "e":
            m = 0
            while (data[i][1][m] != mydata[0][j]):
                m+=1            
            vale = data[i][1][m]
    stap*=valp
    stae*=vale
    if mydata[i][0] == "p":
        stap *= data[0][0]
        if stap >= 0.5:
            file.write(" p\n")
        else:
            file.write(" e\n")
    if mydata[i][0] == "e":
        stae *= data[0][1]
        if stae >= 0.5:
            file.write(" e\n")
        else:
            file.write(" p\n")

