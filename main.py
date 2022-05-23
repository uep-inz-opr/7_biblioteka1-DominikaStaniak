class Biblioteka:
    def __init__(self):
      self.egzemplarze = []
      self.czytelnicy = []

    def wypisz_ksiazki(self):
        result = []
        for book in self.egzemplarze:
            t = (book.tytul, book.autor, self.egzemplarze.count(book))
            result.append(t)
        result_set = set(result)     #unikalne wartosci przedstawia
        result_set = sorted(result_set, key = lambda y: y[0])
        return result_set

class Ksiazka:

    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok= rok

    def __eq__(self, other):
        if isinstance(other, Ksiazka):
            return self.tytul == other.tytul
        return False



library = Biblioteka()

il_nowych_egz =int(input())
ksiazka = []
for n in range(il_nowych_egz):
  text = eval(input())
  tytul = text[0]
  autor = text[1]
  rok = text[2]
  egz = Ksiazka(tytul, autor, rok)
  library.egzemplarze.append(egz)

for book in library.wypisz_ksiazki():
    print(book)

