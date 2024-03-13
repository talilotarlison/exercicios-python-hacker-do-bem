# programa calcular imc
print('#'*40)
print("Calcule seu IMC agora!!")
peso = float(input("Qual seu peso?\n"))
altura = float(input("Qual sua altura?\n"))
print('#'*40)

imc = peso/(altura*altura)
print(f'Seu IMC é: {imc:0.2f} .')
print('Fim do programa')
