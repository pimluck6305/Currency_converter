exchange_rate = {
    "USD": 36.50,   # 1 USD = 36.50 THB
    "EUR": 39.00,   # 1 EUR = 39.00 THB
    "JPY": 0.25,    # 1 JPY = 0.25 THB
    "THB": 1.00,    # 1 THB = 1 THB
    "GBP": 45.20,   # 1 GBP = 45.20 THB (British Pound)
    "CNY": 5.10,    # 1 CNY = 5.10 THB (Chinese Yuan)
    "KRW": 0.027,   # 1 KRW = 0.027 THB (Korean Won)
    "SGD": 26.80,   # 1 SGD = 26.80 THB (Singapore Dollar)
    "AUD": 24.30,   # 1 AUD = 24.30 THB (Australian Dollar)
    "CAD": 26.90,   # 1 CAD = 26.90 THB (Canadian Dollar)
    "CHF": 40.50,   # 1 CHF = 40.50 THB (Swiss Franc)
    "MYR": 8.20,    # 1 MYR = 8.20 THB (Malaysian Ringgit)
    "INR": 0.44,    # 1 INR = 0.44 THB (Indian Rupee)
    "VND": 0.00148, # 1 VND = 0.00148 THB (Vietnamese Dong)
    "LAK": 0.00175, # 1 LAK = 0.00175 THB (Lao Kip)
    "MMK": 0.0174,  # 1 MMK = 0.0174 THB (Myanmar Kyat)
    "IDR": 0.0024,  # 1 IDR = 0.0024 THB (Indonesian Rupiah)
    "PHP": 0.65,    # 1 PHP = 0.65 THB (Philippine Peso)
    "HKD": 4.68,    # 1 HKD = 4.68 THB (Hong Kong Dollar)
    "TWD": 1.13     # 1 TWD = 1.13 THB (Taiwan Dollar)
}

# Dictionary for currency full names (for better user experience)
currency_names = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "JPY": "Japanese Yen",
    "THB": "Thai Baht",
    "GBP": "British Pound",
    "CNY": "Chinese Yuan",
    "KRW": "Korean Won",
    "SGD": "Singapore Dollar",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "MYR": "Malaysian Ringgit",
    "INR": "Indian Rupee",
    "VND": "Vietnamese Dong",
    "LAK": "Lao Kip",
    "MMK": "Myanmar Kyat",
    "IDR": "Indonesian Rupiah",
    "PHP": "Philippine Peso",
    "HKD": "Hong Kong Dollar",
    "TWD": "Taiwan Dollar"
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rate or to_currency not in exchange_rate:
        return None
    # แปลงจากสกุลต้นทาง -> บาท -> สกุลปลายทาง
    amount_in_thb = amount * exchange_rate[from_currency]
    result = amount_in_thb / exchange_rate[to_currency]
    return result

def display_supported_currencies():
    print("\n=== รายการสกุลเงินที่รองรับ ===")
    for code, name in currency_names.items():
        print(f"{code}: {name}")
    print("=" * 40)

print("=== Currency Converter ===")
print("💱 โปรแกรมแปลงสกุลเงิน")
print(f"รองรับสกุลเงิน {len(exchange_rate)} สกุล")

# Ask if user wants to see all supported currencies
show_currencies = input("ต้องการดูรายการสกุลเงินทั้งหมด? (y/n): ").lower()
if show_currencies == 'y':
    display_supported_currencies()

print(f"\nสกุลเงินที่รองรับ: {', '.join(exchange_rate.keys())}")

try:
    amount = float(input("กรอกจำนวนเงิน: "))
    from_cur = input("จากสกุลเงิน: ").upper()
    to_cur = input("ไปยังสกุลเงิน: ").upper()

    converted = convert_currency(amount, from_cur, to_cur)

    if converted is not None:
        from_name = currency_names.get(from_cur, from_cur)
        to_name = currency_names.get(to_cur, to_cur)
        print(f"\n✅ ผลการแปลง:")
        print(f"{amount:,.2f} {from_cur} ({from_name})")
        print(f"= {converted:,.2f} {to_cur} ({to_name})")
        print(f"\nอัตราแลกเปลี่ยน: 1 {from_cur} = {exchange_rate[from_cur]/exchange_rate[to_cur]:.6f} {to_cur}")
    else:
        print("❌ ไม่รองรับสกุลเงินที่เลือก")
        print("กรุณาเลือกจากสกุลเงินที่รองรับ:")
        print(", ".join(exchange_rate.keys()))

except ValueError:
    print("❌ กรุณากรอกตัวเลขที่ถูกต้อง")
except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")
