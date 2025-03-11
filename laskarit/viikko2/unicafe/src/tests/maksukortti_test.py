import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)

    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):

        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_metodi_palauttaa_true_jos_rahat_riittivat(self):

        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):

        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)

    def test_kortin_saldon_kertova_metodi_tulostaa_oikein(self):

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")