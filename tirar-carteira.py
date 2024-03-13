# programa se pode tirar carteira
print('#'*40)
print("Tire sua carteira agora!!")
maiorIdade = input("Você é maior de idade? Responda S/N?\n")
idade = int(input("Qual sua idade?\n"))
anoAtual = 2024
print('#'*40)

if ( maiorIdade.lower() == 's' and idade >= 18):
  print(f'Sua idade é {idade} anos, você nasceu em {(anoAtual-idade)}, e você pode tirar carteira!')
elif ( maiorIdade.lower() == 'n' and idade < 18):
  print(f'Sua idade é {idade} anos,você nasceu em {(anoAtual-idade)} e você só pode tirar carteira daqui a {(18-idade)} anos!')
else:
  print('Dados incorretos, tente novamente!')
  
print('Fim do programa')
