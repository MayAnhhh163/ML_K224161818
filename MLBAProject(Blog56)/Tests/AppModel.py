'''test tiền xử lý và transformation'''

from Connectors.Connector import Connector
from Models.PurchaseMLModel import PurchaseMLModel

connector=Connector(server="localhost",port=3306,database="lecturer_retails",username="root",password="1234")
connector.connect()
pm=PurchaseMLModel(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)