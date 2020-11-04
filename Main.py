#questao 1.a = P(X=x) = (x-1)/10
#E(X) = 1*(0/10) + 2*(1/10) + 3*(2/10) + 4*(3/10) + 5*(4/10) + 6*(5/10) + 7*(6/10) + 8*(7/10) + 9*(8/10) + 10*(9/10) + 11*(10/10)

def simula_questao_1(numero_de_simulacoes):
    bolas_sorteadas = [False] * 10
    print(str(bolas_sorteadas))
    for i in range(numero_de_simulacoes):
        #enquanto nao sortear um numero igual
        for j in range(11):
            print(str(j))

simula_questao_1(1)