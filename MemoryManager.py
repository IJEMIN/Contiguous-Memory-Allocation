import Memory
import Process

class MemoryManager:
    mainMemory = Memory.Memory(256)
    
    #Process Object Container
    processList = []
    
    #Free Memory Partition Container
    # KEY: PARTITION START ADDRESS, VALUE: PATITION SIZE
    freePartitionList = {}
    
    def __init__(self):
        self.freePartitionList = {0:self.mainMemory.memSize}
    
    
    #Merge and Update Free Partition Information Dictionary
    def UpdateFreePartitionList(self):
        self.freePartitionList.clear()
        if len(self.processList) == 0:
            self.freePartitionList = {0:self.mainMemory.memSize}
            return
        
        
        i=0
        while (i < self.mainMemory.memSize):
            #if pointer if after pTail or first position of empty space
            if self.mainMemory.memID[i] == Memory.Memory.EMPTY:
                for j in range (i,self.mainMemory.memSize):
                    #if last space is empty.
                    if j == self.mainMemory.memSize-1:
                        self.freePartitionList[i] = (j-i+1)
                        i = j+1
                        
                        break
                    
                    if self.mainMemory.memID[j] != Memory.Memory.EMPTY:
                        #add new Partition Information
                        #i= partition head, j-i = partition size
                        self.freePartitionList[i] = (j-i+1)
                        
                        #Jump to new check Position
                        i = j+1
                        break
            i+=1

    def AllocateNewProcessByFirstFit(self,memoryRequired):
        
        #check free partition
        for k,v in self.freePartitionList.items():
            if v> memoryRequired:
                newProcess = Process.Process(len(self.processList),k,memoryRequired)
                newProcess.allocate(self.mainMemory)
                self.processList.append(newProcess)
                return True
            
        return False
        
        
        '''
        #this is worst way to check every empty space.
        #YOU CAN modify Algorithm to CHECK ONLY pHead, pTail to find empty space
        for i in range (0,self.mainMemory.memSize):
            
            # Not enough space
            if i == self.mainMemory.memSize - memoryRequired:
                return False
            
            if self.mainMemory.memID[i] ==  Memory.Memory.EMPTY:
                for j in range (i,i+memoryRequired):
                    if self.mainMemory.memID[j] != Memory.Memory.EMPTY:
                        return False
                #if space from i to i + processRequire is Empty
                newProcess = Process.Process(len(self.processList),i,memoryRequired)
                newProcess.allocate(self.mainMemory)
                self.processList.append(newProcess)
                return True
            
        return False
        '''
    def AllocateNewProcessByWorstFit(self,memoryRequired):
        
        partitionAddress = 0
        partitionSize = 0
        for k,v in self.freePartitionList.items():
            #import biggest Partition Size, address.
            if partitionSize < v:
                partitionSize = v
                partitionAddress = k
            
        if partitionSize < memoryRequired:
            return False
        
        
        newProcess = Process.Process(len(self.processList),partitionAddress,memoryRequired)
        newProcess.allocate(self.mainMemory)
        self.processList.append(newProcess)
        return True
    
    def AllocateNewProcessByBestFit(self,memoryRequired):
        
        partitionSize = 256
        partitionAddress = 0
        
        for k,v in self.freePartitionList.items():
            #import biggest Partition Size, address.
            
            if partitionSize > v and v >= memoryRequired:
                partitionSize = v
                partitionAddress = k
            
        if partitionSize < memoryRequired:
            return False
        
        
        newProcess = Process.Process(len(self.processList),partitionAddress,memoryRequired)
        newProcess.allocate(self.mainMemory)
        self.processList.append(newProcess)
        return True
    
    def ReleaseMemory(self,processName):
        for i in range(0,len(self.processList)):
            if self.processList[i].name == processName:
                self.processList[i].release(self.mainMemory)
                return True
        return False
    
    def CompactMemory(self):
        
        self.processList.sort(reverse = True)
        
        #moving Process to Upside
        for i in range (0, len(self.processList)):
            
            currentProcess = self.processList[i]
            
            '''
            #if process is already on top
            if currentProcess.address == 0:
                break
            '''
            
            tmpAddress = currentProcess.address
            
            #move process address until meeting tail of other process
            while(1):
                if self.mainMemory.memID[tmpAddress-1] == Memory.Memory.EMPTY and tmpAddress != 0:
                    tmpAddress = tmpAddress -1
                else:
                    break
            
            #move to Upside
            self.mainMemory.MoveProcess(currentProcess, tmpAddress)                  
            
            '''
            while(1):
                if self.mainMemory.memID[currentProcess-1] == Memory.Memory.EMPTY and currentProcess.address != 0:
                    currentProcess.release(self.mainMemory)
                    #move to upside
                    currentProcess.address -= 1
                    currentProcess.allocate(self.mainMemory)
            '''