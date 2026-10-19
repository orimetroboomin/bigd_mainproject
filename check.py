import pandas as pd
import time
import requests

def fetch_naver_current_price(code: str, retries: int = 2) -> dict:

    url = f"https://m.stock.naver.com/api/stock/{code}/basic"

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=3)
            if response.status_code != 200:
                print(f"❌ [{code}] 네이버 현재가 조회 실패 (응답 코드: {response.status_code}, {attempt}/{retries}번째 시도)")
            else:

                data = response.json()

                price_str = data.get("closePrice", "0").replace(",", "")

                price = int(price_str) if price_str.isdigit() else 0

                if price <= 0:
                    print(f"❌ [{code}] 가격을 숫자로 읽지 못했습니다 "
                          f"(closePrice: {data.get('closePrice')!r}, {attempt}/{retries}번째 시도)")
                else:
                    return {
                        "code": code,
                        "name": data.get("stockName", "알 수 없음"),
                        "price": price,

                        "rate": float(data.get("fluctuationsRatio", "0") or "0"),
                        "is_open": data.get("marketStatus") == "OPEN",

                        "traded_at": data.get("localTradedAt"),
                    }
        except Exception as e:
            print(f"❌ [{code}] 네이버 현재가 조회 중 오류 발생: {e} ({attempt}/{retries}번째 시도)")

        if attempt < retries:
            time.sleep(1) 

    return None

watchlist_int_df = pd.read_csv("watchlist.csv") 
watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})

fetch_naver_current_price(print(watchlist_int_df["code"].tolist()[0]))

print(watchlist_int_df["code"].tolist()) 
print(watchlist_df["code"].tolist())


