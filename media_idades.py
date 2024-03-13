
# programa calcular media dinamica das idades com for

print('#'*40)
print("Calcule sua Média Dinamica das idades!!")
print('#'*40)

# idades
idades = [10,10,20,50]

# sua media de idades
idadeTotal = 0


# for com as notas

for i in range(len(idades)):
  idadeTotal += idades[i]
  
# media das notas

media = idadeTotal / len(idades)
  
print(f'Media final das idades é: {media:0.0f} anos')

print('Fim do programa')
