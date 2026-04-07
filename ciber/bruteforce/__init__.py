def bruteforce(senhacorreta, listadesenhas):
    for i, senha in enumerate(listadesenhas):
        print(f'tentativa {i+1}: {senha}')
        if senha == senhacorreta:
            print("acertou a senha")
            return True

    print("não se encontrou a senha")
    return False
senhacorreta = 'kleito2009'
listadesenhas = ['adimin', 'user69','kleito2009']
bruteforce(senhacorreta, listadesenhas)