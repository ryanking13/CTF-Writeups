import re
import zlib
f = open('chall.png', 'rb').read()

checker = f[0x25:0x46] 

comments = re.findall(b'iTXtComment[\s\S]*?(?=iTXt)', f)

fix = []
for c in comments:
	c = c[len(b'iTXtComment\x00\x01\x001337\x00C0|V||V|3|\\|7\x00'):]
	fix.append(c)
	
order = []
for f in fix:
	
	code = zlib.decompress(f).decode()
	order.append((int(code[1:]), code[0]))
	order.sort()

print(len(order))
for o in order:
	print(o[1], end='')
	
# SECT{D4K3Y_2_D4_G1B50N_5UP3RU53R_15_G0D_H3H3!}
# SECT{D4_K3Y_2_D4_G1B50N_5UP3RU53R_15_G0D_H3H3!}
