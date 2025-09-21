import requests
import tkinter as tk
from tkinter import ttk, messagebox

def load_currencies():
    """ดึงรายชื่อสกุลเงินจาก API"""
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" in data:
            return sorted(list(data["rates"].keys()))  # ✅ คืนค่าลิสต์สกุลเงิน
        else:
            return ["USD", "THB", "EUR", "JPY"]
    except Exception as e:
        print("❌ โหลดสกุลเงินไม่สำเร็จ:", e)
        return ["USD", "THB", "EUR", "JPY"]

def convert_currency():
    amount = entry_amount.get()
    from_currency = combo_from.get()
    to_currency = combo_to.get()

    if not amount or not from_currency or not to_currency:
        messagebox.showwarning("Warning", "กรุณากรอกข้อมูลให้ครบ")
        return

    try:
        amount = float(amount)
        url = f"https://open.er-api.com/v6/latest/{from_currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" in data and to_currency in data["rates"]:
            rate = float(data["rates"][to_currency])
            converted = amount * rate

            text_result.config(state="normal")
            text_result.delete("1.0", tk.END)
            text_result.insert(
                tk.END,
                f"{amount:,.2f} {from_currency} = {converted:,.2f} {to_currency}"
            )
            text_result.config(state="disabled")
        else:
            messagebox.showerror("Error", "ไม่พบอัตราแลกเปลี่ยน")
    except Exception as e:
        messagebox.showerror("Error", f"❌ {e}")

def swap_currency():
    """สลับค่าเงิน จาก ↔ ไปยัง"""
    from_cur = combo_from.get()
    to_cur = combo_to.get()
    combo_from.set(to_cur)
    combo_to.set(from_cur)

# ------------------ UI ------------------
root = tk.Tk()
root.title("💱 Currency Converter")
root.geometry("500x300")
root.resizable(False, False)

# โหลดสกุลเงินจาก API
currency_list = load_currencies()

# Amount
tk.Label(root, text="จำนวนเงิน:", font=("Arial", 12)).pack(pady=5)
entry_amount = tk.Entry(root, font=("Arial", 14), justify="center")
entry_amount.pack(pady=5)

# Frame สำหรับ From / To + Swap
frame_currency = tk.Frame(root)
frame_currency.pack(pady=10)

# From Currency
tk.Label(frame_currency, text="จาก:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
combo_from = ttk.Combobox(frame_currency, values=currency_list, state="readonly", width=12)
combo_from.set("USD")
combo_from.grid(row=0, column=1, padx=5)

# ปุ่ม Swap
btn_swap = tk.Button(frame_currency, text="🔄", command=swap_currency, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_swap.grid(row=0, column=2, padx=10)

# To Currency
tk.Label(frame_currency, text="ไปยัง:", font=("Arial", 12)).grid(row=0, column=3, padx=5)
combo_to = ttk.Combobox(frame_currency, values=currency_list, state="readonly", width=12)
combo_to.set("THB")
combo_to.grid(row=0, column=4, padx=5)

# ปุ่มแปลงค่าเงิน
btn = tk.Button(root, text="แปลงค่าเงิน", command=convert_currency,
                bg="#4CAF50", fg="white", font=("Arial", 14))
btn.pack(pady=15)

# Text Box แสดงผล
text_result = tk.Text(root, height=1, width=40, font=("Arial", 14, "bold"), fg="blue", wrap="word")
text_result.pack(pady=20)
text_result.config(state="disabled")

root.mainloop()