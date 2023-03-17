from tkinter import *
import "TECHCOM.png"

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="TECHCOM.png")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()

"""
1-No código, há a inserção do elemento de imagem e o botão.
Nas linhas 10, 11 e 12, é feita a criação do objeto Label para conter
a imagem e seu posicionamento. Observe que passamos a utilizar o método pack(),
que coloca o elemento centralizado e posicionado o mais perto possível do topo,
depois dos elementos posicionados anteriormente.

2-O elemento botão é criado na linha 14 com os atributos text e command,
os quais são respectivamente o texto exibido no corpo do botão e a função a ser
executada quando o botão é clicado.

3-Para o funcionamento correto do botão, é preciso definir a função funcClicar(),
nas linhas 3 e 4. Essa função serve apenas para imprimir na tela a string “Botão pressionado”.
"""