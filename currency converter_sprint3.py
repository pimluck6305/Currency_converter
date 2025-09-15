import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "rates" in data and to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            return amount * rate
        else:
            return None
    except Exception as e:
        print("❌ Error:", e)
        return None

print("=== Currency Converter (API Version) ===")

amount = float(input("กรอกจำนวนเงิน: "))
from_cur = input("จากสกุลเงิน (เช่น USD, EUR, THB, JPY): ").upper()
to_cur = input("ไปยังสกุลเงิน (เช่น USD, EUR, THB, JPY): ").upper()

converted = convert_currency(amount, from_cur, to_cur)

if converted is not None:
    print(f"{amount:,.2f} {from_cur} = {converted:,.2f} {to_cur}")
else:
    print("❌ ไม่สามารถดึงอัตราแลกเปลี่ยนได้")
