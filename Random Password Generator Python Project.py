import random
import string

          ####### Random Password Generator #####


print("Welcome ! to the Random Password Generator ")
print()

name=input("Enter your name = ")
print()
print(name,"! here you go !!!")
print()

alphabet=[ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S", "T","U","V","W","X","Y" ]

number=["1","2","3","4","5","6","7","8","9","0"]

punctuation=["@","#","$","%","&","*",">","!"]



pswrd=[]


for i in range(0,3):
    
    a=random.choice(alphabet)
    pswrd.append(a)

    
    n=random.choice(number)
    pswrd.append(n)

    
    p=random.choice(punctuation)
    pswrd.append(p)

    
    l=random.choice(alphabet)
    La=l.lower()
    pswrd.append(La)


print("Random password in list is : ")
print(pswrd)
print()

#### Concetination by loop and string variable ####

x=""
for y in pswrd:
    x+=y

print("Password =",x)

 