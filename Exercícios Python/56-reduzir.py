# reduce() = aplica a função escolhida com os 2 primeiros elementos, e assim sucessivamente, até sobrar apenas 1 valor.

import functools

letras = ["O", "R", "A", "N", "G", "O", "T", "A", "N", "G", "O"]

palavra = functools.reduce(lambda a, b,:a + b, letras)

print(palavra)

fatorial = [4, 3, 4, 3, 3, 2]

resultado = functools.reduce(lambda a, b: a * b, fatorial)

print(resultado)