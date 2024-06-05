import requests
from pprint import pprint

def download_youbike_data():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
    
    try:
        response = requests.get(youbike_url)
        response.raise_for_status()  # 檢查請求是否成功
        youbike_data = response.json()
        return youbike_data
    except requests.RequestException as e:
        print(f"下載失敗: {e}")
        return None
    except JSONDecodeError:
        print("JSON 解碼錯誤")
        return None

def main():
    youbike_data = download_youbike_data()
    
    if youbike_data:
        print("台北市 YouBike 即時資料下載成功！")
        # 解析並顯示所需數據
        stations = youbike_data.get('retVal', {})
        for station_id, station_info in stations.items():
            print(f"站點編號 (sno): {station_info['sno']}")
            print(f"站點名稱 (sna): {station_info['sna']}")
            print(f"站點區域 (sarea): {station_info['sarea']}")
            print(f"更新時間 (mday): {station_info['mday']}")
            print(f"站點地址 (ar): {station_info['ar']}")
            print(f"站點區域英文 (sareaen): {station_info['sareaen']}")
            print(f"站點名稱英文 (snaen): {station_info['snaen']}")
            print(f"站點地址英文 (aren): {station_info['aren']}")
            print(f"是否可借 (act): {station_info['act']}")
            print(f"資料更新時間 (srcUpdateTime): {station_info['srcUpdateTime']}")
            print(f"即時更新時間 (updateTime): {station_info['updateTime']}")
            print(f"資料記錄時間 (infoTime): {station_info['infoTime']}")
            print(f"資料記錄日期 (infoDate): {station_info['infoDate']}")
            print(f"總車位數 (total): {station_info['tot']}")
            print(f"可借車輛數 (available_rent_bikes): {station_info['sbi']}")
            print(f"可還空位數 (available_return_bikes): {station_info['bemp']}")
            print(f"緯度 (latitude): {station_info['lat']}")
            print(f"經度 (longitude): {station_info['lng']}")
            print('-' * 40)
            break

if __name__ == "__main__":
    main()
