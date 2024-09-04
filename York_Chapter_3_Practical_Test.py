People = [["Michael Buchanan", "Hersey"], ["Seth Johns", "Gummy Bears"], ["Yaseen Kedio", "Snickers"], ["Trace Likens", "Candy Corn"], ["Miguel Moreno", "Resses"], ["Josue Roque", "Twix"], ["Julian-Jordan Starks", "Sour Patch Kids"]]
print(People)
for i in range(len(People)):
    for b in range(1):
        print(People[i][b]+ ":", People[i][b+1])
People.sort()
for i in range(len(People)):
    for b in range(1):
        print(People[i][b]+ ":", People[i][b+1])
        print()
People.append(["McKindtry", "Almond Joy"])
print(People)
for i in reversed(range(len(People))):
    for b in range(1):
        print(People[i][b]+ ":", People[i][b+1])
print(len(People))





