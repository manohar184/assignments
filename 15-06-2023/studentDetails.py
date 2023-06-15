d={"don":85,"sunny":90,"sai":95,"shannu":87}
name= input("Enter the name : ")
if name in d.keys():
    print(name, d[name])
else:
    print("No records found")    