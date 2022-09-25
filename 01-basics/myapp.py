name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
iq = int(input("IQ: "))
sub = input("Your favourite subject?: ")

print("Hello "+name)
print("You are "+str(age)+" years old")
if(height < 160):
    print("Only "+str(height)+"cm tall")
else:
    print("You are " + str(height) + "cm tall")

if(iq < 80):
    print(""+str(iq)+"iq really ?")
else:
    print("Your iq:")
if(sub == "math" ):
    print("you are weird for choosing "+str(sub)+" ")
else:
    print("favourite subject: "+str(sub)+"")

