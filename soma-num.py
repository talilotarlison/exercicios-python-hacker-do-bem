print("Vamos tirar a media de duas notas!")
nota1 = int(input("Digite sua primeira nota!"))
nota2 = int(input("Digite sua segunda nota!"))
media = (nota1 + nota2)/ 2

print("Sua media final foi {}" .format(media))

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
