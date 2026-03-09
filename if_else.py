# # write a program to check of given char is  uppercase
# n=input("enter the character:")
# if ord(n)>=65 and ord(n)<=90:
#     print("character is uppercase")

# if 'A' <=n <= 'Z':
#     print("Character is uppercase")

#write a program to check length of the string is odd

# n=input("enter is string")
# if len(n)%2!=0:
#     print(n,"string is odd")
#     print(f"{n} string is odd")#formulated string 


#write a program to check if given value is collection a data type or not

# n=eval(input("enter the number"))
# if type(n) in (list ,tuple , set, dict):
#     print(n,"the value in collection datatype")


# else:
#     print(n,"the value of collection not indatatype")

#write a program to  check if len of the string is even or odd  if 
# it is odd  print its middle value or else print the last value.

# n=input("enter is string")
# if len(n)%2==0:
#     print(n,"string is even then last value is",n[-1])

# else:
#     index=len(n)//2
#     print(f"{n} string is odd then middle number is",n[index])#formulated string 

#wp is immuutable or not
#wap is pal@Zindrome or not

#if n==n[::-1]:

#wp to check the given dtaa sis special characters or not

# a=(input("Enter the  data"))
# if (a>='0'and a<='9') or(a>='a' and a<='z') or  (a>='A' and a<='Z') :
#     print(" not special characters")
# else:
#     print("special") 

#wap wheteher datatype is homogenous or not

# n=eval(input("eneter the data "))
# if type(n[0])==(n[1]):
#     print("homogenous")

# else:
#     print("no homgenous")
   
#wap to check whether num is divisble by 6 and 9 if divisible then write cube of itt

#wap to check if a given number is single diigit ,or double dogit or three digit or greate then that

# n=(abs(int(input("enter the number"))))# abs -convert negative to [positives and positive remain same]
# if 0<=n<=9:  #n>= 0 and n<=9
#     print("single value",n)

# elif 10<=n<=99: # #n>= 10 and n<=99
#     print("double digit",n)

# elif 100<=n<=999: # #n>= 100 and n<=999
#     print("three digit",n)

# else:
#     print("greter with all",n)

#wap to check upper case or lower case or digits or special character 

# n=(input("enter the value"))
# if 'A'<= n <='Z':
#     print("Upper case")

# elif 'a'<= n <='z':
#     print("lower case")
    
# elif '0'<=n <='9':
#     print("digiits")
# else:
#     print("special characters")

# CONSIDER A CAHRACTER INO]PUT IF THE CHARACTER IS UPPERCASE  CONVERT IN TO LOWER CAS , 
# IF THE CHARQACTER IS LOWER CASE CONVERT IN TO UPPER CASEE
# IF IT IS DIGITS PRINT THE  REMAINDER WHEN DIVIDED BY 3 AND LASTLY IF IT IS SPECIASL CHARACTER 
# PRINT ITS ASCII VALUE

# n=(input("ehter the data"))
# if 65<=ord(n)<=90: #!'A' <=n<= 'Z'
#     b=chr(ord(n)+32)
#     print("uppercase in to lowercse",b)
    
# elif 97<=ord(n)<=122:  #!'a' <=n<= 'z'
#     c=chr(ord(n)-32)
#     print("uppercase ",c)

# elif '0'<=n<='9':
#     print("digit")
#     d=int(n)%3     #!type casting
#     print("remainder",d)
# else :
#     s=ord(n)
#     print("Special character",s)

 #wap to find the geraeatest of three number to be using elif

# a=int(input("eneter the numbers"))

# b=int(input("eneter the numbers"))

# c=int(input("eneter the numbers"))
# if a>=b and a>=c:
#     print("a is greater1",a)
# elif b>=a and b>=c:
#     print("b is greater2")
# else:
#     print("c is greater3")

# smallest of 4 nubers
#waqp to print fizz if rthe given number is divisible by 3,
# print buzz if the give number is divisble by 5 and 
# print fizz buzz if the number ius dividble both 3 and 5.


n=int(input("Entre the number:"))

if n%3==0 and n%5==0:
    print("fizz and buzz",n)
elif n%5==0:
    print("buzz",n)

elif n%3==0:
    print("fizz",n)n=int(input("Entre the number:"))

if n%3==0 and n%5==0:
    print("fizz and buzz",n)
elif n%5==0:
    print("buzz",n)

elif n%3==0:
    print("fizz",n)

