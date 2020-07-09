# 1. SORU
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
# 3. SORU
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modüler ters mevcut değil
    else:
        return x % m

    # afin şifreleme şifreleme işlevi


# şifre tex döndürür
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


# afin şifre çözme fonksiyonu
# orijinal metni döndürür
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])


# Yukarıdaki işlevleri test etmek için Sürücü Kodu
def main():
    # metin ve anahtar bildirme
    text = 'DENIZ SEREZLI'
    key = [17, 20]

    # çağrı şifreleme işlevi
    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # şifre çözme işlevi çağırma
    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
    main()

    # 4. SORU
    sayi = int(input("Sayi Giriniz:"))
    sayac = 0
    toplam = 0
    sayac2 = 0

    for i in range(2, (sayi + 1)):
        sayac = 0
        for j in range(2, i):
            if (i % j == 0):
                sayac = sayac + 1
                break
        if (sayac == 0):
            print(i)
            sayac2 = sayac2 + 1

    print("Toplam ", sayac2, " adet asal sayı var.")
