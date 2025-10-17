Web_Development = ["Alex", "Ajay", "Ben"]
Data_Science = ["Alan", "Max", "Tom"]
UIUX_Design = ["David", "Jane", "Jose"]
all_participants = Web_Development + Data_Science + UIUX_Design
Web_Development.append("Harry")
Data_Science.insert(1, "Louis")
UIUX_Design.pop()
new_Datascience = Data_Science.copy()
del Data_Science
print(new_Datascience)
print(Data_Science)