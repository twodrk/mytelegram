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
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@NS_Bot_Supporters\n\nHow Get Api Code For Website"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
