import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_saldo_1000_euroa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_uuden_kassapaatteen_myydyt_lounaat_0_kpl(self):
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaat, 0)

    def test_edullinen_lounas_kateismaksu_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_lounas_kateismaksu_vaihtorahan_suuruus_on_oikein(self):
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_maukas_lounas_kateismaksu_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_lounas_kateismaksu_vaihtorahan_suuruus_on_oikein(self):
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_edullinen_lounas_kateismaksu_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kateismaksu_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_jos_maksu_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_lounas_jos_maksu_ei_riita_rahat_palautetaan(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_edullinen_lounas_jos_maksu_ei_riita_myytyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_lounas_jos_maksu_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_jos_maksu_ei_riita_rahat_palautetaan(self):

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_maukas_lounas_jos_maksu_ei_riita_myytyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_lounas_jos_kortilla_tarpeeksi_rahaa_korttiosto_toimii(self):

        return_value = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        # Summa veloitetaan kortilta:
        self.assertEqual(self.maksukortti.saldo, 1000 - 240)
        # Palautetaan True:
        self.assertEqual(return_value, True)
        # Myytyjen lounaiden määrä kasvaa:
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_jos_kortilla_tarpeeksi_rahaa_korttiosto_toimii(self):

        return_value = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        # Summa veloitetaan kortilta:
        self.assertEqual(self.maksukortti.saldo, 1000 - 400)
        # Palautetaan True:
        self.assertEqual(return_value, True)
        # Myytyjen lounaiden määrä kasvaa:
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_jos_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(10)

        return_value = self.kassapaate.syo_edullisesti_kortilla(kortti)

        # Kortin rahamäärä ei muutu:
        self.assertEqual(kortti.saldo, 10)
        # Myytyjen lounaiden määrä ei muutu:
        self.assertEqual(self.kassapaate.edulliset, 0)
        # Palautetaan False:
        self.assertEqual(return_value, False)

    def test_maukas_lounas_jos_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(10)

        return_value = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        # Kortin rahamäärä ei muutu:
        self.assertEqual(kortti.saldo, 10)
        # Myytyjen lounaiden määrä ei muutu:
        self.assertEqual(self.kassapaate.maukkaat, 0)
        # Palautetaan False:
        self.assertEqual(return_value, False)

    def test_edullinen_lounas_korttiosto_ei_muuta_kassan_rahamaaraa(self):

        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_korttiosto_ei_muuta_kassan_rahamaaraa(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataus_kortille_onnistuu(self):

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        # Kortin saldo muuttuu, kun sille ladataan rahaa:
        self.assertEqual(self.maksukortti.saldo, 1100)
        # Kassassa oleva rahamäärä muuttuu ladatulla summalla:
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):

        return_value = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        # Metodi lataa_rahaa_kortille ei palauta mitään, jos summa < 0:
        self.assertEqual(return_value, None)

    def test_kassan_rahamaaran_kertova_metodi_tulostaa_oikein(self):
        
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)