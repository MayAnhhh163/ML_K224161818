'''test tiền xử lý và transformation'''

from ML_K224161818.Blog56.Connectors.Connector import Connector
from ML_K224161818.Blog56.Models.PurchaseMLModel import PurchaseMLModel

connector=Connector(server="localhost",port=3306,database="lecturer_retails",username="root",password="1234")
connector.connect()
pm=PurchaseMLModel(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)