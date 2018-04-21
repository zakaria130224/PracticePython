name=["zakaria","umesh","Boss"] #list
person={"name":'zakaria', "age":26, "Education":'BSC'} #dictionary

persons=[person,person]

print(persons[0]["age"])

print(person["name"])

for item in name:
    print(item)


run= True
count=0
while run:
    if count==len(name):
        run=False
    else:
        print(name[count])
        count += 1
