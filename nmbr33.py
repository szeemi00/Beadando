def mailCim (mail):
    kukac=0
    for c in mail:
        if c=="@":
            kukac+=1
    if kukac==1:
        mail = mail.split("@")
    else:
        return print("Nem valid")
    for i in mail[0]:
        if i=="_" or i=="," or i=="?" or i=="!" or i=="*" or i==":" or i==";":
            return print ("Nem valid")
    domain = mail[1].split(".")
    for j in domain[0]:
        if j.isupper()==True or j=="_" or j=="," or j=="?" or j=="!" or j=="*" or j==":" or j==";":
            return print("Nem valid")
    ls=["com","hu"]
    for l in ls:
        if domain[1]==l:
           return print("Valid")
    return print("Nem valid")

mail=input("Adja meg az e-mail címet és megállapítom, hogy valid-e: ")
mailCim(mail)
