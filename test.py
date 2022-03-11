group = ''
group_number = ''

text = "М-49"
for c in text:
	if c.isdigit():
		group_number = group_number + c
	elif c.isalpha():
	 	group = group + c

print(group)
print(group_number)