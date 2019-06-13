from hashlib import sha1
from Crypto.PublicKey import DSA
import random

private_key = 1234

p = 145774370140705743619288815016506936272601276321515267981294709325646228235350799641396853482542510455702593145365689674776551326526283561120782331775753481248764911686023024656237178221049671999816376444280423000085773391715885524862881877222848088840644737895543531766907185051846802894682811137086905085419
q = 739904609682520586736011252451716180456601329519
g = 52865703933600072480340150084328845769706702669400766904467248075164948743170867377627486621900744105555465052783047541675343643777082719270261354312243195450389581166294097053506337884439282134405767273312076933070573084676163659758350542617531330447790290695414443063102502247168199735083467132847036144443


k = random.randint(2,q)
assert k < q
m = b'cat flag'
y = pow(g,x,p)
dsa = DSA.construct((y,g,p,q,x))
r,s = dsa.sign(m,k)
assert dsa.verify(m,(r,s)) == True
print(f"r = {r}")
print(f"s = {s}")
# print(vertify(m,r,s))
