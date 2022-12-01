KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        self._validate_kapaciteetti(kapasiteetti)
        self._validate_kasvatuskoko(kapasiteetti, kasvatuskoko)

        self.luku_jono = [0] * self.kapasiteetti
        self.alkioiden_lukumaara = 0

    def kuuluu(self, n):
        on = 0

        for i in range(0, self.alkioiden_lukumaara):
            if n == self.luku_jono[i]:
                on = on + 1

        if on > 0:
            return True
        
        return False
    

    def lisaa(self, n):

        if self.alkioiden_lukumaara == 0:
            self.set_first(n)
            return True

        if not self.kuuluu(n):
            self.luku_jono[self.alkioiden_lukumaara] = n
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.alkioiden_lukumaara % len(self.luku_jono) == 0:
                self.copy_procedure()
        
            return True

        return False

    def copy_procedure(self):
        taulukko_old = self.luku_jono
        self.kopioi_taulukko(self.luku_jono, taulukko_old)
        self.luku_jono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.luku_jono)

    def set_first(self, n):
        
        self.luku_jono[0] = n
        self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

    def poista(self, n):

        kohta = self._find_place(n)

        if kohta != -1:
            return self._redefine_positions(kohta)

        return False

    def _find_place(self, n):
        kohta = -1
        for i in range(0, self.alkioiden_lukumaara):
            if n == self.luku_jono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.luku_jono[kohta] = 0
                break

        return kohta

    def _redefine_positions(self, kohta):

        for j in range(kohta, self.alkioiden_lukumaara - 1):
            apu = self.luku_jono[j]
            self.luku_jono[j] = self.luku_jono[j + 1]
            self.luku_jono[j + 1] = apu

        self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
        return True

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumaara

        for i in range(0, len(taulu)):
            taulu[i] = self.luku_jono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.luku_jono[0]) + "}"
        else:
            return self._print_if_alkioiden_lukumaara_is_more_than_one()

    def _print_if_alkioiden_lukumaara_is_more_than_one(self):

        tuotos = "{"
        for i in range(0, self.alkioiden_lukumaara - 1):
            tuotos = tuotos + str(self.luku_jono[i])
            tuotos = tuotos + ", "
        tuotos = tuotos + str(self.luku_jono[self.alkioiden_lukumaara - 1])
        tuotos = tuotos + "}"
        return tuotos

    def _validate_kapaciteetti(self, kapasiteetti):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        
        self.kapasiteetti = kapasiteetti

    def _validate_kasvatuskoko(self, kapasiteetti, kasvatuskoko):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        
        self.kasvatuskoko = kasvatuskoko
