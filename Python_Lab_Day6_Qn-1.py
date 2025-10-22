attendance = [18, 20, 19, 15, 21]
for x in attendance:
	if x == 20:
		print("Full")
	else:
		print("Not Full")
count = 0
for x in attendance:
	if x >=20:
	    count = count + 1
print("Number of days class was full:", count)
totalAttendance = sum(attendance)
print("Total attendance for all 5 days: ", totalAttendance)
