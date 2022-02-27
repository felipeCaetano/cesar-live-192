from string import ascii_lowercase


def encripta(message, n=13):
    """encripta a message."""

    encriptado = ''
    for l in message:
        l = l.lower()
        if l == ' ':
            encriptado += l
        elif l not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encriptado += l
    return encriptado


def decripta(message, n=13):
    return encripta(message)
