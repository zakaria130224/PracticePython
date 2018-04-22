string=input("Enter the text here:")
length=len(string)-1
for index in range(len(string)):
    if string[index] != string[length]:
        print("Not palindrom!!")
        break
    else:
        length=length-1
        if length>index:
            print("paliindrom")
            break