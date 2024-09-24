def celisius_to_fahrenheit(celisius):
    return (celisius*9/5)+32
def fahrenheit_to_celisius(fahrenheit):
    return(fahrenheit-32)*5/9
print("temperature conversions")
print("1.celisius to fahrenheit")
print("2. fahrenheit to celisius")
choice=int(input("enter your choice(1/2):"))
if choice==1:
    celisius=float(input("enter temperature in celisius:"))
    fahrenheit=celisius_to_fahrenheit(celisius)
    print(f"{celisius}'c is equal to {fahrenheit}of")
elif choice==2:
    fahrenheit=float(input(" enter temperature in fahrenheit:"))
    celisius=fahrenheit_to_celisius(fahrenheit)
    print(f"{fahrenheit} is equal to {celisius}of")
else:
    print("invalid choice")
    
