
# programa calcular media dinamica das notas com for

print('#'*40)
print("Calcule sua Média Dinamica agora!!")
print('#'*40)

# suas notas
notas = [10,10,10]

# sua media
notaTotal = 0


# for com as notas

for nota in notas:
  notaTotal += nota
  
# media das notas

media = notaTotal / len(notas)
  
print(f'Sua media final é: {media:0.2f}')

def calcularMediaStatus(notaMedia):
  if(notaMedia>=9):
    print(f' A => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
  elif(notaMedia<9 and notaMedia>=8):
    print(f' B => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
  elif(notaMedia<8 and notaMedia>=7):
    print(f' C => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
  elif(notaMedia<7 and notaMedia>=6):
    print(f' D => Você esta aprovado, sua nota é: {notaMedia:0.2f}!')
  else:
    print(f'E => Você esta reprovado,  sua nota é: {notaMedia:0.2f}!')
    
calcularMediaStatus(media)
  
print('Fim do programa')



