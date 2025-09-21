import unittest
from unittest.mock import patch, MagicMock

# แก้ import ให้ถูกต้อง (ไม่ต้องใส่ .py)
import final_currency_converter as cc   # type: ignore

class TestCurrencyConverter(unittest.TestCase):

    # ---------- TEST load_currencies ----------
    @patch("requests.get")
    def test_load_currencies_success(self, mock_get):
        """โหลดสกุลเงินสำเร็จ"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"THB": 35, "EUR": 0.9}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = cc.load_currencies()
        self.assertEqual(result, ["EUR", "THB"])

    @patch("requests.get")
    def test_load_currencies_no_rates(self, mock_get):
        """API ไม่มี rates → return default"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": "error"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = cc.load_currencies()
        self.assertIn("USD", result)
        self.assertEqual(len(result), 4)

    @patch("requests.get", side_effect=Exception("API error"))
    @patch("builtins.print")  # ซ่อน print
    def test_load_currencies_api_error(self, mock_print, mock_get):
        """API error → return default และซ่อน log"""
        result = cc.load_currencies()
        self.assertIn("USD", result)
        self.assertEqual(len(result), 4)


    # ---------- TEST convert_currency ----------
    @patch("requests.get")
    def test_convert_currency_success(self, mock_get):
        """คำนวณสำเร็จ"""
        # Mock Tkinter widgets
        cc.entry_amount = MagicMock()
        cc.entry_amount.get.return_value = "100"

        cc.combo_from = MagicMock()
        cc.combo_from.get.return_value = "USD"

        cc.combo_to = MagicMock()
        cc.combo_to.get.return_value = "THB"

        cc.text_result = MagicMock()
        cc.text_result.config = MagicMock()
        cc.text_result.delete = MagicMock()
        cc.text_result.insert = MagicMock()

        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"THB": 35}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        cc.convert_currency()
        # ตรวจสอบว่าผลลัพธ์ถูกเรียก insert ลง Text widget
        cc.text_result.insert.assert_called_once()
        args = cc.text_result.insert.call_args[0]
        self.assertIn("3,500.00", args[1])

    @patch("tkinter.messagebox.showwarning")
    def test_convert_currency_missing_input(self, mock_warning):
        """ไม่มี amount → showwarning"""
        cc.entry_amount = MagicMock()
        cc.entry_amount.get.return_value = ""
        cc.combo_from = MagicMock()
        cc.combo_from.get.return_value = ""
        cc.combo_to = MagicMock()
        cc.combo_to.get.return_value = ""

        cc.convert_currency()
        mock_warning.assert_called_once()

    @patch("requests.get")
    @patch("tkinter.messagebox.showerror")
    def test_convert_currency_no_rates(self, mock_error, mock_get):
        """API ไม่มี rates → showerror"""
        cc.entry_amount = MagicMock()
        cc.entry_amount.get.return_value = "100"
        cc.combo_from = MagicMock()
        cc.combo_from.get.return_value = "USD"
        cc.combo_to = MagicMock()
        cc.combo_to.get.return_value = "THB"
        cc.text_result = MagicMock()

        mock_response = MagicMock()
        mock_response.json.return_value = {"result": "error"}
        mock_get.return_value = mock_response

        cc.convert_currency()
        mock_error.assert_called_once()

    # ---------- TEST swap_currency ----------
    def test_swap_currency(self):
        """สลับค่าเงิน"""
        cc.combo_from = MagicMock()
        cc.combo_to = MagicMock()
        cc.combo_from.get.return_value = "USD"
        cc.combo_to.get.return_value = "THB"

        cc.swap_currency()
        cc.combo_from.set.assert_called_with("THB")
        cc.combo_to.set.assert_called_with("USD")


if __name__ == "__main__":
    unittest.main()