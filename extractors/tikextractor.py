from extractors.extractor import ExtractorInterface
import os
from config import ExtractorConfig
import tika
from tika import parser


class TIKExtractor(ExtractorInterface):
    
    def __init__(self,config=None):
        if config == None:
           config = ExtractorConfig() 
        tika.initVM()

    def extract(self, fileobject):
        parsed = parser.from_file(fileobject)
        listOfPara=self.splitInfoPara(parsed["content"])
        return listOfPara

    def splitIntoPara(self, content):
        listOfPara=[]
        listOfSections=[]
        counter=1
        splitContent=content.split("\n")
        for para in splitContent:
            listOfPara.append(para)
            listOfSections.append(counter)
            counter+=1
        return listOfPara, listOfSections

if __name__=="__main__":
    myextractor = TIKExtractor()
    content=myextractor.extract(open('test.pdf'))	
    print("Test content:\n",content)
