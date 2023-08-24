while True:
    try:
        vitórias = int(input("Quantas vitórias deseja atribuir ao Herói? "))
        break
    except ValueError:
        print("Valor inválido.")

while True:
    try:
        derrotas = int(input("Quantas derrotas deseja atribuir ao Herói? "))
        break
    except ValueError:
        print("Valor inválido.")

def calc(valor1, valor2):
    return valor1 - valor2

total = calc(vitórias, derrotas)

print(total)

if total < 10:
    lvl = "ferro"
if 11 <= total <= 20:
    lvl = "bronze"
if 21 <= total <=50:
    lvl = "prata"
if 51 <= total <= 80:
    lvl = "ouro"
if 81 <= total <= 90:
    lvl = "diamante"
if 91 <= total <= 100:
    lvl = "lendário"
if 101 <= total:
    lvl = "imortal"

print(f"O Herói tem de saldo de {total} está no nível de {lvl}")



