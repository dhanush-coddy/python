file = open(r"goku.jpg", "wb") 
file.write(b"fjhfjhf") 
file.write(bytes([1]))
file.close()



file2 = open(r"goku.jpg", "rb") 
 
print(file2.read())              
file2.close()


