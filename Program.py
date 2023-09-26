
with open("file.txt", "r") as input:
	
	with open("f.txt", "w") as output:
		
		for line in input:
			output.write(line)
