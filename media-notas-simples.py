# programa calcular media simple
print('#'*40)
print("Calcule sua Média agora!!")
notaMedia = float(input("Qual media de suas notas?\n"))
print('#'*40)

if(notaMedia>=6):
  print(f'Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
else:
  print(f'Você esta reprovado,  sua nota é: {notaMedia:0.2f}!')

print('Fim do programa')
