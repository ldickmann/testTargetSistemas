# Teste de Lógica Target Sistemas

"""1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

indice = 13
soma = 0
k = 0

while k < indice:
	k += 1
	soma += k

print(soma)

print('####################################################################')

"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência."""


def fibonacci(n):
	a, b = 0, 1
	while a <= n:
		if a == n:
			return True
		a, b = b, a + b
	return False


num = int(input('Digite um número: '))

if fibonacci(num):
	print(f'O número digitado {num} faz parte da sequência de Fibonacci.')
else:
	print(f'O número digitado {num} não faz parte da sequência de Fibonacci.')

print('####################################################################')

"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;"""


import json


def calc_faturamento(lista):
	faturamentos = [dia['valor'] for dia in lista['faturamento-diario'] if dia['valor'] >= 0]
	
	min_faturamento = min(faturamentos)
	max_faturamento = max(faturamentos)
	media = sum(faturamentos) / len(faturamentos)
	
	dias_acima_media_fat = len([dia for dia in faturamentos if dia > media])
	
	return min_faturamento, max_faturamento, dias_acima_media_fat


with open('faturamento.json', 'r') as file:
	faturamento_lista = json.load(file)
	
menor_faturamento, maior_faturamento, dias_acima_media_fat = calc_faturamento(faturamento_lista)

print(f'O menor valor de faturamento ocorrido na distribuidora foi R$: {menor_faturamento}')
print(f'Maior valor de faturamento da distribuidora for de R$: {maior_faturamento}')
print(f'Dias com faturamento acima da média: {dias_acima_media_fat}')

print('####################################################################')


"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve
dentro do valor total mensal da distribuidora."""

faturamento = {
	'SP': 67836.43,
	'RJ': 36678.66,
	'MG': 29229.88,
	'ES': 27165.48,
	'Outros': 19849.53
}

fat_total = sum(faturamento.values())

for estado, valor in faturamento.items():
	percentual = (valor / fat_total) * 100
	print(f'O estado {estado} obteve um percentual de {percentual:.2f}% do faturamento total da distribuidora.')

print('####################################################################')

"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""


def inverter_string(s):
	pilha = []
	
	for char in s:
		pilha.append(char)
		
	string_invertida = ""
	while pilha:
		string_invertida += pilha.pop()
	
	return string_invertida


if __name__ == "__main__":
	entrada = input("Digite uma string para inverter: ")
	resultado = inverter_string(entrada)
	print("String invertida:", resultado)
