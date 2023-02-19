valor = 10
quant = int(input("Quantas peças?"))

ValorTotal = (valor * quant)

if(quant>20):
    Total = (ValorTotal/100*80)
elif(quant>10):
    Total = (ValorTotal/100*90)
else:
    Total = ValorTotal

valorfinal = (Total/quant)

print(f"O valor total é: {Total}")
print(f"Cada peça vai sair á: {valorfinal}")