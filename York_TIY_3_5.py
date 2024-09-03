invites = ["Notch", "Jeb_", "Babe Ruth"]
for i in invites:
    print(f"Dear {i}, you have been invited to dinner by Yorky.")
print(f"{invites[1]} was not able to come.")
invites.pop(1)
invites.append("Joey Votto")
for i in invites:
    print(f"Dear {i}, you have been invited to dinner by Yorky.")