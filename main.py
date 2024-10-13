def calcular_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas
    
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return saldo, nivel

# Laço de repetição para permitir múltiplos cálculos
while True:
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))

    saldo, nivel = calcular_nivel(vitorias, derrotas)

    print(f"O Herói tem de saldo {saldo} está no nível {nivel}")
    
    continuar = input("Deseja calcular para outro jogador? (s/n): ")
    if continuar.lower() != 's':
        break

print("Programa encerrado. Obrigado por usar a Calculadora de Partidas Rankeadas!")