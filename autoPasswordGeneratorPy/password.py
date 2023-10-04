import random 

lower = 'abcdefghijklmnopqrstuvwxyz' #lower case alphabates
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Uppercase alphabates
num = '0123456789' #numbers
sym = '(){}[]-_@#' #symbols

all = lower + upper + num + sym #concatinate all of these above
length = 10 #password length
password = "".join(random.sample(all, length)) #join randomly and created as a password
print("Your generated password: ", password) #print it out