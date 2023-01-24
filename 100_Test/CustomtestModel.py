#import pandas as pd

class CustomtestModel:
    def __init__(self, inputfile=""):
        #self.sheet = pd.ExcelFile(inputfile)
        self.sheet = inputfile        
        # df = pd.read_excel(self.sheet, sheet_name = "Sheet1", header = None)
        # df2 = pd.DataFrame({'data' : [10, 100, 1000]})
        # writer = pd.ExcelWriter(self.sheet)
        # df.to_excel(writer, header=None, index=None)
        # df2.to_excel(writer, startcol = 5, startrow = 5, header=None, index=False)
        # writer.save()
        
    def getjson(self):
        #df = pd.DataFrame({"testdata" : [100], "realdata" : [200]})
        response = {
            "test" : {"testdata" : [101], "realdata" : [201]}
        }        
        return response