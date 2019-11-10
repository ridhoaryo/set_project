import math
import sympy

ss = set(range(0,11,1))
aa = set(sympy.primerange(0,10))
bb = set([5,7,9])

print('S:',ss,'\n','A:',aa,'\n','B',bb,'\n')

cc = set(aa&bb)
dd = set(aa|bb)
ee = set(aa&(aa|bb))
ff = set(bb&(aa|bb))
gg = set((aa|bb)&(aa|bb))
hh = set((aa&bb)|(aa|bb))

print(cc)
print(dd)
print(ee)
print(ff)
print(gg)
print(hh)