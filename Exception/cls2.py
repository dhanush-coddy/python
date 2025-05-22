# Custom exception class
class cn(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

try:
    passw = input("Enter your password: ")
    if len(passw) < 6:
        raise cn("❌ Weak password: must be at least 6 characters.")
    else:
        print("✅ Password accepted.")
except cn as e:
    print("Custom Exception:", e) 
