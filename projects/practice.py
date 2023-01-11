MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ',':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-', '^':'^'}
key_list=[]
item_list=[]
for i in MORSE_CODE_DICT:
    key_list.append(i)
    item_list.append(MORSE_CODE_DICT[i])

def encryption():
    encrypted=" "
    lst=[]
    str1=input("string to be coded : ")
    str1=str1.upper()
    for i in str1:
        lst.append(i)
    for i in lst:
        if(i!=" "):
            encrypted=encrypted + MORSE_CODE_DICT[i]+" "
        else:
            encrypted=encrypted + "   "  
            
    print(encrypted) 
    
def decryption(encoded_str):
    encoded_str=encoded_str+" "
    letter_to_decode=""
    decoded_letter=""
    decoded_word=""
    final=""
    x=0
    encoded_str=encoded_str+" "
    for i in range(0,len(encoded_str)):
        if (x==2):
            x=0
            final += decoded_word + "  "
            decoded_word=""
            continue
        if(encoded_str [i]!=" "):
            letter_to_decode=letter_to_decode + encoded_str[i]
        if(encoded_str[i]==" "):
            if(encoded_str[i+1]==" "):
                x=2 
            index_=item_list.index(letter_to_decode)
            decoded_letter=key_list[index_]
            decoded_word += decoded_letter
            letter_to_decode=""
            decoded_letter=""
    print(f"decode string is : {final}")                
            
    
task=int(input("Enter 1 to encrypt a string \n\nEnter 2 to decrypt a string\n\n"))
print("\n\n")
if(task==1):
    encryption()
elif (task==2):
    string_=input("enter the encrypted string which is to be decrypted : ")
    decryption(string_)
else:
    print("UNDEFINED TASK ASSIGNED")
    
                
            