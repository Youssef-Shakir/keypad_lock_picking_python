import json

codes = []
pure_codes = []
with open('codes.json','r') as f:
	codes = json.load(f)

for x in codes:
	x.sort()


with open('codes.txt', 'a') as f:
    for item in codes:
        f.write("%s\n" % str(item))