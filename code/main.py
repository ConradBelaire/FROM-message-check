import re

file = open("words.txt", "r")
content = file.read()
words = content.split("\n")[:-1]
file.close()

regex = [
	re.compile("^Seek ([\w\s]+)$"),
	re.compile("^([\w\s]+) ahead$"),
	re.compile("^No ([\w\s]+) ahead$"),
	re.compile("^Be wary of ([\w\s]+)$"),
	re.compile("^Try ([\w\s]+)$"),
	re.compile("^First off, ([\w\s]+)$"),
	re.compile("^Still no ([\w\s]+)[.]{3}$"),
	re.compile("^Why is it always ([\w\s]+)\?$"),
	re.compile("^Didn't expect ([\w\s]+)[.]{3}$"),
	re.compile("^Could this be a ([\w\s]+)\?$"),
	re.compile("^Time for ([\w\s]+)$"),
	re.compile("^Behold, ([\w\s]+)!$"),
	re.compile("^Offer ([\w\s]+)$"),
	re.compile("^Praise the ([\w\s]+)!$"),
	re.compile("^([\w\s]+)!$"),
	re.compile("^([\w\s]+)\?$"),
	re.compile("^([\w\s]+)[.]{3}$"),
	re.compile("^([\w\s]+)$"),
	re.compile("^If only I had a ([\w\s]+)[.]{3}$"),
	re.compile("^Likely ([\w\s]+)$")]

print("Input:")
val = input()

for r in regex:
	m = r.match(val)
	if m:
		if m.group(1) in words:
			print("Match!")
			print(m)
			print(m.group(1))
