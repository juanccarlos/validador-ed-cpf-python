import re
import sys

entrada =  input('digite um cpf: ').replace('.', '').replace('-', '')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)
digitos_cpf = cpf[:9]
contador = 10
soma = 0

if cpf == cpf[0] * len(cpf):
    print('valores repetidos não forma um cpf válido !')
    sys.exit()


for digito in digitos_cpf:
     soma += int(digito ) * contador
     contador -= 1

primeiro_digito = (soma * 10) % 11

if primeiro_digito > 9 :
    primeiro_digito = 0

contador = 11
digitos_cpf = cpf[:9] + str(primeiro_digito)

for digito in digitos_cpf:
     soma += int(digito ) * contador
     contador -= 1

segundo_digito = (soma * 10) % 11

if segundo_digito > 9 :
    segundo_digito = 0

if str(segundo_digito) in cpf[10] and str(primeiro_digito) in cpf[9]:
    print('o cpf {} é valido !'.format(cpf))

else:
    print('o cpf {} não é valido !'.format(cpf))
