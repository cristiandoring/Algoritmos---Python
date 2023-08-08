peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m):'))

imc = peso/(altura**2)

if peso < 0 or altura <0:
    print('Dados inválidos!')
else:
    print('O IMC é {:.2f}.'.format(imc))
    
    if imc > 0 and imc <= 18.5:
        print('ABAIXO')
    elif imc > 18.5 and imc <=25:
        print('NORMAL')
    elif imc > 25 and imc <=30:
        print('SOBREPESO')
    elif imc > 30 and imc <=40:
        print('OBESIDADE')
    else:
        print('OBESIDADE MÓRBIDA')


