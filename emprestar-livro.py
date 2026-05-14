"""Apresenta os livros e suas disponibilidade

output: Lista de livros"""

class Livro:
    livros = []

    def __init__(self, titulo, autor, publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._publicacao = publicacao
        self._disponibilidade = True

    def __str__(self):
        return f'\n => {self._titulo} de {self._autor} publicado em {self._publicacao} - Disponivel = {self._disponibilidade}'
    
    def emprestar_livro(self):
        self._disponibilidade = False
        
            
livro1 = Livro('Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', 2008)            
livro2 = Livro('Python Fluente: Programação Clara, Concisa e Eficaz', 'Luciano Ramalho', 2015)            
livro3 = Livro('O Codificador Limpo: Um Código de Conduta para Programadores Profissionais', 'robert c. martin', 2011)            
livro4 = Livro('Entendendo Algoritmos: Um Guia Ilustrado para Programadores e Outros Curiosos', 'Aditya Bhargava', 2017)            
livro2.emprestar_livro()
livro4.emprestar_livro()

print(livro1)        
print(livro2)        
print(livro3)        
print(livro4)        