# -*- encoding: UTF-8 -*

from tkinter import *

class ClassMaker():
    
    """
    @author: job_he
    """
    ans = ""
    
    def newOne(self,rawData):
        self.ans = ""
        className = rawData["className"]
        rawData = rawData["rawData"]
        for k in rawData.keys():
            self.__addAttribute__(rawData[k],k)
        
        self.__addConstructorFunction__(className,rawData)
        
        for k in rawData.keys():
            self.__addAttrFunction__(rawData[k],k)
        
        self.ans = "class %s{\n%s\n}"%(className,self.ans)
        self.saveClass(className)
        
    def __addAttribute__(self,typeName,attrName):
        self.ans = self.ans + "\t" + typeName + " " + attrName + " = null;\n"
    
    def __addSetFunction__(self,typeName,attrName):
        addition = "\tpublic void set"+attrName[0].upper()+attrName[1:]+"("+ typeName + " "+ attrName +")\n"
        addition += "\t{\n\t\tthis." + attrName + " = "+ attrName + ";\n\t}\n"
        self.ans+=addition
    
    def __addGetFunction__(self,typeName,attrName):
        addition = "\tpublic "+ typeName + " get" + attrName[0].upper() + attrName[1:] + "()\n\t{\n\t\treturn " + attrName + ";\n\t}\n" 
        self.ans+=addition
        
    def __addAttrFunction__(self,typeName,attrName):
        self.__addSetFunction__(typeName,attrName)
        self.__addGetFunction__(typeName,attrName)
    
    def __addConstructorFunction__(self,className,rawData):
        argument_tb = "(" + ",".join([ rawData[k]+" "+k for k in rawData.keys()]) +"){\n"
        functionName = "\tpublic %s"%(className)
        functionName+=argument_tb
        for k in rawData.keys():
            newRow = "\t\tthis.%s = %s;\n"%(k,k)
            functionName+=newRow
            
        functionName+="\t}\n"
        self.ans+=functionName
    
    def saveClass(self,className):
        with open("%s.java"%className,"w") as fp:
            fp.write(self.ans)

        print("Succeed")
             
class ClassMakerWindow():
    
    """
    @author: job_he
    @description: Write less code and create *.java automaticlly.
    """
    
    app = Tk()

    def __init__(self):
        pass
    
if __name__ == "__main__":
    rawData = {
        "className": "Person",
        "rawData": {
            "id":"String",
            "name":"String"
        }
    }
    maker = ClassMaker()
    maker.newOne(rawData)