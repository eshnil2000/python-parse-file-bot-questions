#Process data file from: https://rajpurkar.github.io/SQuAD-explorer/
# Data format:b'Woodrow_Wilson\tWas Wilson president of the American Political Science Association in 1910 ?\tYes\tNULL\teasy\tdata/set3/a8\n'
# Take Question & Answer (columns 1,2) and save them in new file
# New file format: question & answer on alternating lines

import os
import re

list=[]
question=[]
answer=[]
for _file in os.listdir('raw_files'):
	chats=open('raw_files/' + _file, 'rb').readlines()
	for text_line in chats:
		print(text_line)
		lower_line=text_line.lower()
		line=re.split(rb'\t+', lower_line)
		question.append(str(line[1],"ISO-8859-1"))
		answer.append(str(line[2],"ISO-8859-1"))

	f= open("files/"+_file,"w+")
	for q,a in zip(question,answer):
		f.write(q+"\n")
		f.write(a+"\n")
	f.close()
