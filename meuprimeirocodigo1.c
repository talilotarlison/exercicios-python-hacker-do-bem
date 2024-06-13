;// codigo do programa em liguagem C
#include <stdio.h>
#include <string.h>
int main (int argc, char const *argv[])
{
	char nome[50];
	char endereco[60];
	char telefone[14];
	printf("Digite seu nome:\n");
	fgets(nome,50,stdin);
	printf("Digite seu endereco:\n");
	fgets(endereco,60,stdin);
	printf("Digite seu telefone:\n");
	fgets(telefone,14,stdin);
	printf("Nome: %s\n", nome);
	printf("Endereco: %s\n",endereco);
	printf("Telefone: %s",telefone);

}

//segunda opção do codigo:

#include <stdio.h>
#include <string.h>
int main (int argc, char const *argv[])
{
	char nome[50];
	char endereco[60];
	char telefone[14];
	printf("digite o nome:\n");
	fgets(nome,50,stdin);
	printf("digite o endereco:\n");
	fgets(endereco,60,stdin);
	printf("digite o telefone:\n");
	fgets(telefone,14,stdin);
	printf("Nome: %s\nEndereco: %s\nTelefone: %s",nome,endereco,telefone);
}