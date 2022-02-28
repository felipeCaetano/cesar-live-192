from string import ascii_lowercase


def encripta(message, rot=13):
    """Encripta a message."""

    encriptado = ''
    for letra in message:
        letra = letra.lower()
        if letra == ' ':
            encriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) + rot
            letra = ascii_lowercase[pos % 26]
            encriptado += letra
    return encriptado


def decripta(message, rot=13):
    """Decripta a menssagem."""

    return encripta(message, rot)
