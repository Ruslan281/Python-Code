def daxil_et():
    a=float(input('1-ci ededi daxil edin:'))
    b=float(input('2-ci ededi daxl edin:'))
    return a,b
def gorunus():
    print('---------------')
    print('|  + : Toplama |')
    print('|  - : Cixma |')
    print('|  * : Vurma |')
    print('|  / : Bolme |')
    print('---------------')
    print('|  x : Cixis |')
    t=input('Seciminizi edin :')
    while t not in ['+','-','*','/','x']:
        t=input()
        return t
def hesabla():
    n1,n2=daxil_et()
    p=gorunus()
    if p=='+':
        print('Cem=',n1+n2)
    if p=='-':
        print('Ferq=',n1-n2)
    if p=='*':
        print('Hasil=',n1*n2)
    if p=='/':
        print('Qismet=',n1/n2)

hesabla()
