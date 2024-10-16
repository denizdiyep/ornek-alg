# Öğrenci notlarını bir liste olarak tanımla
ogrenci_notlari = [85, 90, 78, 92, 88, 50, 31, 72]

# Notların toplamını hesapla
toplam_not = sum(ogrenci_notlari)

# Öğrenci sayısını al
ogrenci_sayisi = len(ogrenci_notlari)

# Sınıf not ortalamasını hesapla
sinif_ortalamasi = toplam_not / ogrenci_sayisi

# Sonucu ekrana yazdır
print(f"Sınıf not ortalaması: {sinif_ortalamasi:.2f}")
