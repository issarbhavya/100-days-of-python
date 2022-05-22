name1=input("enter your name ")
name2=input("enter partner's name ")
name = name1+name2
len_both_name=len(name1)+len(name2)


i=0
c1=0
c2=0
while(i<len_both_name):
    match name[i]:
        case "t":
            c1 += 1
        case "r":
            c1 += 1
        case "u":
            c1 += 1
        case "e":
            c1 += 1
        
        
    match name[i]:
        case "l":
            c2 += 1
        case "o":
            c2 += 1
        case "v":
            c2 += 1
        case "e":
            c2 += 1
        
    i+=1

print(f"love calculator score is {c1}{c2} %")


