import base64
import hashlib

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

__all__ = [
    "md5",
    "b64encode",
    "b64decode",
]

UTF8 = "utf-8"
DEFAULT_PASSWORD_FIELD = "password"


def md5(content: str) -> str:
    m = hashlib.md5()
    m.update(content.encode(UTF8))
    return m.hexdigest()


def b64encode(content: str) -> str:
    return base64.b64encode(content.encode(UTF8)).decode(UTF8)


def b64decode(content: str) -> str:
    return base64.b64decode(content.encode(UTF8)).decode(UTF8)


def red_decrypt():
    ciphertext = "i8e96i0wyA3e0J1etuXR/dkDmKvFRlBuIpdSyzcv18VSq2zp2XjW31tOA/FzdcNi/WHJQT9NAPJe6CDQrFylvDx3Z4vhEHMZOzrv88BW6Dk0dc94j+hsRldBBKnMIXaZRDB9Maj1wTu9TTgvb9D+cEonQnDz3qAQHfzbY0Jz0p5WNfiDE3zi17xQeDVQFe0r1N93jRRfLhEZ35pQFImYKAEFopOQBVEpRxbBhFAjPg1V9DEuEwst42rqmjTgX7Xpt6DuazKwy0zCAucA/FcQVfDr9CkwE5pfPO+RQP2Ku2cbd6iB9yqz0GdO60/Z6ljbvNTE7Npbi67QK0CRcs4x2xgqg+D8mfpkc9bnVz++oiW9I2lkH7P71yCNbNwDBkHMqd08juCkyg06a112MAcwwpHdyQdLdSGGx7XfrFOKmg7ZmQG161PE3FiX2t6sLDSTcmyQlwoQvbiYmsV8Qiho4kc1T4R5xMzaivDOsm6dJ/03+tehXDI+UBxh0MznUwU5Aa/WnnaMkBJ7eK4wePVeHXGazBKGbepnr61zQ0ZdBr1yE78dzuLqG2zkowhMsEvaaiU6n7KSPufkWsvCmn9L4aCzt2h4z3hqwXh8snsutEPBaLuTenoi+YBZcm5oY3nz/jiLPQt/9NkpfiaghP/+OOLhGqLzDvY8J86PY+hbN/A2YAO9dgTeocxjI0bk/SFn54pgR2KG7KjOuhW+T2pkTmvLU2QFPrZ9DkhtaLTGuuspUXFMeC8vhu67jvsbq1E0RdjYHsiAcGQfI+WlYSbtcrynL4Tdv2vME+tJMGhvWKXtRBMJ3YuWzyF3A5sFflB1CkE/arfc238VN49b25ld3lDTiegZ82aha7t5J0SB1eTd0/AE+JT4b+BZA4Fqge9PbnYSgWyFvJTq5YWa3Nq2Yjj9ccgwotVBEsdfE6eKhcGyDtRY+JF1LJs7A7ZDPGSpkktRmL2kWQhYU8e/pU3ClqKXbHaYiIkrzSJKI457kSHLmt8oMeFdD8zotj+xrwHbiiMDY43sC7zc/gNIImZWFoJVe0D3/3j1kpZ93thi5Is0GXNoex5QyBPvFR3PlGQdN4v3LBjjipZyPTIs9LWhmNegahPxaGJvfylRlsNRt+MXA2bAsztJIhwYcbQJHhS64jsk2/W9EqeSRKYfyED/ANmEGUQFdTIgro5EmZMcha5bxJgPzOxv/DB+VIIbkMHfo5fPFpS0sJ/pBJM5Y1ybgbtfw7EbqUfLWiSet83qwFBjXg7Vyxj63nj5qkkS6vDceRcagMHfwREjJkdnmJrAv4Kns4EupsJ4XtOAu7GTKgaCFDiLHKX4k6WndOTd06fK3LGO3Ak6jbF5lEQL1pNclAS5yAlgRwnCcobrn+VWCCYF6XuhzxGaC3/jeeCMDHD3y3XLThbS32H1p8k5awgBjQtScZgm2UcyuNJUqFHpSVS2Zcccj/HqFypE/g28kMaa5jCrIN2wpFPemuQxdbi5MDYhkjGiOhm3l2hrvzIxViud7f8ekaGGoB5IGM/9uy8wIML24Kta1seJaRsC/mFhCD/nNBQzaxNFZy47lqFfi81496JoR3c+bM31rreDY3Iwre8gEatBJEuF2fJR71F2led4ONbJ2cG8XYFrYTAqTyZzf25JOuI308ITKUbCga8+JDzYxL9EhOXaIN86PEJao6lUWHrrEYXLMpUUU4C8OOA="  # noqa: #501
    pem = "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCqblHfz/2ohTf+QendtBqsTVR4m9iNFr4gkVryMGo5AOGkfzkFLGxbza0+PuI9MDZoMQLsSeijryq4iJ2csEIboshudSUyQ4DvXhamDvR8R6kMCZXFFHvD01JtKyUrlFnIRTMdG7sFEN8XF4Vt9FpqOONMb2GyWc9ieosNfoDBEwIDAQABAoGADHpVPjvd7qRwrAneLUabAu09qplM0Ok1J4p2crx+tAiCr+asoXQi+Gzl95ezb31qWyIZ4uJ3L0mLQpI/nKtlVSTcED0GEan+GhhsdMdB8OojSYdXWk3o/L1PpT6rBZa95Y2tZ64UP9axXyIt0YzNw5SCSpySb0qp6L4EaaUEvyECQQDQfhxDaYEkIrf3+YtZEoaKkyAdqfhGUbXPWuRstRa3BswB2RvMoxkRs74XGIkF+aTHprDfeevAJ+PRb+g8UKixAkEA0UP6Ozay28rhvR0+Me74DMjlqsL7dv2ek5LWYKvNXMJnR9XiF7+a6daOn9kDZQ0VAnXyBe5gpbvCD3jfloz3AwJANk4CspRSbMUWQeKfpw2qOYHkxZU186rovh+gi6gHSJjenkScdwqsRu4YPw/G8OV7Q/1o6GxrOVuqfSy2wq8HoQJALRiUFSydcKYQ7Xseyw3vYHnunFT2cdcH1E+BaUW8tK+kKCPcXDfLP3cgNyxCAgXGsEgQhtyu8Sg8Eq9+p2frVwJBAJyXutx7yplpLE/aozG2go20xePmZRTDDi5yPJLGMcBwTamKeVVNWoy/P9sXHs8xK+ChpK+80ku+akYWDMc0WQ4=\n-----END RSA PRIVATE KEY-----"  # noqa: #501
    msg = base64.b64decode(ciphertext.encode('utf-8'))
    res = []
    cipher = PKCS1_v1_5.new(RSA.importKey(pem))
    length = 128
    for i in range(0, len(msg), length):
        content = msg[i:i + length]
        ds = cipher.decrypt(content, '')
        res.append(ds)
    res = "".join(res)

    print('解密数据: ', res)
    print('签名后数据: ', "signature")
    return ""


if __name__ == "__main__":
    red_decrypt()
