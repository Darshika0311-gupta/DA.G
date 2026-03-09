#wap ti praint the last value of  a list if it is palindrom estart with vowel.

n=eval(input("Enter value:"))
if type(n)==list:
    if type(n[-1]) == str:
        value=n[-1]
        if value[0] in 'AEIOUaeiou':
            if value == value[::-1]:
                print(value)
else:
    print("it is not a list")
    else:
    print("last value is not str")
        else:
    print("code does not strt with str")
else:
print("str is not palindrome")





