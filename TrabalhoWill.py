class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def imprimir(self): 
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo

    def inserir_inicio(self, valor):
        novo = NoDuplo(valor)

        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
            return

        novo.proximo = self.primeiro
        self.primeiro.anterior = novo
        self.primeiro = novo

    def inserir_final(self, valor):
        novo = NoDuplo(valor)

        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
            return

        novo.anterior = self.ultimo
        self.ultimo.proximo = novo
        self.ultimo = novo

    def inserir_meio(self, valor, posicao):
        if posicao == 0:
            self.inserir_inicio(valor)
            return

        atual = self.primeiro
        contador = 0

        while atual is not None and contador < posicao:
            atual = atual.proximo
            contador += 1

        if atual is None:
            self.inserir_final(valor)
            return

        novo = NoDuplo(valor)
        anterior_no = atual.anterior

        novo.anterior = anterior_no
        novo.proximo = atual
        anterior_no.proximo = novo
        atual.anterior = novo

    def remover_inicio(self):
        if self.primeiro is None:
            return

        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
            return

        self.primeiro = self.primeiro.proximo
        self.primeiro.anterior = None

    def remover_final(self):
        if self.ultimo is None:
            return

        if self.primeiro == self.ultimo:
            self.priemiro = None
            self.ultimo = None
            return

        self.ultimo = self.ultimo.anterior
        self.ultimo.proximo = None

lista = ListaLigada()
lista.inserir_inicio(10)
lista.inserir_final(20)
lista.inserir_final(40)
lista.inserir_meio(30,2)

lista.imprimir()

print(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

lista.remover_inicio()
lista.remover_final()

lista.imprimir()

