age = input("Enter your age: ")
print(type(age))
#cast so we can switch from str into int
age = int(age)
print(type(age))
print ("You have entered: ",age)
x = age

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
    print("boom!")