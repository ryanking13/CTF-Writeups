# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
# https://github.com/JulesDT/RSA-Hastad/blob/master/rsaHastad.py
import decimal

def gcd(a, b):
    if a == 0:
        return b, 0, 1

    g, y, x = gcd(b % a, a)
    return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = gcd(a, m)
    return x % m

e = 3
c1 = 261345950255088824199206969589297492768083568554363001807292202086148198631069614798317906886299072940920951937069931075994761321418000094107070197147416232451234562137722533530001310201471551767502259512846878693743921465671480793619416441157679876573645967333221476165966649313807280916495883545554435023160
n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c2 = 147535246350781145803699087910221608128508531245679654307942476916759248402180698511227611535377693488970864036787712988194245030670645208110795125254578153846086630526499182264937761201472425511144209974951604149869356601106990003338401922581070216536894405879630689229777166269267902906144122090456277151649
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
c3 = 633230627388596886579908367739501184580838393691617645602928172655297372236196464426416204577901621898655053073397875989780009016829587556817421643262778573735371948196428638345897175520696355459658575711857530988655436690752338676635648544800403073660763700012964410416220335837344998266649955163596047639781
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723

c = c1 * (n2 * n3) * modinv(n2*n3, n1) +\
    c2 * (n1 * n3) * modinv(n1*n3, n2) +\
    c3 * (n1*n2) * modinv(n1*n2, n3)

c = c % (n1*n2*n3)

# print(c)

decimal.getcontext().prec = 500
c = decimal.Decimal(c)
m = c ** (decimal.Decimal("1.0")/3)

m = int(m)
# print(m)

message = hex(m)[2:]
# print(message)

flag = ''

for i in range(0,len(message),2):
    flag += chr(int(message[i:i+2], 16))

print(flag)