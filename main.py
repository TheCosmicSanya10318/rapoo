from replit import db
db["admin_id"] = "1024"
ask = input("Enter your ID: ")
lol = db["admin_id"]
keys = db.keys()
matches = db.prefix("admin_id")
print(keys)
print(matches)
