import os

from HousingPricePrediction.conding_pyqt6.HousingPricePredictonMainWindow import Ui_MainWindow


class HousingPricePredictionMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.populate_comboBox()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonPredict.clicked.connect(self.process_predict_housepricing)

    def process_predict_housepricing(self):
        AreaIncome = float(self.lineEditAreaIncome.text())
        AreaHouseAge = float(self.lineEditAreaHouseAge.text())
        AreaNumberOfRooms = float(self.lineEditNumberOfRooms.text())
        AreaNumberOfBedrooms = float(self.lineEditNumberOfBedrooms.text())
        AreaPopulation = float(self.lineEditPopulation.text())

        import pickle
        # chạy mô hình
        modelname = "../trainedmodel/housingmodel.zip"

        if self.comboBoxTrainedModel.currentIndex()!=-1:
            modelname=f"../trainedmodel/{self.comboBoxTrainedModel.currentText()}"

        trainedmodel = pickle.load(open(modelname, 'rb'))
        prediction = trainedmodel.predict([[AreaIncome, AreaHouseAge, AreaNumberOfRooms, AreaNumberOfBedrooms, AreaPopulation]])
        print("kết quả =", prediction)
        self.lineEditHousePrice.setText(f'{prediction[0]}')

    def populate_comboBox(self):
        model_dir = "../trainedmodel"
        if os.path.exists(model_dir):  # Kiểm tra thư mục có tồn tại không
            models = sorted(set(f for f in os.listdir(model_dir) if f.endswith(".zip")))  # Loại bỏ trùng lặp và sắp xếp
            self.comboBoxTrainedModel.clear()  # Xóa danh sách cũ để tránh bị trùng lặp
            self.comboBoxTrainedModel.addItems(models)  # Thêm danh sách mới vào combobox

