'''with open("ex.txt", "w") as file:
    file.write("hello world")'''
   
with open("ex.txt", "w") as file:
    file.write("hello world\n")
    file.write("hello world\n")
    file.write("hello world\n")


with open("ex.txt", "r") as file:
    content = file.read()
    print(content)

