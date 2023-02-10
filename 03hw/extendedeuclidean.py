def extendedEuclidean(a, b):
    if a == 0: 
        return b, 0, 1
            
    gcd, s, t = extendedEuclidean(b%a, a)

    print("Pre:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s) + "\tt:" + str(t))

    tmp = s
    s = (b//a) * s
    s = t - s
    t = tmp

    print("Post:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s) + "\tt:" + str(t) + "\nFormula: " + str(a) + "(" + str(s) + ")+" + str(b) + "(" + str(t) + ") = " + str(gcd) + "\n")

    return gcd, s, t

def gcd(a, b):
    gcd, s, t = extendedEuclidean(a,b)
    print("Final:\ta:" + str(a) + "\tb:" + str(b) + "\ts:" + str(s) + "\tt:" + str(t) + "\nFormula: " + str(a) + "(" + str(s) + ")+" + str(b) + "(" + str(t) + ") = " + str(gcd) + "\n")

gcd(817542,9438)
