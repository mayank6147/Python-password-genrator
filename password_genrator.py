import random
def Uppercase(alen , uppercase):
    test=len(uppercase)
    while len(uppercase)<(test+alen):
        s="".join(random.sample(uppercase,k=len(uppercase)))
        uppercase+=s
            
    uppercase="".join(random.sample(uppercase,k=len(uppercase)))
    return uppercase  
    
def Lowercase(alen,lowercase):
    test=len(lowercase)
    while len(lowercase)<(test+alen):
        s="".join(random.sample(lowercase,k=len(lowercase)))
        lowercase+=s
            
    lowercase="".join(random.sample(lowercase,k=len(lowercase)))
    return lowercase

def Number(alen,number):
    test=len(number)
    while len(number)<test+alen:
        s="".join(random.sample(number,k=len(number)))
        number+=s
    number="".join(random.sample(number,k=len(number)))
    return number
def SpecialCharacter(alen,special):
    test=len(special)
    while len(special)< alen+test:
        s="".join(random.sample(special,k=len(special)))
        special+=s
    special="".join(random.sample(special,k=len(special)))
    return special

def genrator(n):
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    number="1234567890"
    special="!@#$%^&*()<>,._/\|-+{}[]"
    diff=n-86
    each=diff//4
    p1=Uppercase(each,uppercase)
    p2=Lowercase(each,lowercase)
    p3=SpecialCharacter(each,special)
    p4=Number(each,number)
    total_char=p1+p2+p3+p4
    total_char="".join(random.sample(total_char,k=len(total_char)))
    print(len(total_char))
    password="".join(random.sample(total_char,k=n))
    return password
len_pass=int(input('Enter Length of Password : '))
password=genrator(len_pass)
print(password)
print(len(password))
