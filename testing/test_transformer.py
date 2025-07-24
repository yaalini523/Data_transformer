import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from transformer.data_transformer import transform_record
from datetime import datetime


class TestTransformerPriya(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_data = {
            "first_name": "Priya",
            "last_name": "Singh",
            "phone": "+91-9988776655",
            "dob": "1992-11-25",
            "email": "priya.singh@example.com",
            "address": "22 MG Road, Mumbai, India",
            "subscription_status": "Inactive",
            "last_login": "2025-07-01T09:45:00",
            "preferred_contact": "Whatsapp",
            "social": {
                "twitter": "@priyasingh"
            },
            "language": "en-IN"
        }
        cls.result = transform_record(cls.input_data)
        print("\nTransformed Result:\n", cls.result)

    def test_name(self):
        self.assertEqual(self.result["name"], "Priya Singh")

    def test_country_code(self):
        self.assertEqual(self.result["country_code"], "91")

    def test_phone_number(self):
        self.assertEqual(self.result["phone_number"], "9988776655")

    def test_age(self):
        dob = datetime.strptime("1992-11-25", "%Y-%m-%d")
        today = datetime.today()
        expected_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        self.assertEqual(self.result["age"], expected_age)

    def test_is_adult(self):
        self.assertTrue(self.result["is_adult"])

    def test_location(self):
        self.assertEqual(self.result["location"], {
            "full_address":"22 MG Road, Mumbai, India",
            "city":"Mumbai",
            "country":"India"
        })

    def test_last_login_ts(self):
        expected_ts = int(datetime.strptime("2025-07-01T09:45:00", "%Y-%m-%dT%H:%M:%S").timestamp())
        self.assertEqual(self.result["last_login_ts"], expected_ts)

    def test_language_main(self):
        self.assertEqual(self.result["language_main"], "en")

    def test_contact_preference(self):
        self.assertEqual(self.result["contact_preference"], "whatsapp")

    def test_social_links(self):
        self.assertEqual(self.result["social_links"], {
            "twitter": "https://twitter.com/priyasingh"
        })

    def test_status_code(self):
        self.assertEqual(self.result["status_code"], 0)


if __name__ == '__main__':
    unittest.main()
