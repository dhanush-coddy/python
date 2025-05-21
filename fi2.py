# Reading from the file (optional)
file = open("ex.txt", "r")
print(file.read())
file.close()

# Writing to the file
file = open(r"C:\Users\Ethnotech\Desktop\python\ex.txt", "w")
file.write("\n hello")

file.writelines([
    "hello\n",
    "sjdksajdk\n",
    "saldalskmdklasd\n",
    "dwjkjsndn"
])
file.close()

# Reading again to see changes
file = open(r"C:\Users\Ethnotech\Desktop\python\ex.txt", "r")
print(file.read())
file.close()
