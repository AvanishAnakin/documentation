from sys import modules
from .ClassGenerator import ClassGenerator
from .services import sum

# Export the ClassGenerator class
modules['__all__'] = ['ClassGenerator', 'sum']
modules['name'] = 'ClassGenerator'
modules['author'] = 'Avanish Gupta'