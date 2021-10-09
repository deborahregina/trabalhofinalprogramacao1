fraselida = input('Digite uma frase: ')

result = fraselida.upper();

result1 = result.replace('A','@')
result2 = result1.replace('E','&')
result3 = result2.replace('I','!')
result4 = result3.replace('O','#')
result5 = result4.replace('U','*')

print(result5)
