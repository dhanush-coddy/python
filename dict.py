d1={"name":"jhon","age":20}
print(d1)
print(d1["name"])
print(d1.get("name"))
d1["email"]="jhom@gmail.com"
print(d1)
d2 = {"name": "jhon", "age": 20, "city": "New York", "email": "jhon@example.com"}
print(d2.keys())
print(d2.values())


del d2["age"]


d2.pop("city")


d2.clear()

print(d2)
