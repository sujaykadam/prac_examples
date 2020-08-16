import socket
import os
import sys

lis=list()
genlis=list()

for i in range(0,256):
	ele="172.11.14."+str(i)
	genlis.append(ele)

f= open("hits.txt","w+")

for server_ip in genlis:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rep = os.system('ping ' + server_ip)
	if rep == 0:
		lis.append(server_ip)
		f.write(server_ip+"\n")
f.close()
print("\n.......\n")
print(lis)
print("\n.......\n")