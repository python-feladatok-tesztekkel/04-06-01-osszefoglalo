from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat06(self):
        aktualis = feladatok.feladat06()
        elvart = 5
        self.assertEqual(elvart, aktualis, "A fagyos napok számát nem jól határozta meg!")
