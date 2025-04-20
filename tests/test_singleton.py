import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'creational_patterns')))

import unittest
import threading
from creational_patterns.singleton import AppointmentManager

class TestSingleton(unittest.TestCase):

    def test_singleton(self):
        print("Running Singleton Test...")
        mgr1 = AppointmentManager()
        mgr2 = AppointmentManager()
        mgr1.add_appointment("Checkup")
        self.assertIn("Checkup", mgr2.list_appointments())
        self.assertIs(mgr1, mgr2)  # Same instance
        print("Singleton Test passed for instance consistency.")

    def test_singleton_thread_safety(self):
        print("Running Singleton Thread Safety Test...")

        def create_instance():
            mgr = AppointmentManager()
            mgr.add_appointment("Thread Appointment")
            return mgr

        thread1 = threading.Thread(target=create_instance)
        thread2 = threading.Thread(target=create_instance)

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

        mgr1 = AppointmentManager()  # Singleton instance
        self.assertIn("Thread Appointment", mgr1.list_appointments())
        self.assertIs(mgr1, mgr1)  # Compare the same instance
        print("Singleton Thread Safety Test passed.")

if __name__ == "__main__":
    unittest.main()
