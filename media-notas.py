# programa calcular media notas

print('#'*40)
print("Calcule sua Média agora!!")
nota1 = float(input("Qual sua nota 1?\n"))
nota2 = float(input("Qual sua nota 2?\n"))
nota3 = float(input("Qual sua nota 3?\n"))
print('#'*40)

notaMedia = (nota1+nota2+nota3)/3

if(notaMedia<=10 and notaMedia>=9):
  print(f' A => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
elif(notaMedia<9 and notaMedia>=8):
  print(f' B => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
elif(notaMedia<8 and notaMedia>=7):
  print(f' C => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
elif(notaMedia<7 and notaMedia>=6):
  print(f' D => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
else:
  print(f'E => Você esta reprovado,  sua nota é: {notaMedia:0.2f}!')

print('Fim do programa')

