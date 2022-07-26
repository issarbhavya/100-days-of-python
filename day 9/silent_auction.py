
decision="yes"
auction={}
while(decision=="yes"):
    name=input("your name : ")
    bid=int(input("your bid : $"))
    auction[name]=bid
    decision=input("if any more bids left then type \"yes\"  : ")
   
    
highest_bid=0
for bidder in auction:
    if (auction[bidder]>highest_bid):
        highest_bid=auction[bidder]
        highest_bidder=bidder
print(f"highest bid is of {highest_bidder} of amount ${highest_bid}")
    

