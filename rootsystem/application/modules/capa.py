

class Capa(object):
    
    def __init__(self):
        self.capa_id = 0
        self.matriz = 0
        self.n = ""
        self.k = ""
        self.espesor = ""
    
    def insert(self):
        pass
    
    def select(self):
        pass
        
        
class CapaView(object):
    pass
    

class CapaController(object):
    
    def __init__(self):
        self.model = Capa()
        self.view = CapaView()
        
