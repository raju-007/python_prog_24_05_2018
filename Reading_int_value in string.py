import re
t=[]
r="hi 1 2 hello 9 6"
print (re.findall("\d",r))
print("&&&&&&&&&&&&&&")
print(r)
u=""
t.append(r.split(" "))
print(t)
print("%%%%%%%%%%%%%%%%%%%%%")
string="hi123 54 hello 8347 darling143 67"
ki=[x for x in string.split() if x.isdigit()== False]
print(ki)
print("^^^^^^^^^^^^^^^^^^^^^^^")
strings = "h3110 23 cat 444.4 rabbit 11 2 dog"
ui=[int(x) for x in strings.split() if x.isdigit()]
print(ui)