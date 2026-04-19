"""
调用风险处置列表接口
接口: http://192.10.91.36:8081/fxfk/api/v1/fxcz/fxczlb
"""

import requests
import json

# ===================== 你可以改 token =====================
input_token = "111"
# ==========================================================

API_URL = "http://192.10.91.36:8081/fxfk/api/v1/fxcz/fxczlb"

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Referer": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com/fxfkxt/homepage.html?yzw_theme=blueTheme&yzw_font=large&",
    "Origin": "http://babg-appweb-pre.oss-cn-hangzhou-yzwsouth-d01-a.res.zgf.yzwsouth.com",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "token": input_token,
    "routerId": "4"
}

PAYLOAD = {
    "limit": 15,
    "offset": 0,
    "warningLevel": [],
    "sujectMc": "",
    "cbrMc": "",
    "sjyMc": "",
    "modelMc": "",
    "notice": "",
    "czzt": "2"
}


def call_fxczlb_api():
    print("=" * 80)
    print("调用风险处置列表接口")
    print("=" * 80)
    print(f"接口URL: {API_URL}")
    print("=" * 80)

    try:
        response = requests.post(API_URL, headers=HEADERS, json=PAYLOAD, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print("[SUCCESS] 接口调用成功!")
            print(f"[INFO] 响应状态码: {response.status_code}")
            print(f"[INFO] 响应数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
            return data
        else:
            print(f"[ERROR] 接口调用失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] 调用接口错误: {e}")


def main():
    call_fxczlb_api()


if __name__ == "__main__":
    main()
