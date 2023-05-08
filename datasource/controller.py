from .window import Window
from .data import getCo2Data

class Co2Controller:
    def __init__(self):
        self.co2Data = getCo2Data()
        self.window = Window(callback=self.callback,co2Data=self.co2Data)
        self.output_view = self.window
        self.output_view.title(" 全球 CO2資料 ")
    def run(self):
        self.window.mainloop()

    def callback(self):  # 給視窗執行的回呼
        # 讀取資料
        co2Lst = getCo2Data()
        # 建立 資料模型 model
        self.co2Data = co2Lst
        # 輸出結果 output_view  更新畫面
        self.output_view.bottomRootFrame.destroy()
        self.output_view.designLabel.destroy()
        self.output_view.createDisplayFrame(self.co2Data)



