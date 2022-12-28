
print("find where is treasure")
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


coloumn=int(position[0])
row=int(position[1])

if row ==1:
    if coloumn == 1:
        row1[0] ="x "
        

    elif coloumn == 2:
        map[0][1]="x "
    
    elif coloumn == 3:
        map[0][2]="x "

if row ==2:
    if coloumn == 1:
        map[1][0]="x "

    elif coloumn == 2:
        map[1][1]="x " 
    
    elif coloumn == 3:
        map[1][2]="x "
if row ==3:
    if coloumn == 1:
        map[2][0]="x "

    elif coloumn == 2:
        map[2][1]="x "
    
    elif coloumn == 3:
        map[2][2]="x "



print(f"{row1}\n{row2}\n{row3}")
