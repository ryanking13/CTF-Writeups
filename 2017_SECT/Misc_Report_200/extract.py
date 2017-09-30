# http://lotabout.me/orgwiki/pdf.html
# https://blog.idrsolutions.com/2011/05/understanding-the-pdf-file-format-%E2%80%93-pdf-xref-tables-explained/

lines = open('xref.txt', 'r').readlines()

lines = [l.split()[1][3:] for l in lines]

flag = ''

for l in lines:
	if l == '00':
		continue
		
	flag = chr(int(l, 16)) + flag

print(flag)