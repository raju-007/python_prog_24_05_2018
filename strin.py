k="raju@google.com"
j=""
p=0
for i in k:
    if i == '@':
        break
    else:
        j+=i
print(j)
print("%%%%%%%%%%%%%%%%%")
y="food@google.com"
x=""
for h in y:
    if h == '.':
        break
    else:
        x+=h
        if h=="@":
            x=""

print(x)
u="food@google.com"
y=""
for r in u:
    if r==".":
        y=""
    else:
        y+=r
print(y)