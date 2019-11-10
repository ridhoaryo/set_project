p = [1,2,4,7,9,19]
q = [5,12,16,17,7,9,19,6]
r = [19,6,3,8]
p = set(p)
q = set(q)
r = set(r)
print('set P: {0}'.format(p))
print('set Q: {0}'.format(q))
print('set R: {0}'.format(r))

p_irisan_q = p.intersection(q)
print('P irisan Q adalah: {0}'.format(p_irisan_q))

p_irisan_q_irisan_r = p.intersection(q).intersection(r)
print('P irisan Q irisan R adalah: {0}'.format(p_irisan_q_irisan_r))