Web_Development = ["Alex", "Ajay", "Ben"]
Data_Science = ["Alan", "Max", "Tom"]
UIUX_Design = ["David", "Jane", "Jose"]
all_participants = Web_Development + Data_Science + UIUX_Design
Web_Development.append("Harry")
Data_Science.insert(1, "Louis")
UIUX_Design.pop()
new_Datascience = Data_Science.copy()
del Data_Science
print(Web_Development[:2])
name_lengths = [len(name) for name in new_Datascience]
print("Length of each name in Data Science list:", name_lengths)
if "Asha" in all_participants:
    print("Yes, 'Asha' is in the workshop list")
else:
    print("No, 'Asha' is not in the workshop list")
first_participants = (Web_Development[0], new_Datascience[0], UIUX_Design[0])
print("First participants from each workshop:", first_participants)
