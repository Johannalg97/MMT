
class Host(object):
    
    def __init__(self):
        self.host_id = 0
        self.n = ""
        self.k = ""
    
    def insert(self):
        pass
    
    def select(self):
        pass

class HostView(object):
    pass
    

class HostController(object):
    
    def __init__(self):
        self.model = Host()
        self.view = HostView()
        

