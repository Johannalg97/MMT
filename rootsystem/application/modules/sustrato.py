
class Sustrato(object):
    
    def __init__(self):
        self.sustrato_id = 0
        self.n = ""
        self.k = ""
    
    def insert(self):
        pass
    
    def select(self):
        pass
        
        
class SustratoView(object):
    pass
    

class SustratoController(object):
    
    def __init__(self):
        self.model = Sustrato()
        self.view = SustratoView()
