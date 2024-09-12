from django.test import TestCase

# Create your tests here.
nome = 'luiz cenci'
sobrenome = nome.split()
idx = len(sobrenome)
print(sobrenome.count('cenci'))