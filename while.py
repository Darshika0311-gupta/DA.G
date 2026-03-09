

# # #!wap to print python fror 10 times without using for and while loop

# # # i=0
# # # while i<10:
# # #     #print('before:i)
# # #     print("Python")
# # #     i=i+1
# # #     #print('after:'i)
# # # print("hii")
# # # print(i)

# # #!wap to print even numbers up to n=20

# # # a=int(input("Enter the number:"))
# # # n=0
# # # while  n<a:
# # #     print(n)
# # #     n=n+2 

# # # n=10
# # # i=2
# # # while i<+n:
# # #     if i%2==0:
# # #         print(i)

# # #     i=i+1

# # #! write a progream to print chharacter at present in the odd string


# # # a="python" 
# # # a="python"
# # # i=1
# # # while i<len(a)
# # #         print(a[i])
# # #         i=i+2
# # # 
# # #!write a to  extract the only uppercase from the string

# # n='hoLiDay'
# # i=0
# # out=[]
# # t=len(n)
# # while i < t:
# #     if 'A' <=n[i]<='Z':
# #          out.append(n[i])
# #     i+=1
# # print(out)
    
# #! write a program to reverse the string using while loop

# # n='hoLiDay'
# # i=0
# # out=''
# # t=len(n)
# # while i < t:
   
# #           out=n[i]+out
# #           i+=1
# # print(out)   


# #!new code
# # n='PyTHon@15'
# # i=0
# # upper=[]
# # lower=[]
# # special=[]
# # digit=[]

# # while i<len(n):
# #     if 'A'<=n[i]<='Z':
# #         upper.append(n[i])
   
# #     elif 'a'<=n[i]<='z':
# #          lower.append(n[i])
# #     elif n[i] in '0,1,2,3,4,5,6,7,8,9':
# #         digit.append(n[i])
   
# #     else:
# #         special.append(n[i])
# #     i +=1
# # print(upper)
# # print(lower)
# # print(digit)
# # print(special)


# #!write a program tpo replace space with underscore in the string
# # n='Hii Python here'
# # i=0
# # out=''
# # while i <len(n):
# #     if n[i]==' ':
# #         out=out+'_'
# #     else:
# #         out=out+n[i]
# #     i=i+1
# # print(out)

# #!wrie a proogram to count number of times  a particular char is repeted in the str
# # n=input("enter the string: ")
# # p=input("enter the character: ")
# # i=0
# # c=0
# # while i < len(n):
# #     if n[i] == p:
# #         c+=1

# #     i=i+1
# # print(c)
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # WAP to convert lowercase characters into uppercase characters and uppercase characters into lowercase characters without using in-built function
# # n=input("Enter the string")
# # i=0
# # ans=''
# # while i < len(n):
# #     if 'A'<n[i]<'Z':
# #       ans=ans+chr(ord(n[i])+32)
# #     else:
# #        ans=ans+chr(ord(n[i])-32)
# #     i=i+1
# # print(ans)
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# #wap to convert a string in to title without inbuilt function

# # n=input("ENTER the string")
# # i=0
# # out=''
# # while i < len(n):
# #     if i == 0:
# #         if 'a'<=n[i]<='z':
# #             out=chr(ord(n[i])-32)
# #         else:
# #             out=out+n[i]
       
# #     elif n[i-1]==' ':
# #         if 'a'<=n[i]<='z':
# #             out=out+chr(ord(n[i])-32)
# #         else:
# #             out=out+n[i]
     
# #     else:
# #         if 'A'<=n[i]<='Z':
# #             out=out+chr(ord(n[i])+32)
# #         else:
# #              out=out+n[i]

# #     i=i+1
# # print(out)


#!write a program to reverse the number usinnng while loop and without type casting
# n=145
# print("number",n%10) #!EXTRACT THE VALUE
# print("new n",n//10) #!REMOVE THE VALUE

# n=14
# print("number",n%10)
# print("new n",n//10)

# n=1
# print("number",n%10)
# print("new n",n//10)

# n=int(input("Enter the number:"))
# out=0

# while n>0:
#     ld=n%10
#     out=out*10+ld
#     n=n//10
# print(out)


