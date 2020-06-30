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
        print(str(parsed["content"]).strip())
        return (self.splitIntoPara(str(parsed["content"]).strip()))
   
    def splitIntoPara(self,mystring):
        return mystring.split("\n\n")

if __name__=="__main__":
    myextractor = TIKExtractor()
    content=myextractor.extract(open('test.pdf'))	
    print("Test content:\n",content)
