from kivipaperisakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):

    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly

    def _toisen_siirto(self, siirto):
        return self.tekoaly.anna_siirto()
