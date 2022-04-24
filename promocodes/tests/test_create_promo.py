from django.test import TestCase
import subprocess


class TestPromo(TestCase):
    def test_promo_creation(self):
        test_cases = [
            subprocess.run(["venv/Scripts/python", "manage.py", "create_promo", "12", "агенства"], capture_output=True),
            subprocess.run(["venv/Scripts/python", "manage.py", "create_promo", "1", "агенства"], capture_output=True),
            subprocess.run(["venv/Scripts/python", "manage.py", "create_promo", "12", "avtostop"], capture_output=True),
            subprocess.run(["venv/Scripts/python", "manage.py", "create_promo", "5", "1"], capture_output=True),
        ]
        for case in test_cases:
            self.assertEqual(case.returncode, 0)
