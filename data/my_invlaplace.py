from mpmath import *

mp.dps = 5; mp.pretty = True
tt = [0.001, 0.01, 0.1, 1, 10]
fp = lambda p: 1/(p+1)**2
ft = lambda t: t*exp(-t)
sol = ft(tt[0]),ft(tt[0])-invertlaplace(fp,tt[0],method='talbot')
print(sol)
