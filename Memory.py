class Memory:
    EMPTY = "EMPTY"
    
    memID = []
    def __init__(self,memSize):
        self.memSize = memSize
        for i in range(0,memSize):
            self.memID.append(self.EMPTY)
    
    def AllocateProcess(self,allocatedProcess):
        allocatedProcess.allocate(self)
        
    def ReleaseProcess(self,releasedProcess):
        releasedProcess.release(self)
    
    
    
    def MoveProcess(self,movingProcess,arrivalPoint):
        """MOVING PROCESS TO arrivalPoint"""
        #temporary releasing for moving
        movingProcess.release(self)
        
        #change head address of process
        movingProcess.address = arrivalPoint
        
        movingProcess.allocate(self)
        
        
        