import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestVoiceAppointment(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_voice_booking_turn(self):
        res = self.client.post("/voice-appointment", json={"call_sid": "CALL-777", "user_speech": "Can I book for tomorrow at 2pm?"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["booking_status"], "BOOKING_COMPLETED")

if __name__ == "__main__":
    unittest.main()
