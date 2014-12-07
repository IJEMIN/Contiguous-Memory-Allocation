import MemoryManager
import sys, time


from PyQt4.QtGui import*
from PyQt4.QtCore import*

from ui import Ui_MainWindow

class MyForm(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uiMemoryManager = MemoryManager.MemoryManager()
        self.uiMemoryManager.UpdateFreePartitionList()
    
    def compactingClicked(self):
        self.uiMemoryManager.CompactMemory()
        self.uiMemoryManager.UpdateFreePartitionList()
        
        freeMemoryInfo = str(self.uiMemoryManager.freePartitionList)
        a = "Address of Free Partition: Size of Free Partition - "
        qStringContainer = QString( a + freeMemoryInfo)
        
        self.ui.FreePartitionInfo.clear()
        self.ui.FreePartitionInfo.setPlainText(qStringContainer)
        
        
        
        processInfoContainer = ""
        
        for i in range (0,len(self.uiMemoryManager.processList)):
            processInfoContainer += self.uiMemoryManager.processList[i].exportProcessInfo()
            
        qStringContainer = QString(processInfoContainer)
        self.ui.ProcessListDisplay.clear()
        self.ui.ProcessListDisplay.setPlainText(qStringContainer)
        
            
            

    def releasingClicked(self):
        
        processNumber = self.ui.lineEdit.text().toInt()[0]
        
        self.uiMemoryManager.ReleaseMemory(processNumber)
        self.uiMemoryManager.UpdateFreePartitionList()
        
        freeMemoryInfo = str(self.uiMemoryManager.freePartitionList)
        a = "Address of Free Partition: Size of Free Partition - "
        qStringContainer = QString( a + freeMemoryInfo)
        
        
        
        
        self.ui.FreePartitionInfo.clear()
        self.ui.FreePartitionInfo.setPlainText(qStringContainer)
        
        processInfoContainer = ""
        
        for i in range (0,len(self.uiMemoryManager.processList)):
            processInfoContainer += self.uiMemoryManager.processList[i].exportProcessInfo()
            
        qStringContainer = QString(processInfoContainer)
        self.ui.ProcessListDisplay.clear()
        self.ui.ProcessListDisplay.setPlainText(qStringContainer)
        
        
        




    def worstClicked(self):
        
        self.uiMemoryManager.UpdateFreePartitionList()
        
        processMemory = self.ui.MemoryInput.text().toInt()[0]
        
        self.uiMemoryManager.AllocateNewProcessByWorstFit(processMemory)
        
        self.uiMemoryManager.UpdateFreePartitionList()
        
        
        freeMemoryInfo = str(self.uiMemoryManager.freePartitionList)
        a = "Address of Free Partition: Size of Free Partition - "
        qStringContainer = QString( a + freeMemoryInfo)
        
        self.ui.FreePartitionInfo.clear()
        self.ui.FreePartitionInfo.setPlainText(qStringContainer)
        
        
        
        processInfoContainer = ""
        
        for i in range (0,len(self.uiMemoryManager.processList)):
            processInfoContainer += self.uiMemoryManager.processList[i].exportProcessInfo()
            
        qStringContainer = QString(processInfoContainer)
        self.ui.ProcessListDisplay.clear()
        self.ui.ProcessListDisplay.setPlainText(qStringContainer)
        

    def firstClicked(self):

        self.uiMemoryManager.UpdateFreePartitionList()
        processMemory = self.ui.MemoryInput.text().toInt()[0]
        
        self.uiMemoryManager.AllocateNewProcessByFirstFit(processMemory)
        
        self.uiMemoryManager.UpdateFreePartitionList()
        freeMemoryInfo = str(self.uiMemoryManager.freePartitionList)
        a = "Address of Free Partition: Size of Free Partition - "
        qStringContainer = QString( a + freeMemoryInfo)
        
        self.ui.FreePartitionInfo.clear()
        self.ui.FreePartitionInfo.setPlainText(qStringContainer)
        
        
        
        processInfoContainer = ""
        
        for i in range (0,len(self.uiMemoryManager.processList)):
            processInfoContainer += self.uiMemoryManager.processList[i].exportProcessInfo()
            
        qStringContainer = QString(processInfoContainer)
        self.ui.ProcessListDisplay.clear()
        self.ui.ProcessListDisplay.setPlainText(qStringContainer)


    def bestClicked(self):
        self.uiMemoryManager.UpdateFreePartitionList()
        processMemory = self.ui.MemoryInput.text().toInt()[0]
        
        self.uiMemoryManager.AllocateNewProcessByBestFit(processMemory)
        
        self.uiMemoryManager.UpdateFreePartitionList()
        freeMemoryInfo = str(self.uiMemoryManager.freePartitionList)
        a = "Address of Free Partition: Size of Free Partition - "
        qStringContainer = QString( a + freeMemoryInfo)
        
        self.ui.FreePartitionInfo.clear()
        self.ui.FreePartitionInfo.setPlainText(qStringContainer)
        
        
        
        processInfoContainer = ""
        
        for i in range (0,len(self.uiMemoryManager.processList)):
            processInfoContainer += self.uiMemoryManager.processList[i].exportProcessInfo()
            
        qStringContainer = QString(processInfoContainer)
        self.ui.ProcessListDisplay.clear()
        self.ui.ProcessListDisplay.setPlainText(qStringContainer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())