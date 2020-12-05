class Lutadores:
    n_vitorias = 0
    n_derrotas = 0

    def __init__(self, nome, altura, peso, forca, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.forca = forca
        self.resistencia = resistencia

    def __repr__(self):
        return f'O lutador {self.nome} tem {self.altura}m de altura e pesa {self.peso}kg, tem {self.forca}% de força e' \
               f' {self.resistencia}% de resistência. Vitórias x Derrotas = {self.n_vitorias} x {self.n_derrotas}'


def luta(l1, l2):
    if int(l1.peso/10) == int(l2.peso/10):
        if l1.forca + l1.resistencia > l2.forca + l2.resistencia:
            l1.n_vitorias = l1.n_vitorias + 1
            l2.n_derrotas = l2.n_derrotas +1
            print(f'O lutador {l1.nome} venceu a luta!')
        else:
            l2.n_vitorias = l2.n_vitorias + 1
            l1.n_derrotas = l1.n_derrotas + 1
            print(f'O lutador {l2.nome} venceu a luta!')
    else:
        print('Luta inválida: Os lutadores pertencem a categorias diferentes')


print('\nCADASTRO DOS LUTADORES:')
lutador_1 = Lutadores('João', 1.8, 75, 70, 80)
print(lutador_1)
lutador_2 = Lutadores('Pedro', 1.85, 79, 90, 60)
print(lutador_2)
lutador_3 = Lutadores('Gabriel', 1.75, 71, 80, 70)
print(lutador_2)

print(f'\nLuta entre {lutador_1.nome} e {lutador_2.nome}:')
luta(lutador_1, lutador_2)
print(f'\nLuta entre {lutador_1.nome} e {lutador_3.nome}:')
luta(lutador_1, lutador_3)
print(f'\nLuta entre {lutador_2.nome} e {lutador_3.nome}:')
luta(lutador_2, lutador_3)

print('\nAO FINAL DE TODOS OS CONFRONTOS:')
print(f'Historia de Vitórias x Derrotas do {lutador_1.nome}: {lutador_1.n_vitorias} x {lutador_1.n_derrotas}')
print(f'Historia de Vitórias x Derrotas do {lutador_2.nome}: {lutador_2.n_vitorias} x {lutador_2.n_derrotas}')
print(f'Historia de Vitórias x Derrotas do {lutador_3.nome}: {lutador_3.n_vitorias} x {lutador_3.n_derrotas}')
