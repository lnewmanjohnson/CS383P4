import sys
import hashlib

lines = [line.strip() for line in open('word lists/smallList1.txt')]
dictionary = dict()
cracked = dict()


with open('weak.txt') as file:
	for line in file:

		split = line.split(' ')
		if (len(split) == 2):
			dictionary[split[1].strip()] = 0
print ("finished ingesting list")
print(dictionary)

numRead = 0
for line in lines:
	numRead += 1
	hash = hashlib.md5(line).hexdigest()
	if hash in dictionary:
		dictionary[hash] = 1
		cracked[line] = hash
		print ("password:", line, " was cracked")

print(numRead)
print(cracked)

out = open('output.txt', 'w')
for item in cracked.items():
	print(''.join(item))
	print('\n')
	out.write(''.join(item))
	out.write('\n')
