
try:
    # pede ao usuário para digitar a quantidade de alunos do curso
    # se nada for digitado ou ocorrer um erro, 5 será o número padrão
    alunos = int(input("Digite a quantidade de alunos (o padrão é 5):"))
except:
    alunos = 5


def verifica_nota(lst):

    # fazer com que o usuário digite um número entre 0 e 1.0
    # min e max talvez?
    if lst > 1.0 or lst < 0:
        lst = float(input("Digite valores entre 0 e 1.0: "))

lst_notas = [] 


i=0
while(i<alunos):

    nota_aop1 = float(input("Nota AOP1: "))
    nota_aop2 = float(input("Nota AOP2: "))
    nota_aop3 = float(input("Nota AOP3: "))
    avaliacao = float(input("Nota AVALIAÇÃO: "))

    verifica_nota(nota_aop1)

    # XXX implementar uma função que verifique a nota
    # se a nota for inválida, força o usuário a digitar novamente

    media_modulo = nota_aop1 + nota_aop2 + nota_aop3 + avaliacao 

    if media_modulo < 7.0:
        print("O aluno está de recuperação! A média {:.2f} é insuficiente.".format(media_modulo))

        prova_final = float(input("Digite a nota da prova final do aluno: "))
        media_modulo = prova_final
    else:
        print("Aluno aprovado!")

    lst_notas.append(media_modulo)

    i+=1


# calcular a porcentagem de aprovados e reprovados
# talvez usar numpy, não sei ainda
# uma alternativa é iterar todos os itens com o laço for
# e fazer um append em outra lista com aprovados e reprovados
# depois subtrair a quantidade de aprovado por reprovados

# listas de aprovados e reprovados
lst_ap = []
lst_rep = []

for i in lst_notas:

    if i < 5.0:
        lst_rep.append(i)
    else:
        lst_ap.append(i)

""" o tamanho da lista com as notas dos aprovados e reprovados, dirá quantos alunos obtiveram 
    resultado acima ou abaixo da média. Após isso, a porcentagem pode ser calculada.
"""
porcentagem_ap = (len(lst_ap) * 100) / alunos
procentagem_rep = 100 - porcentagem_ap
print("De um total de {} alunos, {:.2f}% foram aprovados!".format(alunos, porcentagem_ap))



        


