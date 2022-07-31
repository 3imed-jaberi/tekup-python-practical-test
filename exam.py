class Personne:
    def __init__(self):
        print("Tapez le information global de la personne: \n")
        self.nom = input("nom: ")
        self.prenom = input("prenom: ")
        self.age = input("age: ")

    def __str__(self) -> str:
        return f"<Personne nom: {self.nom}  prenom: {self.prenom} age: {self.age}>"


class Etudiant(Personne):
    def __init__(self):
        super().__init__()
        print("Tapez le information specifique pour l'etudiant: \n")

        num_ins = int(input("numero d'inscription: "))
        while len(str(num_ins)) != 7:
            num_ins = int(input("numero d'inscription: "))
        self.num_ins = int(num_ins)

        mg = float(input("moyenne generale: "))
        while mg not in range(21):
            mg = float(input("moyenne generale: "))
        self.mg = mg

        note_supp = float(input("note supplementaire: "))
        while note_supp not in range(21):
            note_supp = float(input("note supplementaire: "))
        self.note_supp = note_supp

        i = float(input("status d'etudiant: "))
        while i not in [1.0, 1.10]:
            i = float(input("status d'etudiant: "))
        self.i = i

        self.score = 0

    def calculerscore(self):
        self.score = (5 * self.mg + self.note_supp) * self.i

    def __str__(self) -> str:
        return f"<Etudiant nom: {super().nom}  prenom: {super().prenom} age: {super().age} numero d'inscription: {self.num_ins} moyenne generale: {self.mg}  note supplementaire: {self.note_supp} i: {self.i}>"


class Classes:
    __nb_total = 0

    def __init__(self, nom, set_etudiant=set()):
        self.nom = nom
        self.set_etudiant = set_etudiant

    def get_nb_total(self):
        return self.__nb_total

    def set_nb_total(self, coming_nb_total):
        self.__nb_total = coming_nb_total


def main():
    c1 = Classes("class 1")
    c2 = Classes("class 2")
    c3 = Classes("class 3")

    nb_etudiants = 2
    while nb_etudiants < 3:
        nb_etudiants = int(input("Tapez le nombre d'edutiants: "))

    while nb_etudiants != 0:
        etudiant = Etudiant()
        etudiant.calculerscore()
        if etudiant.score < 95:
            c3.set_etudiant.add(etudiant)
            c3.set_nb_total(c3.get_nb_total() + 1)
        elif etudiant.score > 115:
            c1.set_etudiant.add(etudiant)
            c1.set_nb_total(c1.get_nb_total() + 1)
        else:
            c2.set_etudiant.add(etudiant)
            c2.set_nb_total(c2.get_nb_total() + 1)
        nb_etudiants -= 1

    file = open("db.txt", "a+")
    lineC1 = f"{c1.nom} {c1.get_nb_total()}\n"
    file.write(lineC1)
    lineC2 = f"{c2.nom} {c2.get_nb_total()}\n"
    file.write(lineC2)
    lineC3 = f"{c3.nom} {c3.get_nb_total()}\n"
    file.write(lineC3)
    file.close()


main()
