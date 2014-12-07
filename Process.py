import Memory

#process which consume memory at memory stack. Only released by release method.

class Process:
    HEAD = "pHEAD"
    TAIL = "pTAIL"
    
    
    def __init__(self,name,address,required):
        #name:: process ID
        #address:: start position at memory
        #allocated:: total memory allocated at stack
        #require:: total memory required
        self.name = name
        self.address = address
        self.required = required
        self.allocated = 0
    
    
    def release(self,mem):
        endPosition = self.address+self.allocated
        
        
        for i in range(self.address,endPosition-1):
            mem.memID[i] = Memory.Memory.EMPTY
        
        self.allocated = 0
        
    
    
    #allocate self to memory. call by memory class
    def allocate(self,mem):
        endPosition = self.address+self.required
        
        #allocating
        for i in range(self.address,endPosition-1):
            mem.memID[i] = self.name
            
            
        #signing for easy finding
        mem.memID[self.address] = self.HEAD
        mem.memID[endPosition-1] = self.TAIL
        
        self.allocated = self.required
        
    #operator overloading
    def __lt__(self,other):
        if self.address < other.address:
            return True
        return False
    
    def __le__(self,other):
        if self.address <= other.address:
            return True
        return False