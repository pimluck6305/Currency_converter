**โครงงาน:** Currency Converter (แปลงค่าเงิน)
**สมาชิกกลุ่ม:**

* แมน (Planner)
* พลอย (Coder)
* ใบยอ แมน (Debuggers)

#  รายงานความก้าวหน้า Sprint 1

## แผนการทำงานSprint 1

* กำหนดขอบเขตโครงการและวางแผนการทำงานในสัปดาห์
* เขียนและแก้ไขโค้ดให้สามารถแปลงสกุลเงินได้ (พื้นฐาน เช่น อัตราคงที่หรือตารางอัตราแบบภายใน)
* ทดสอบการทำงานของโค้ดเพื่อค้นหาข้อผิดพลาดเบื้องต้น

## บทบาทและหน้าที่sprint 1
* แมน (Planner)
  - กำหนดขอบเขตงานของ Sprint 1 (ฟีเจอร์หลักที่ต้องมี เช่น เลือกสกุลต้นทาง/ปลายทาง, ป้อนจำนวน, แสดงผลลัพธ์)
  -  แบ่งงานเป็นรายการย่อย พร้อมกำหนดเวลาสั้น ๆ และผู้รับผิดชอบ
  - ระบุเกณฑ์ความสำเร็จ (acceptance criteria) เช่น ความถูกต้องของการคำนวณ, UI พื้นฐานใช้งานได้
  - ประสานงานประชุมเริ่มต้นและติดตามความคืบหน้าเป็นประจำ
* พลอย (Coder)
  - สร้างโครงร่างโปรเจ็กต์ (โฟลเดอร์ ไฟล์หลัก) และเขียนฟังก์ชันแปลงสกุลเงินพื้นฐาน
  - เก็บค่าราคา/อัตราแบบตายตัวหรือจากตารางภายใน และเขียนฟังก์ชันคำนวณ
  - เขียน unit test เบื้องต้นสำหรับการคำนวณ
  - จัดทำ README พื้นฐานและวิธีรันโปรแกรม
* ใบยอ,แมน (Debuggers)
  - รันการทดสอบแบบ manual เพื่อหาข้อผิดพลาด (เช่น กรณีป้อนค่าผิด รูปแบบทศนิยม ฯลฯ)
  - ตรวจสอบความถูกต้องของการคำนวณกับตัวอย่างจริง
  - รายงานบั๊ก และเสนอข้อปรับปรุงโค้ดให้พลอยแก้ไข
  - ช่วยทดสอบหน่วย (unit tests) และทดสอบการทำงานร่วมกัน (integration) เบื้องต้น

## ผลลัพธ์การทำงานsprint 1

* ได้โปรแกรมแปลงสกุลเงินที่ใช้งานได้จริง
* มีการกำหนดสกุลเงินไว้จำนวนน้อย
* รายงานสรุปความก้าวหน้าของ Sprint 1
  
---

#  รายงานความก้าวหน้า Sprint 2

## แผนการทำงานSprint 2

* เพิ่มสกุลเงินให้มากขึ้นโดยวางแผนใช้งาน API
* ปรับให้โปรแกรมมีความน่าใช้มากขึ้น (UI เบื้องต้น, ข้อความแสดงผลชัดเจน)
* ทดสอบการทำงานของโค้ดเพื่อค้นหาข้อผิดพลาดเบื้องต้น

## บทบาทและหน้าที่sprint 2
* พลอย (Planner)
  - ระบุรายการสกุลเงินที่ต้องเพิ่มและจัดลำดับความสำคัญ
  - วางแผน UI ปรับปรุง
  - กำหนดวิธีทดสอบ (test cases) และเกณฑ์ผ่านสำหรับ Sprint 2
* พลอย,ใบยอ (Coder)
  - ขยายโครงสร้างโปรแกรมให้รองรับสกุลเงินจำนวนมาก
  - เตรียม abstraction สำหรับการเชื่อม API (interface/class) แม้ยังไม่เรียกใช้จริง
  - ปรับปรุง UI พื้นฐาน (input validation, ข้อความแสดงข้อผิดพลาด)
  - เพิ่มชุดทดสอบทั้ง unit/integration สำหรับสกุลเงินที่เพิ่มมา
* แมน (Debuggers)
  - ทดสอบรายการสกุลเงินที่เพิ่มมาทั้งหมด
  - ตรวจสอบการจัดการ input ผิดพลาด และการแสดงผลข้อความผิดพลาด
  - ให้ feedback เรื่อง usability และความถูกต้องของผลลัพธ์
  - ช่วยร่าง test script สำหรับการเชื่อม API ใน sprint ถัดไป

## ผลลัพธ์การทำงานsprint 2

* เพิ่มสกุลเงินให้มากขึ้นแต่ยังไม่มีการดึง API
  
colab sprint2 : https://colab.research.google.com/drive/1Hgez5oo28V4-to8jyYlysJj4WGDXztA6?usp=sharing

---

#  รายงานความก้าวหน้า Sprint 3

## แผนการทำงานSprint 3

* เพิ่มสกุลเงินให้มากขึ้นโดยใช้ API (เชื่อมจริง) — ดึงอัตราแบบ real-time
* ปรับให้โค้ดและระบบมีความน่าใช้มากขึ้น (error handling, caching, format)
* ทดสอบโค้ดว่าใช้งานได้จริง (รวมการทดสอบกับ API)


## บทบาทและหน้าที่sprint 3
* ใบยอ (Planner)
  - เลือก API ที่จะใช้งาน
  - ประสานการทดสอบระบบจริง 
