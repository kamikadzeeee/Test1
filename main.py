class Anime:
    def __init__(self):
        pass


class Isekai(Anime):
    nazvanie = "suka"
    def show(self):
      print(self.nazvanie)
    def paramaetrs(self):
        pass
    pass

class Hentai(Anime):
    pass# Test1

kino = Isekai()
kino.show()
a = input("Введите название аниме: ")
kino.nazvanie= a
print(kino.nazvanie)

