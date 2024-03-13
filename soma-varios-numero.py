# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

valorEntrada = 0
soma = incremento = 0
while valorEntrada != 99:
      entradaUsuario = int(input("digite um número: [digite 99 para cancela]"))
      valorEntrada = entradaUsuario
      if entradaUsuario != 99:
         incremento = incremento +1
         soma = soma + entradaUsuario
print("fim!")
print(f"Você adicionou {incremento} números e a soma é {soma}")
