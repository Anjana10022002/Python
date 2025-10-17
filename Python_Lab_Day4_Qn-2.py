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
print("Length of each name in copied Data Science list:", name_lengths)
is_asha_present = any("Asha" in workshop for workshop in all_participants)
print("Is 'Asha' present in any workshop list", is_asha_present)
first_participants = (Web_Development[0], new_Datascience[0], UIUX_Design[0])
print("First participants from each workshop:", first_participants)