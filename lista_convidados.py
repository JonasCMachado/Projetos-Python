import os

print("LISTA DE CONVIDADOS")
print()

# Funções de interação com o usuário, para facilitar a escrita do código.
def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)
    print()

def finalizar_programa():
    exibir_subtitulo('Finalizando o programa...')

# Função para ler número inteiro, evitando a inserção de qualquer outra tecla senão algarismos.
def ler_numero_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Opção inválida! Por favor, digite um número inteiro.\n")

# Função que impossibilita a inserção de um texto nulo pelo usuário .
def ler_nome (mensagem):
  while True:
    nome = input(mensagem).strip()
    
    if nome == "":
      print("O nome não pode estar em branco!")
    else:
      return nome

# Função que permite somente a entrada das letras exigidas.
def ler_letra(mensagem):
    while True:
        try:
            resposta = input(mensagem).strip().lower()
            if resposta != 's' and resposta != 'n':
                raise ValueError
            return resposta 
        except ValueError:
            print("Opção inválida! Digite apenas 's' ou 'n'.\n")

# Variável criada com o intuito de finalizar o programa caso o usuário não queira continuar.
deve_continuar = True

while True:
    quantidade_maxima = ler_numero_inteiro("Qual é o máximo de pessoas na festa: ")
    quantidade_convidados = ler_numero_inteiro("Quantos convidados terão na festa: ")

    # Estrutura de repetição usada para verificar se a quantidade máxima de convidados está sendo atendida.
    if quantidade_convidados <= quantidade_maxima:
        print("A quantidade de convidados está dentro do limite!")
        break

    else:
        print("A quantidade de convidados está acima do limite!\n")
        continuar = ler_letra(
            "Caso deseje continuar, digite 's'.\n"
            "Caso deseje encerrar, digite 'n': "
        )

        if continuar == "s":
            continue
        else:
            exibir_subtitulo("Até a próxima")
            finalizar_programa()
            deve_continuar = False
            break 

# Lista para armazenar os convidados inseridos
lista_convidados = []
convidados = 0

# Repetição usada para ser ativada apenas se o usuário aceitar continuar caso tenha violado a quantidade máxima.
while deve_continuar and (convidados < quantidade_convidados):

    numero = convidados + 1

    nome_convidado = ler_nome(f"Digite o nome do convidado {numero}: ")
    idade_convidado = ler_numero_inteiro(f"Digite a idade do convidado {numero}: ")

    # Verificação de idade para evitar a entrada de menores de idade
    if idade_convidado < 18:
        print(f"O convidado {numero} não pode entrar na festa por ser menor de idade!\n")

        continuar2 = ler_letra(
            "Deseja adicionar outro convidado no lugar dele? (s/n) "
        )

        if continuar2 == "s":
            print("Certo, digite os dados do substituto a seguir:\n")
            continue

        else:
            quantidade_convidados -= 1
            print(f"A quantidade de convidados agora é {quantidade_convidados}")
            continue
    
    # Adiciona os dados puros (nome e idade) como uma lista dentro da lista.
    lista_convidados.append([nome_convidado, idade_convidado])

    convidados += 1

# Verifica se a quantidade de convidados na lista é maior que 0.
if len(lista_convidados) > 0:
    print("\n--- LISTA FINAL DE CONVIDADOS ---\n")
    
    maior_tamanho = max(len(convidado[0]) for convidado in lista_convidados)
    largura = max(maior_tamanho, 15)
    
    # Percorre a lista exibindo os dados alinhados de forma organizada.
    for i, convidado in enumerate(lista_convidados, start=1):
        nome = convidado[0]
        idade = convidado[1]
        print(f"{i} - {nome:<{largura}} | {idade} anos")

# Uso do elif para evitar que a mensagem seja apresentada logo no início.       
elif deve_continuar:
    print("\nNenhum convidado cadastrado.")
