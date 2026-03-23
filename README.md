
# Craftrise Oyuncu Checker

Craftrise sunucusundaki oyuncuların ban durumunu terminal üzerinden hızlı, renkli ve güvenli bir şekilde sorgulamanızı sağlayan Python tabanlı bir CLI aracı.

## Özellikler

- **Hızlı Sorgulama:** `requests.Session()` altyapısı sayesinde bağlantıyı açık tutarak seri sorgularda maksimum hız sağlar.
- **Renkli Çıktılar:** `colorama` kütüphanesi kullanılarak sonuçlar terminalde kolay okunabilir şekilde (Banlı: Kırmızı, Temiz: Yeşil) gösterilir.
- **Gelişmiş Hata Yakalama:** Sunucu çökmelerine, zaman aşımı (timeout) durumlarına veya Cloudflare engellemelerine karşı korumalıdır. Patlamaz, size ne olduğunu söyler.
- **Bot Koruması:** Özel `User-Agent` ve header bilgileriyle isteklerin sunucu tarafından reddedilme ihtimali en aza indirilmiştir.

---

## Gereksinimler

Bu aracı çalıştırabilmek için sisteminizde **Python 3.x** kurulu olmalıdır. Ayrıca aşağıdaki Python kütüphanelerine ihtiyaç vardır:
- `requests`
- `colorama`

---

## Kurulum

1. Repoyu bilgisayarınıza klonlayın:
```bash
git clone [https://github.com/y4gz/craftrise-checker.git](https://github.com/y4gz/craftrise-checker.git)
cd craftrise-checker
```

2. Gerekli kütüphaneleri kurun:
```bash
pip install requests colorama
```
*(Eğer `pip` hata verirse `pip3 install requests colorama` olarak deneyebilirsiniz.)*

---

## Kullanım

Kurulumu tamamladıktan sonra terminal veya komut satırında aracı başlatmak için şu komutu girin:

```bash
python checker.py
```

Araç açıldığında size bir kullanıcı adı soracaktır:
- Sorgulamak istediğiniz oyuncunun adını yazıp `Enter`a basın.
- Çıkmak istediğinizde `exit` yazmanız yeterlidir.

**Örnek Görünüm:**
```text
=== Craftrise Oyuncu Checker V2 ===

Kullanıcı adı giriniz ('exit' ile çık): ahmet
 ahmet adlı oyuncu BANLI.

Kullanıcı adı giriniz ('exit' ile çık): yagiz
 yagiz adlı oyuncu TEMİZ.
```

---

## Yasal Uyarı

Bu araç tamamen eğitim ve test amacıyla yazılmıştır. Çok hızlı ve art arda yapılan sorgular Craftrise sunucuları tarafından IP adresinizin geçici veya kalıcı olarak engellenmesine (Rate Limit/Ban) yol açabilir. Aracın kullanımından doğabilecek her türlü sorumluluk kullanıcıya aittir.
