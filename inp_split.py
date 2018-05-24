values=[]
for i in range(3):
    values.append(input())

#t=tuple(l)
print("#########")
print (values)
print("-------------")
print ()
print(len(values))
print("---------seq if num----------")
items=[x for x in input().split(',')]
print(items)
print("%%%%%%%%%")
s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))
print(words)
print("^^^^^^^^^^^^^^^^^^")
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (numbers)

