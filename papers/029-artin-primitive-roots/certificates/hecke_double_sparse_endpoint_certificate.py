"""Standalone exact enclosure of the double-sparse variational endpoint.

This uses only fractions.Fraction and integer arithmetic.  Analytic validity of the density
and contour branches is separate from this algebraic certificate.
"""

from fractions import Fraction as F


def coefficients(d):
    return 6*d*(6*d*d-15*d+7),54*d*d-39*d+4,2*d-2


def root_polynomial(d,x):
    a,b,c=coefficients(d)
    return (a*x+b)*x+c


def x_interval(d,steps=280):
    lo,hi=F(5,7),F(1)
    vlo,vhi=root_polynomial(d,lo),root_polynomial(d,hi)
    assert vlo<=0<vhi
    if vlo==0:
        return lo,lo
    for _ in range(steps):
        mid=(lo+hi)/2
        v=root_polynomial(d,mid)
        if v==0:
            return mid,mid
        if v<0:lo=mid
        else:hi=mid
    return lo,hi


def interval_add(a,b):
    return a[0]+b[0],a[1]+b[1]


def interval_mul(a,b):
    products=[u*v for u in a for v in b]
    return min(products),max(products)


def interval_scale(a,c):
    return interval_mul(a,(c,c))


def g_interval(d,xi):
    # g=(1-x)*F_x+d*F_d, after collecting powers of x.
    aa=36*d**3-42*d
    bb=72*d**3-126*d*d+84*d-4
    cc=54*d*d-37*d+4
    return interval_add(interval_mul(
        interval_add(interval_scale(xi,aa),(bb,bb)),xi),(cc,cc))


def qdd(d,r):
    return 432*d*d-(216+432*r)*d+10+252*r+72*r*r


def decimal_bound(x,digits=45,upper=False):
    scale=10**digits
    n=x.numerator*scale//x.denominator
    if upper and n*x.denominator != x.numerator*scale:n+=1
    return f'{n//scale}.{n%scale:0{digits}d}'


def main():
    assert root_polynomial(F(1,4),F(15,19))==F(81,5776)>0
    assert root_polynomial(F(1,3),F(16,19))==F(-28,361)<0
    assert root_polynomial(F(1,6),F(5,7))==0
    assert F(1,21)<F(1,19) and F(2,39)<F(1,19)
    # Q_dd increases with r because its derivative is at least 108.
    assert 252-432*F(1,3)==108>0
    endpoint_values=[qdd(d,F(4,75)) for d in [F(1,6),F(1,3)]]
    assert max(endpoint_values)==F(-2622,625)<0
    print('Q_dd upper throughout central rectangle:',max(endpoint_values))
    print('Boundary/interior root tests: 0, 81/5776, -28/361; all verified')

    # At a stationary point r''=Q_dd/F_x<0. The endpoint values are
    # below an interior value, hence there is exactly one stationary
    # point, the global maximum. Its derivative sign is that of g.
    lo,hi=F(1,6),F(1,3)
    assert g_interval(lo,x_interval(lo))[0]>0
    assert g_interval(hi,x_interval(hi))[1]<0
    for _ in range(180):
        mid=(lo+hi)/2
        xi=x_interval(mid)
        gi=g_interval(mid,xi)
        if gi[0]>0:lo=mid
        elif gi[1]<0:hi=mid
        else:
            # This fallback is not needed in the certified run, but
            # keeps the sign decision explicitly rigorous.
            gi=g_interval(mid,x_interval(mid,steps=560))
            if gi[0]>0:lo=mid
            elif gi[1]<0:hi=mid
            else:raise ArithmeticError('Increase exact root enclosure precision')
    assert g_interval(lo,x_interval(lo))[0]>0
    assert g_interval(hi,x_interval(hi))[1]<0
    mid=(lo+hi)/2
    xlo,xhi=x_interval(mid)
    # A>=8/3 and -C>=4/3 give F_x=sqrt(B^2-4AC)>3 at
    # the positive root. Also |F_d|<=15+21+2=38, so
    # |x'|<13 and |r'|<=1+(1/3)*13<6 on the central interval.
    assert 4*F(8,3)*F(4,3)>9
    assert F(38,3)<13 and 1+F(13,3)<6
    rlo=mid*(1-xhi)
    rhi=mid*(1-xlo)+3*(hi-lo)
    # The maximum is at least the midpoint value, and at most
    # midpoint value plus 6 times the maximum displacement.
    assert F(1,19)<rlo<rhi<F(4,75)
    dlo,dhi=1/(10+6*rhi),1/(10+6*rlo)
    assert F(25,258)<dlo<dhi<F(19,196)
    print('Maximizing d lower:',decimal_bound(lo))
    print('Maximizing d upper:',decimal_bound(hi,upper=True))
    print('r_sharp lower:',decimal_bound(rlo))
    print('r_sharp upper:',decimal_bound(rhi,upper=True))
    print('Delta_sharp lower:',decimal_bound(dlo))
    print('Delta_sharp upper:',decimal_bound(dhi,upper=True))
    print('h_sharp lower:',decimal_bound(6*dlo))
    print('h_sharp upper:',decimal_bound(6*dhi,upper=True))
    print('Verified: 25/258 < Delta_sharp < 19/196, and h_sharp < 7/12')
    print('No floating-point square root, numerical optimizer, or ODE is used.')


if __name__=='__main__':
    main()
