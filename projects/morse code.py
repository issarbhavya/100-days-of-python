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
    
    #encoded_str length is increased by 2 spaces to detect that a word has ended at the end as well.
    encoded_str=encoded_str + "  "
    
    letter_to_decode=""
    decoded_letter=""
    decoded_word=""
    final=""
    for i in range(0,len(encoded_str)):
        
        if(encoded_str[i]==" " and encoded_str[i-1]==" "):
            final += decoded_word+ " " 
            decoded_word=""
            continue
               
        if(encoded_str[i]!=" "):
            letter_to_decode += encoded_str[i]
            
        else:
            index_of_item=item_list.index(letter_to_decode)
            decoded_letter=key_list[index_of_item]
            letter_to_decode=""
            decoded_word += decoded_letter
            decoded_letter=""
            
    print(f"\ndecode string is : {final}\n")
    
            
task=int(input("Enter 1 to encrypt a string \n\nEnter 2 to decrypt a string\n\n"))
print("\n\n")
if(task==1):
    encryption()
elif (task==2):
    string_=input("enter the encrypted string which is to be decrypted : ")
    decryption(string_)
else:
    print("UNDEFINED TASK ASSIGNED")          