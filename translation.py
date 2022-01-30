class Translation(object):
    START_TEXT = """Merhaba!
Ben basit bir my.telegram.org botuyum.

API ID ve API HASH almak için Telefon numaranızı ülke koduyla girin.

🤖Bot Güncellemeleri : @chillgng

/start tıklayarak botu başlatın"""
    AFTER_RECVD_CODE_TEXT = """Anlıyorum !
Şimdi lütfen Telegram'dan aldığınız Telegram kodunu gönderin!

bu kod yalnızca my.telegram.org'dan APP kimliğini almak amacıyla kullanılır.
\nBu robot geliştiriciye güvenmiyorsanız, lütfen siteden alın
https://my.telegram.org/ 

Click /Start To Restart The Progress"""
    BEFORE_SUCC_LOGIN = "alınan kod. Web sayfası taranıyor..."
    ERRED_PAGE = "bir yanlışlık var. uygulama kimliği alınamadı.. \n\n@chillgng\n\nWeb Sitesi İçin Api Kodu Nasıl Alınır"
    CANCELLED_MESG = "Görüşürüz! Lütfen bot konuşmasını yeniden /start tıklayın"
    IN_VALID_CODE_PVDED = "üzgünüz, ancak giriş geçerli bir Telegram Web-Giriş kodu gibi görünmüyor"
    IN_VALID_PHNO_PVDED = "üzgünüz, ancak giriş geçerli bir telefon numarası gibi görünmüyor"
