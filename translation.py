class Translation(object):
    START_TEXT = """Merhaba!
Ben basit bir my.telegram.org botuyum.

API ID ve API HASH almak i癟in Telefon numaran覺z覺 羹lke koduyla girin.

????Bot G羹ncellemeleri : @chillgng

/start t覺klayarak botu ba??lat覺n"""
    AFTER_RECVD_CODE_TEXT = """Anl覺yorum !
??imdi l羹tfen Telegram'dan ald覺??覺n覺z Telegram kodunu g繹nderin!

bu kod yaln覺zca my.telegram.org'dan APP kimli??ini almak amac覺yla kullan覺l覺r.
\nBu robot geli??tiriciye g羹venmiyorsan覺z, l羹tfen siteden al覺n
https://my.telegram.org/ 

Click /Start To Restart The Progress"""
    BEFORE_SUCC_LOGIN = "al覺nan kod. Web sayfas覺 taran覺yor..."
    ERRED_PAGE = "bir yanl覺??l覺k var. uygulama kimli??i al覺namad覺.. \n\n@chillgng\n\nWeb Sitesi 襤癟in Api Kodu Nas覺l Al覺n覺r"
    CANCELLED_MESG = "G繹r羹??羹r羹z! L羹tfen bot konu??mas覺n覺 yeniden /start t覺klay覺n"
    IN_VALID_CODE_PVDED = "羹zg羹n羹z, ancak giri?? ge癟erli bir Telegram Web-Giri?? kodu gibi g繹r羹nm羹yor"
    IN_VALID_PHNO_PVDED = "羹zg羹n羹z, ancak giri?? ge癟erli bir telefon numaras覺 gibi g繹r羹nm羹yor"
