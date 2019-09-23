className = input("Input a class Name: ")
argsList = []
print("Input [type] [argName] and end up with 'CREATE'")
while True:
    ipt = input()
    if ipt.upper() == "CREATE":
        break
    feature,fname = ipt.split()
    feature = feature.upper()
    if feature=="S":
        argsList.append(("String",fname))
    elif feature=="i":
        argsList.append(("int",fname))
    elif feature == "I":
        argsList.append(("Integer", fname))
    elif feature=="D":
        argsList.append(("Date",fname))
    elif feature=="F":
        argsList.append(("File",fname))
    else:
        argsList.append((feature,fname))

ans = "public class "+className+"{\n"
for x in argsList:
    ans +="\tprivate "+x[0]+" "+x[1]+";\n"
ans += "\tpublic "+className+"(){}\n"
ans += "\tpublic "+className+"("+",".join([ x[0]+" _"+x[1] for x in argsList ]) + "){\n"+"\n".join(["\t\t"+x[1]+" = _"+x[1]+";" for x in argsList ])
ans += "\n\t}\n"

for x in argsList:
    firstUpper = x[1][0:1].upper()+x[1][1:]
    ans+="\tpublic void "+"set"+firstUpper+"("+x[0]+" _"+x[1]+"){\n\t\t"+x[1]+"="+"_"+x[1]+";\n\t}\n"
    ans+="\tpublic "+x[0]+" get"+firstUpper+"(){\n\t\treturn "+x[1]+";\n\t}\n"

ans+="}\n"
print(ans)
