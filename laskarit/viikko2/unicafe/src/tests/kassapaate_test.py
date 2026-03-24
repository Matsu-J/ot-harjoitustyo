import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassapaate_alustuu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
  
    
    def test_osta_edullinen_kateinen_riittavalla_rahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_osta_maukas_kateinen_riittavalla_rahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_osta_edullinen_kateinen_ei_riittavalla_rahalla(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_osta_maukas_kateinen_ei_riittavalla_rahalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_osta_edullinen_kortilla_liialla_rahalla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_osta_maukas_kortilla_liialla_rahalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)


    def test_osta_edullinen_kortilla_liian_vahalla_rahalla(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
    
    def test_osta_maukas_kortilla_liian_vahalla_rahalla(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)



    def test_lataaminen_toimii_postiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_lataaminen_toimii_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)
    

    def test_kassa_palauttaa_oikein(self):
        vastaus = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(vastaus, 1000,0)