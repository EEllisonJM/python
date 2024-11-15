import secrets
import string

longitud = int(input('Longitud de la contraseña: '))
contraseña = ''.join(secrets.choice(string.printable) for _ in range(longitud))
print('Contraseña generada:', contraseña)
