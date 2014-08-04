from hashlib import sha1

passwd = "zWp8LGn01wxJ7"
aim = "e48d316ed573d3273931e19f9ac9f9e6039a4242"

for line in open('9_queen_solution.txt','r').readlines():
	line = line.strip()
	encrypt = sha1((passwd + line + "\n").encode('utf-8')).hexdigest()
	print(encrypt)
	if(encrypt == aim):
		print(line)
		break

