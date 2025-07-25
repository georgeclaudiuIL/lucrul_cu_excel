
class persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"Numele persoanei este {self.nume} si are varsta de {self.varsta}."

if __name__ == "__main__":
    persoana1 = persoana("Adrian", 32)
    print(persoana1.nume)
    print(persoana1)