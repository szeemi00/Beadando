import math
def szoras(n):
    for i in range (0,n):
        szam = ""
        poz_o = 0
        neg_o = 0
        atl_elteres_poz = 0
        atl_elteres_neg = 0
        pozitiv = []
        negativ = []
        szam=input()
        ls=szam.split(" ")
        print (ls)
        for j in (ls):
            j=int(j)
            if j<0:
                neg_o+=j
                negativ.append(j)
            else:
                poz_o+=j
                pozitiv.append(j)
        if len(pozitiv) > 0:
            poz_atl=poz_o/len(pozitiv)
            for p in pozitiv:
                tmp=(p-poz_atl)**2
                atl_elteres_poz+=tmp
            atl_elteres_poz=atl_elteres_poz/n
        else:
            print("pozitív szórás nem számítható")
        if len(negativ)>0:
            neg_atl=neg_o/len(negativ)
            for s in negativ:
                tmp2=(s-neg_atl)**2
                atl_elteres_neg+=tmp2
            atl_elteres_neg=atl_elteres_neg/n
        else:
            print("negatív szórás nem számítható")
        print ("Pozitív szórás:",math.sqrt(atl_elteres_poz),"Negatív szórás:",math.sqrt(atl_elteres_neg))
n=int(input("Kérek egy számot: "))
szoras(n)