name = input()

if len(name) < 3:
    print("Name Must be atleast 3 Characters Long!")

elif len(name) > 50:
    print("Name should be less then 50 Characters.")

else:
     print("name looks good")