class Lutadores:

    def __init__(self, nome, altura, peso, forca, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.forca = forca
        self.resistencia = resistencia
        self.n_vitorias = 0
        self.n_derrotas = 0

    def __repr__(self):
        return f'{self.nome}: {self.altura}m de altura - {self.peso}kg - {self.forca}% de força -' \
               f' {self.resistencia}% de resistência. Vitórias x Derrotas = {self.n_vitorias} x {self.n_derrotas}'

    def aumentar_vitoria(self):
        self.n_vitorias += 1

    def aumentar_derrota(self):
        self.n_derrotas += 1


class Luta:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        if int(self.l1.peso / 10) == int(self.l2.peso / 10):
            self.eh_valido = 1
            print('Os lutadores pertencem à mesma categoria - LUTA VÁLIDA')
        else:
            self.eh_valido = 0

    def lutar(self):
        if self.eh_valido:
            if self.l1.forca + self.l1.resistencia > self.l2.forca + self.l2.resistencia:
                self.l1.aumentar_vitoria()
                self.l2.aumentar_derrota()
                print(f'O lutador {self.l1.nome} venceu a luta!')
            else:
                self.l2.aumentar_vitoria()
                self.l1.aumentar_derrota()
                print(f'O lutador {self.l2.nome} venceu a luta!')
        else:
            print('Os lutadores pertencem a categorias distintas - LUTA INVÁLIDA')


lutador_1 = Lutadores('João', 1.8, 75, 70, 80)
lutador_2 = Lutadores('Pedro', 1.85, 79, 90, 60)
lutador_3 = Lutadores('Gabriel', 1.75, 71, 80, 70)

print('\nSEJA BEM-VINDO AO DESAFIO PAME DE LUTA:\nO modelo de competição será baseado em todos contra todos, '
      'respeitando as devidas categorias\n\n'
      'OS SEGUINTES LUTADORES JÁ ESTÃO INSCRITOS:')

print(lutador_1)
print(lutador_2)
print(lutador_3)

if input('\nDESEJA INSERIR MAIS ALGUM LUTADOR? (S/N): ').lower() == 's':
    a = input('Insira o nome do seu lutador: ')
    b = input('Insira a altura (em metros) do seu lutador: ')
    c = input('Insira o peso (em quilogramas) do seu lutador: ')
    d = input('Insira a força (em porcentagem (%)) do seu lutador conforme medição PAME2020.2: ')
    e = input('Insira a resistência (em porcentagem (%)) do seu lutador conforme medição PAME2020.2: ')
    lutador_4 = Lutadores(a, b, c, d, e)
    print(f'Confira os dados do seu lutador:\n{lutador_4}')
else:
    print('Então podemos prosseguir')

print('\nVAMOS AOS COMBATES!')

print(f'\nLuta entre {lutador_1.nome} e {lutador_2.nome}:')
luta1 = Luta(lutador_1, lutador_2)
luta1.lutar()
print(f'\nLuta entre {lutador_1.nome} e {lutador_3.nome}:')
luta2 = Luta(lutador_1, lutador_3)
luta2.lutar()
print(f'\nLuta entre {lutador_2.nome} e {lutador_3.nome}:')
luta3 = Luta(lutador_2, lutador_3)
luta3.lutar()

print('\nAO FINAL DE TODOS OS CONFRONTOS:')
print(f'Historia de Vitórias x Derrotas do {lutador_1.nome}: {lutador_1.n_vitorias} x {lutador_1.n_derrotas}')
print(f'Historia de Vitórias x Derrotas do {lutador_2.nome}: {lutador_2.n_vitorias} x {lutador_2.n_derrotas}')
print(f'Historia de Vitórias x Derrotas do {lutador_3.nome}: {lutador_3.n_vitorias} x {lutador_3.n_derrotas}')
