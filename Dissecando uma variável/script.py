texto = input('Digite algo: ')

tipo = type(texto)
espaco = texto.isspace()
numero = texto.isnumeric()
alfanumerico = texto.isalnum()
alfabetico = texto.isalpha()
maiuscula = texto.isupper()
minuscula = texto.islower()
capitalizada = texto.istitle()


print('O tipo primitivo é {}!'.format(tipo))
print('Só tem espaços?',espaco)
print('É um número?',numero)
print('É alfanumérico?',alfanumerico)
print('É alfabético?',alfabetico)
print('Está em maísculas?',maiuscula)
print('Está em minúsculas?',minuscula)
print('Ésta capitalizada?',capitalizada)