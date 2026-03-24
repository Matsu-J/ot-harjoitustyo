import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lisaaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_positiivinen_saldo_toimii_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)
    
    def test_rahaa_ei_voi_ottaa_liikaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_raha_riittaa_ja_voi_ottaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)
    
    def test_raha_ei_riita_ja_ei_voi_ottaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
    
    def test_saldo_pyoristyy_oikein(self):
        self.maksukortti.ota_rahaa(333.33)
        vastaus = str(self.maksukortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 6.67 euroa")