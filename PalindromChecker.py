string = input("Enter the text here:")
# My First Version
#length = len(string) - 1
# for index in range(len(string)):
#     if string[index] != string[length]:
#         print("Not palindrom!!")
#         break
#     else:
#         length = length - 1
#         if length > index:
#             print("paliindrom")
#             break

# Second version Adapted from web
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


print(isPalindrome(string))
