import random
import string
num_of_letters=int(input("enter no.letters you want in your password \n"))
num_of_symbols=int(input("enter no. of symbols you want in your password \n"))
num_of_numbers=int(input("amount of no. you want in the password \n"))
str_lst=[]
num_lst=[]
sym_lst=["!","@","#","$","&","*"]
symbol_lst=[]
password=""
for i in range (0,num_of_letters):
    str_lst.append((random.choice(string.ascii_letters)))
for i in range (0,num_of_symbols):
    num_lst.append(str(random.randint(0,9)))
for i in range(0,num_of_symbols):
    symbol_lst.append(random.choice(sym_lst))
    
final_lst=str_lst+num_lst+symbol_lst

for i in range (0,len(final_lst)):
    f=random.choice(final_lst)
    password += f
    final_lst.remove(f)
print(password) 