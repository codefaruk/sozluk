genc_sozluk = {
    "itidal": "soğukkanlı",
    "fiktif": "suni, yapay",
    "string": "karakterler listesi",
    "encoding": "bir karakterin bitler (0 ve 1) ile temsili"
}

yeni_terim = input("eklemek istidiğin terim nedir?\n")
yeni_anlam = input("kelimenin anlama nedir?\n")

genc_sozluk[yeni_terim] = yeni_anlam

sorgu = input("Hangi kelimenin anlamını öğrenmek istersin?")
print(genc_sozluk[sorgu])