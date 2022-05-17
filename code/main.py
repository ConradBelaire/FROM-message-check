import re

words = ["skeleton", "dog"]
regex = [re.compile("^Seek ([\w\s]+)$"), re.compile("^([\w\s]+) ahead$")]

print("Input:")
val = input()

for r in regex:
	m = r.match(val)
	if m:
		if m.group(1) in words:
			print("Match!")
			print(m)
			print(m.group(1))
