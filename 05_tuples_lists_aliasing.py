 
def quotient_and_reminsder(x,y):
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = quotient_and_reminsder(4,5)
print(quot, rem)