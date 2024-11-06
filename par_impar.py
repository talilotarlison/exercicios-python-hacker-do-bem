continuar = input("Deseja continuar S/N?")

while(continuar == "S" or continuar == "s"):
  entrada = int(input("Digite um numero?"))
  
  if((entrada%2)==0):
    print("Numero {} par!".format(entrada))
  else:
     print("Numero {} impar!".format(entrada))
     
  continuar = input("Deseja continuar S/N?")
print("Fim do programa!")
