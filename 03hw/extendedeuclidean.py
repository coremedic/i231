def extendedGCD(a, b):
 
    if a == 0: 
        return b, 0, 1
            
    gcd, s1, t1 = extendedGCD(b%a, a)
    print("\ta: " + str(a) + "\tb: " + str(b) + "\ts: " + str(s1) + "\tt: " + str(t1))
    s,t = updateCoeff(a,b,s1,t1)
    print("\ta: " + str(a) + "\tb: " + str(b) + "\ts: " + str(s) + "\tt: " + str(t) + "\n")
    print(str(a) + "(" + str(s) + ")+" + str(b) + "(" + str(t) + ")")
    return gcd, s, t


def updateCoeff(a,b,s,t):
    return (t - (b//a) * s, s) 


gcd, s, t = extendedGCD(56,15)
print("extendedGCD(25,10)-> ", "GCD:", gcd,"\ts:", s, "\tt:",t)