# 1 can can cover 5sq unit area so program is based on that only
import math
leng=int(input("enter length of the wall in meters : "))
width=int(input("enter width of wall in meters : 7"))
print(f"cans required : {math.ceil((leng*width)/5)}")
