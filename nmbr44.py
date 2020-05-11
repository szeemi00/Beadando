import math
def szoras(n):
    eredmeny_poz=[]
    eredmeny_neg=[]
    for i in range (0,n):
        szam = ""
        poz_o = 0
        neg_o = 0
        atl_elteres_poz = 0
        atl_elteres_neg = 0
        pozitiv = []
        negativ = []
        szam = input()
        ls=szam.split(" ")
        for j in (ls):
            j = int(j)
            if j<0:
                neg_o += j
                negativ.append(j)
            else:
                poz_o += j
                pozitiv.append(j)
        if len(pozitiv) > 1:
            poz_atl = poz_o/len(pozitiv)
            for p in pozitiv:
                tmp = (p-poz_atl)**2
                atl_elteres_poz += tmp
            atl_elteres_poz = atl_elteres_poz/len(pozitiv)
            atl_elteres_poz = math.sqrt(atl_elteres_poz)
            atl_elteres_poz = f"{atl_elteres_poz:0.3}"
        else:
            atl_elteres_poz = "nem számolható"
        if len(negativ) > 1:
            neg_atl = neg_o/len(negativ)
            for s in negativ:
                tmp2 = (s-neg_atl)**2
                atl_elteres_neg += tmp2
            atl_elteres_neg = atl_elteres_neg/len(negativ)
            atl_elteres_neg = math.sqrt(atl_elteres_neg)
            atl_elteres_neg = f"{atl_elteres_neg:0.3}"
        else:
            atl_elteres_neg = "nem számolható."
        eredmeny_poz.append(atl_elteres_poz)
        eredmeny_neg.append(atl_elteres_neg)
    for k in range(len(eredmeny_poz)):
        print("Pozitív szórás:",eredmeny_poz[k]+","+" negatív szórás:",eredmeny_neg[k])
 
n = int(input("n= "))
szoras(n)