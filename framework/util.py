import xlrd
from framework.logger import Logger

logger=Logger("logger=Util").getlog()
class Util(object):
    @classmethod
    def read_excel(self,excel_path,sheetName="Sheet"):
        workbook=xlrd.open_workbook(excel_path)
        sheet=workbook.sheet_by_name(sheetName)
        keys=sheet.row_values(0)
        rowNum=sheet.nrows
        cloNum=sheet.ncols

        if rowNum<=1:
            logger.error("excel表中总行数少于一行")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
        return  r
if __name__=="__main__":
    filepath="data.xlsx"
    print(Util.read_excel("H:/python-webUI-auto/data/data.xlsx", "Sheet1"))