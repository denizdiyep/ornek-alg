import time

def yatak_toplama():
    print("Yatak toplama işlemi başlatılıyor...")
    
    # Adım 1: Yastıkları yerleştir
    print("1. Yastıkları düzeltiyor...")
    time.sleep(5)  # 1 saniye bekleme süresi
    
    # Adım 2: Yatak örtüsünü düzelt
    print("2. Yatak örtüsünü düzeltiyor...")
    time.sleep(5)

    # Adım 3: Yatak çarşafını düzelt
    print("3. Yatak çarşafını düzeltiyor...")
    time.sleep(1)

    # Adım 4: Yatak kenarlarını düzeltiyor
    print("4. Yatak kenarlarını düzeltiyor...")
    time.sleep(5)

    # Adım 5: Yatak tamamen toplandı
    print("Yatak toplama işlemi tamamlandı!")
    
# Yatak toplama simülasyonunu başlat
yatak_toplama()
