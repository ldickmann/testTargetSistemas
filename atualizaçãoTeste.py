# Atualização do teste, devido o recebimento do arquivo dados.json após já ter finalizado o teste.

import json


def calc_fatura(lista):
	faturam = [dia['valor'] for dia in lista if dia['valor'] >= 0]
	
	min_faturamento = min(faturam)
	max_faturamento = max(faturam)
	media = sum(faturam) / len(faturam)
	
	dias_media_acima_fat = len([dia for dia in faturam if dia > media])
	
	return min_faturamento, max_faturamento, dias_media_acima_fat


with open('dados.json', 'r') as file:
	faturam_lista = json.load(file)

min_faturamento, max_faturamento, dias_media_acima_fat = calc_fatura(faturam_lista)

print(f'O menor valor de faturamento ocorrido na distribuidora foi R$: {min_faturamento}')
print(f'Maior valor de faturamento da distribuidora for de R$: {max_faturamento}')
print(f'Dias com faturamento acima da média: {dias_media_acima_fat}')
