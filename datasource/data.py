# data.py 就是自訂的 module
# 全球COVID-19累積病例數與死亡數 的 csv檔, 線上下載
from .Co2Info import Co2Info

FILENAME = 'co2data.csv'
co2Data = None

'''def downloadCo2DataFromPlatForm():
    '''
    #從開放平台下載全球Co2的資料
'''
    import requests
    downloadURL = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
    response = requests.get(downloadURL, stream=True)
    response.encoding = 'utf-8'
    # 檢查是否下載正常
    if response.status_code != 200:
        return

    with open(FILENAME, 'wb') as fileObj:
        # 寫入檔案
        for chunk in response.iter_content(chunk_size=128):
            # print('chunk =', chunk)
            fileObj.write(chunk)
'''


def readAndParseCSVFile():
    '''
    解析下載完成的 co2.csv.
    傳出 python 的資料結構
    傳出list,list內的元素是Co2Info實體
    '''
    import csv
    global co2Data
    # 解析 co2.CSV
    with open(FILENAME, newline='', encoding='utf-8') as csvfile:
        next(csvfile)  # 跳過第一行首標題列
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        co2Lst = []
        seqno = 0
        for row in rows:
            seqno += 1
            item = Co2Info()
            item.seq = seqno
            item.country = row[0]
            item.year = row[1]
            item.population = row[2]
            item.co2 = row[3]
            co2Lst.append(item)
        co2Data = co2Lst


def getCo2Data():
    #downloadCo2DataFromPlatForm()  # 下載檔案
    readAndParseCSVFile()
    return co2Data




