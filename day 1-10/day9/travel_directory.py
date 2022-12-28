travel_note=[]

no_of_cont=int(input("enter no. of countries visited : "))
for i in range(0,no_of_cont):
    countries_info={}
    countries_info["name"]=input(f"enter name of country no.{i+1}:")
    no_of_cities=int(input("enter no. of cities visited in the country: "))
    cities=[]
    for j in range (0,no_of_cities):
        cities.append(input(f"enter city no. {j+1}: "))
    countries_info["cities info: "]=cities
    countries_info["no_of_visits"] =int(input("enter no. of times visited: "))
    travel_note.append(countries_info)

def add_country():
    n=int(input("no. of countries to be added: "))
    for i in range (0,n):
        countries_info["name"]=input(f"enter name of country no.{i+1}: ")
        no_of_cities=int(input("enter no. of cities visited in the country: "))
        cities=[]
        for j in range (0,no_of_cities):
            cities.append(input(f"enter city no. {j+1}: "))
        countries_info["cities info: "]=cities
        countries_info["no_of_visits"] =int(input("enter no. of times visited: "))
        travel_note.append(countries_info)

print("\n\n")
print(travel_note,"\n\n")

decision=input("press y to enter more countries \n Else press any other key")
if decision=="y":
    add_country()
    print(travel_note)
        
    


    
    
    