import re

file = open("words.txt", "r")
content = file.read()
words = content.split("\n")[:-1]
file.close()

templates = [
	re.compile("^([\w\s]+) O, ([\w\s]+)$"),
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

conjs = [
	re.compile("^([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) and then ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) or ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) but ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) therefore ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) in short ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) except ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) by the way ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,![:punct:]]+) so to speak ([\w\s\?.,!]+)$"),
	re.compile("^([\w\s\?.,!]+) all the more ([\w\s\?.,!]+)$"),
	#re.compile("^([\w\s\?.,!]+), ([\w\s\?.,!]+)$")
	]

print("Input:")
val = input()


flag = [False, False]

for c in conjs:
	m = c.match(val)
	if not m:
		continue

	if c.groups > 1:
		msg = [m.group(1), m.group(2)]
	else:
		msg = [m.group(1), ""]

	for t in templates:
		p = t.match(msg[0])
		if p:
			#Check for the **** O, **** template
			if t == templates[0]:
				if p.group(1) == p.group(2):
					if p.group(1) in words:
						flag[0] = True
				break

			if p.group(1) in words:
				flag[0] = True

	if c.groups == 1:
		flag[1] = True
	else:
		for t in templates:
			p = t.match(msg[1])
			if p:
				#Check for the **** O, **** template
				if t == templates[0]:
					if p.group(1) == p.group(2):
						if p.group(1) in words:
							flag[1] = True
					break

				if p.group(1) in words:
					flag[1] = True

if flag[0] and flag[1]:
	print("Match!")
	print(msg[0])
	print(msg[1])
