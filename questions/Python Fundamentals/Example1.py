def acceptInt(dimension_name):
    value = int(input("Please enter "+dimension_name+" : "))
    return value

x = acceptInt("1")
y = acceptInt("2")
z = acceptInt("3")




print("Original numbers: ",x,y,z)

x,y,z = y,z,x

print("After Swapping: ",x,y,z)
