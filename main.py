import json 
char = [0,1,2,3,4,5,6,7,8,9]
codes = []
pure_cod = []

for x in char:
	for y in char:
		if y == x:
			break
		else:
			cod = [x,y]
			codes.append(cod)
print(f'done,len {len(codes)}')



# with open('codes.txt', 'a') as f:
#     for item in codes:
#         f.write("%s\n" % str(item))

with open('codes.json', 'w') as jsonfile:
    json.dump(codes, jsonfile)