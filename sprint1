exchange_rate = {
    "USD": 36.50,   # 1 USD = 36.50 THB
    "EUR": 39.00,   # 1 EUR = 39.00 THB
    "JPY": 0.25,    # 1 JPY = 0.25 THB
    "THB": 1.00     # 1 THB = 1 THB
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rate or to_currency not in exchange_rate:
        return None
    # แปลงจากสกุลต้นทาง -> บาท -> สกุลปลายทาง
    amount_in_thb = amount * exchange_rate[from_currency]
    result = amount_in_thb / exchange_rate[to_currency]
    return result

--- เริ่มโปรแกรม ---
print("=== Currency Converter ===")
print("รองรับสกุลเงิน:", ", ".join(exchange_rate.keys()))

รับค่าจำนวนเงิน
amount = float(input("กรอกจำนวนเงิน: "))

รับสกุลเงินต้นทางและปลายทาง
from_cur = input("จากสกุลเงิน (เช่น USD, EUR, THB): ").upper()
to_cur = input("ไปยังสกุลเงิน (เช่น USD, EUR, THB): ").upper()

เรียกใช้งานฟังก์ชันแปลงค่า
converted = convert_currency(amount, from_cur, to_cur)

if converted is not None:
    print(f"{amount:.2f} {from_cur} = {converted:.2f} {to_cur}")
else:
    print("❌ ไม่รองรับสกุลเงินที่เลือก")
