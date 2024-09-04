#! /usr/bin/env python

""" Hello World Multi Linguas. 
Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.
"""

# This program prints Hello World

__version__ = '0.0.1'
__name__ = "Thaina Helena"


import os

current_lang = os.getenv('LANG', 'en_US')[:5]
msg = 'Hello, World!'

if current_lang == 'pt_BR':
  msg = 'Olá, Mundo!'
elif current_lang == 'it_IT':
  msg = 'Ciao, Mondo!'
elif current_lang == 'es_SP':
  msg = 'Hola, Mundo!'

print(msg)