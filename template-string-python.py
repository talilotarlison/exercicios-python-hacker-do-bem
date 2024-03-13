# tamplete string com python e entrada de dados
print('#'*40)
print('Cadastro de Usuario:')
print('#'*40)

nome = input('Seu nome?\n')
print(nome)
sobrenome = input('Seu sobrenome?\n')
print(sobrenome)
print('Seu nome completo é : \n%s %s!' %(nome, sobrenome))
idade = input('Sua idade?\n')
print(idade)
print('Sua idade é : \n%i anos' %int(idade))

print('Fim do programa')