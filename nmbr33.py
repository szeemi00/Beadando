def mailCim (mail):
    if "@" not in mail:
        return "Nem valid"
    mail = mail.split("@")
    for i in mail[0]:
        if i=="_" or i=="," or i=="?" or i=="!" or i=="*" or i==":" or i==";":
            return "Nem valid"
    domain = mail[1].split(".")
    db=0
    for j in domain[0]:
        if db==0:
            if j.isupper()==True:
                return "Nem valid"
            db+=1
        if j=="_" or j=="," or j=="?" or j=="!" or j=="*" or j==":" or j==";":
            return "Nem valid"
    ls=["com","hu"]
    for l in ls:
        if domain[len(domain)-1]==l:
           return "Valid"
    return "Nem valid"

mail=input("Adja meg az e-mail címet és megállapítom, hogy valid-e: ")
print(mailCim(mail))