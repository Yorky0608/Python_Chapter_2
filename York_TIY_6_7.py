person_1 = {"first_name" : "Denver", "last_name" : "Zararte-Garcia", "city" : "Fort Wayne", "foods" : "anything"}
person_2 = {"first_name" : "Jedidiah", "last_name" : "Sian", "city" : "Fort Wayne", "foods" : "Asian and Mexiacn only"}
person_3 = {"first_name" : "Sam", "last_name" : "Paris", "city" : "Fort Wayne", "foods" : "Asian, American, Mexican"}

list = [person_1, person_2, person_3]

for person in list:
    for key, value in person.items():
        if key == 'first_name':
            print(f"\nThere first name is {value}.")
        elif key == 'last_name':
            print(f"\nThere last name is {value}.")
        elif key == 'city':
            print(f"\nThey live in {value}.")
        elif key == 'foods':
            print(f"\nTheir favorite foods are: {value}.")