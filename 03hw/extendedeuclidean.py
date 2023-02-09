def extendedGCD(a, b):
 
    if a == 0: 
        return b, 0, 1
            
    gcd, s1, t1 = extendedGCD(b%a, a)

    #print("Pre:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s1) + "\tt:" + str(t1) + "\tFormula: " + str(a) + "(" + str(s1) + ")+" + str(b) + "(" + str(t1) + ") = " + str(gcd))
    print("Pre:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s1) + "\tt:" + str(t1))

    s,t = updateCoeff(a,b,s1,t1)

    print("Post:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s) + "\tt:" + str(t) + "\nFormula: " + str(a) + "(" + str(s) + ")+" + str(b) + "(" + str(t) + ") = " + str(gcd) + "\n")

    return gcd, s, t


def updateCoeff(a,b,s,t):
    newT = s
    newS = (b//a) * s
    newS = t - newS
    return (newS, newT) 

def run(a, b):
    gcd, s, t = extendedGCD(a,b)
    print("Final:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s) + "\tt:" + str(t) + "\nFormula: " + str(a) + "(" + str(s) + ")+" + str(b) + "(" + str(t) + ") = " + str(gcd) + "\n")

run(54046,16802)