* พลอย,ใบยอ (Coder)
  - เขียนโค้ดเชื่อมต่อ API (request/response parsing, mapping ของสกุลเงิน)
  - ปรับรูปแบบการแสดงผล (ทศนิยม, สัญลักษณ์สกุลเงิน, localize)
  - เพิ่ม automated tests ที่ mock API และ integration tests ที่เรียก API จริง (ถ้าเป็นไปได้)
* แมน (Debuggers)
  - ทดสอบการเรียก API ในสถานการณ์ต่าง ๆ (ปกติ, ช้า, ล้มเหลว)
  - ตรวจสอบความถูกต้องของอัตราที่ได้กับแหล่งข้อมูลอ้างอิง (spot checks)
  - ตรวจสอบ performance (เวลาตอบสนอง) และปัญหา concurrency/locking ถ้ามี
  - บันทึกบั๊กที่พบและติดตามการแก้ไข ทำ regression test หลังแก้บั๊ก

## ผลลัพธ์การทำงานsprint 3

* ดึง API แล้วสามารถแปลงค่าเงินได้ 161 สกุลเงิน

--- 

#  รายงานความก้าวหน้า Sprint final

## แผนการทำงานSprint final(จากcomment)

* ทำหน้า UI ให้มีความใช้ง่ายมากขึ้น
* ทำ uniittest
* ทำการ deployment

## บทบาทและหน้าที่sprint final
* แมน (Planner)
  - ระบุ scope ของการปรับ UI (ต้องการเพิ่มอะไร)
* ใบยอ,แมน (Coder)
  - ปรับปรุง frontend (หรือ UI layer) ให้สวยงามและใช้งานง่าย
  - เพิ่มฟีเจอร์ UX เล็ก ๆ (ปุ่มสลับสกุล)
* พลอย,แมน (Debuggers)
  - ทดสอบ UI ในหลายอุปกรณ์เพื่อตรวจสอบความถูกต้อง
  - ทดสอบ API ที่ดึงมาอีกครั้ง

## ผลลัพธ์การทำงานsprint final

* มีหน้าUIที่สามารถใช้งานได้ง่ายขึ้น
* ได้ทำ unit testที่สำคัญ
  - Test load_currencies ทำหน้าที่ ดึงรายชื่อสกุลเงินจาก API และมี fallback เป็น default ถ้า API ล่ม
  - Test convert_currency ทำหน้าที่ แปลงค่าเงิน จาก amount + from_currency → to_currency
  - Test swap_currency ทำหน้าที่ สลับค่าเงิน จาก/ไปยัง

## TEST CASES
* Test load_currencies() ฟังก์ชัน load_currencies() ทำหน้าที่ ดึงรายชื่อสกุลเงินจาก API และมี fallback เป็น default ถ้า API ล่ม
  - test_load_currencies_success
    - Mock API ให้ตอบกลับ "rates": {"THB": 35, "EUR": 0.9}
    - ตรวจสอบว่าฟังก์ชัน return list สกุลเงินเรียงแล้ว → ["EUR", "THB"]
    - ✅ Test นี้ตรวจสอบว่า โหลดสกุลเงินสำเร็จ
  - test_load_currencies_no_rates
    - Mock API ให้ไม่มี "rates" (เช่น API ตอบ JSON ผิดรูปแบบ)
    - ฟังก์ชันต้อง fallback → return default ["USD","THB","EUR","JPY"]
    - ✅ Test นี้ตรวจสอบ กรณี API ไม่ตอบ rates
  - test_load_currencies_api_error
    - Mock API ให้ raise Exception ("API error")
    - ใช้ patch("builtins.print") เพื่อซ่อน log ❌ โหลดสกุลเงินไม่สำเร็จ
    - ฟังก์ชันต้อง fallback → return default
    - ✅ Test นี้ตรวจสอบ กรณี API ล่ม / network error

* Test convert_currency() ฟังก์ชัน convert_currency() ทำหน้าที่ แปลงค่าเงิน จาก amount + from_currency → to_currency
  - test_convert_currency_success
    - Mock input: 100 USD → THB
    - Mock API: 1 USD = 35 THB
    - Mock text_result widget เพื่อไม่ต้องสร้าง GUI จริง
    - ตรวจสอบว่า insert ข้อความผลลัพธ์ถูกต้อง → "3,500.00"
    - ✅ Test นี้ตรวจสอบ การคำนวณสำเร็จ
  - test_convert_currency_missing_input
    - Mock input: amount / from / to ว่าง
    - ตรวจสอบว่า เรียก messagebox.showwarning
    - ✅ Test นี้ตรวจสอบ กรณีกรอกข้อมูลไม่ครบ
  - test_convert_currency_no_rates
    - Mock API: ไม่มี "rates"
    - ตรวจสอบว่า เรียก messagebox.showerror
    - ✅ Test นี้ตรวจสอบ กรณี API ล้มเหลวหรือไม่มีอัตราแลกเปลี่ยน
      
* Test swap_currency() ฟังก์ชัน swap_currency() ทำหน้าที่ สลับค่าเงินจาก/ไปยัง
  - test_swap_currency()
    - Mock combo_from = "USD", combo_to = "THB"
    - เรียก swap_currency() → ตรวจสอบว่าค่า สลับกันถูกต้อง
    - ✅ Test นี้ตรวจสอบ logic การสลับค่าเงิน

----

- load_currencies() → test การโหลดสกุลเงิน + fallback
- convert_currency() → test การคำนวณ + handle input ผิดพลาด + API ผิดพลาด
- swap_currency() → test การสลับค่าเงิน

---

link test : https://github.com/pimluck6305/Currency_converter/blob/main/test_final_currency_converter.py

เมื่อRUNโค้ดtestได้result ดังนีั้...
<img width="256" height="72" alt="image" src="https://github.com/user-attachments/assets/0fd81731-73c3-4519-9bf9-f71ff4947f2e" />

--- 
