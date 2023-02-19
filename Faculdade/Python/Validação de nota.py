nota = float(input('Qual é a nota do aluno?'))
print(nota)
if(nota>=7):
    situacao = 'Aprovado'
elif(nota>=5):
    situacao = 'em Recuperação'
else:
    situacao = 'Reprovado'

print(f'O estudante esta {situacao}')