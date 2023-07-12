class Livro:
    def __init__(self, titulo, autor, publi):
        self.__titulo = titulo
        self.__autor = autor 
        self.__publi = publi

    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, novo_autor):
        self.__autor = novo_autor

    def getPubli(self):
        return self.__publi
    
    def setPubli(self, novo_publi):
        self.__publi = novo_publi
        
    
    