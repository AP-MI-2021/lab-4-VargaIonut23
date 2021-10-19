def citire_lista():
    l = []
    listasstring = input("Dati lista ")
    numberasstring = listasstring.split(",")
    for x in numberasstring:
        l.append(str(x))
    return l

    def print_menu():
        print (" 1. Citire lista ")

def se_gaseste_in_lista(l , l2):
    '''

    :param l: un sir de caractere
    :param l2: lista str care corespunde cerintei 2 si cu ajutorul careia se va verifica
    :return: 0 daca l2 nu este in l si 1 in caz constrar
    '''
    ok = 0
    for i in l:
        if i == l2:
            ok = 1

    if ok == 1 :
        return "DA"
    else:
        return "NU"

def repetare(l):
    '''

    :param l: un sir de caractere
    :return: returneaza o lista cu elementele care se regasesc de mai multe ori sau afiseaza unic in cazul in care toate elementele apar o data
    '''
    l2 = []
    ok = 0
    for i in l:
        if aparitii(i , l) > 1 and repetare2(i , l2) == 1:
            l2.append(i)
            ok = 1

    if ok == 1:
        return l2
    else:
        return "UNIC"

def repetare2(i , l2):
    #determina daca acel sir se repeta in l2
    for x in l2:
        if str(x) == str(i):
            return 0
    return 1
def aparitii(x , l):
   #determina numarul de aparitii a lui x in lista l
    nr_aparitii = 0
    for i in l:
        if str(x) == str(i):
            nr_aparitii = nr_aparitii + 1
    return nr_aparitii

def palindrom (l):
    '''

    :param l: un sir de caractere
    :return: va returna toate sirurile de caractere care sunt un palindrom
    '''
    l2 = []
    for i in l:
        xStr = str(i)
        if xStr == xStr[::-1]:
            l2.append(i)

    return l2


    # 5.vom gasi caracterul care are cele mai multe aparitii ,iar apoi vom strabate lista iar sirurile care contin acel caracter le vom inlocui cu aparitia sa

def print_menu():
    print (" 1. Citire  lista ")
    print (" 2. Se afiseaza daca o lista data se gaseste in cea initiala")
    print (" 3. Se afiseaza o lista care contine toate elementele care apar de mai multe ori in lista principala si unic daca nu se repeta niciun element")
    print (" 4. Se afiseaza acele siruri de caractere din lista care sunt un palindrom ")
    print (" 5. Oprire")

def test_se_gaseste_in_lista():
    assert se_gaseste_in_lista(["aaa", "bbbbb" , "ccc"] , "aaa") == "DA"
    assert se_gaseste_in_lista(["abc" , "bac"] , "cde") == "NU"
    assert se_gaseste_in_lista(["asd" , "asd" , "cme"] , "cme") == "DA"

def test_palindrom():
    assert palindrom(["aaa" , "bbb"]) == ["aaa" , "bbb"]
    assert palindrom(["abc" , "aba" , "vcv"]) == ["aba" , "vcv"]
    assert palindrom(["aa" , "ca" ]) == ["aa"]

def test_repetare():
    assert repetare(["aaa" , "aaa"]) == ["aaa"]
    assert repetare(["aba", "aaa" , "aba"]) == ["aba"]
    assert repetare(["aaa", "aac"]) == "UNIC"


def main():
    l = []
    test_se_gaseste_in_lista()
    test_palindrom()
    test_repetare()
    while True:
        print_menu()
        optiune = input("Dati optiunea ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            l2 = str(input())
            print(se_gaseste_in_lista(l,l2))
        elif optiune == "3":
            print(repetare(l))
        elif optiune == "4":
            print(palindrom(l))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati: ")


if __name__ == "__main__":
    main()