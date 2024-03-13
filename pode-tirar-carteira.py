# programa se pode tirar carteira
print('#'*40)
print("Pode tirara carteira?")
idade = int(input('Qual sua idade?\n'))
print('#'*40)


if (idade >=18):
  print(f'Sua idade é {idade} anos, e você pode tirar carteira!')
else:
  print(f'Sua idade é {idade} anos, e você não pode tirar carteira!')
  
print('Fim do programa')

# programa se pode dirigir
print('#'*40)

print("Pode dirigir?")
print('#'*40)


if (idade >=18):
  print(f'Sua idade é {idade} anos, e você pode dirigir!')
else:
  print(f'Sua idade é {idade} anos, e você não pode dirigir!')
  
print('Fim do programa')
