import os



table = {}
####################

#print (os.listdir("./"))
rootDir="./"
for dirName, subdirList, fileList in os.walk(rootDir):
	print('Found directory: %s' % dirName)
	for fname in fileList:

		with open(dirName+"/"+fname, "rb") as f:
			# Check the beginning of the file
			count = 16
			data = "h"
			print('\t%s' % fname)
			while (byte := f.read(1)):
				count-=1
				data+=str(byte)
				if (count <=0):
					break

			data+="0000000000"
		with open(dirName+"/"+fname, "rb") as f:
			# Check also the ending of the file... hoping file is bigger than 16 bytes
			try:
				f.seek(-16,2)
				byte = f.read(16)
				data+=str(byte)
			except:
				pass

		# Use the byte data for the table
		if (data not in table.keys()):
			table[data]=[]
		table[data].append(dirName+"/"+fname)

# Now count the duplicates
for i in table.keys():
	if (len(table[i]) > 1):
		print ("There may be duplicates duplicates in ")
		for j in table[i]:
			print (j)
		print ("")
