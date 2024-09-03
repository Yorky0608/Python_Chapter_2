invites = ["Notch", "Jeb_", "Babe Ruth"]
for i in invites:
    print(f"Dear {i}, you have been invited to dinner by Yorky.")
print(f"{invites[1]} was not able to come.")
invites.pop(1)
invites.append("Joey Votto")
for i in invites:
    print(f"Dear {i}, you have been invited to dinner by Yorky.")
print(f"Everyone, I have a new table, and I will be inviting more people.")
invites.insert(0,"Jay Bruce")
invites.insert(2,"Suarez")
invites.insert(6,"JJ")
for i in invites:
    print(f"Dear {i}, you have been invited to dinner by Yorky.")
print(f"Number of people coming: {len(invites)}")