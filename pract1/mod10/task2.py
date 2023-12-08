import re

color="##2345"

pattern=r"^#?(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}$|^rgb\((?:\d{1,3}%?(?:,\s*)?){3}\)$|^hsl\((?:\d{1,3}%?(?:,\s*)?){3})$"

if re.match(pattern, color):
    print("Пароль корректный.")
else:
    print("Пароль некорректный.")

##?(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}- после # идут либо 3 символа (0-9a-fA-F) либо 6

#rgb\((?:\d{1,3}%?(?:,\s*)?){3}\)-после rgb идёт 3 значения, разделенных запятой и возможным пробелом
#{1,3}- одно, двух или трех значное число
#%?- символ % может быть а может и не быть
#(?:,\s*)- после числа может следовать запятая и возможный пробел

#hsl\((?:\d{1,3}%?(?:,\s*)?){3})- после hsl идет три значения разделенных запятой и возможным пробелом
#{1,3}- одно, двух или трех значное число
#%?- символ % может быть а может и не быть
#(?:,\s*)- после числа может следовать запятая и возможный пробел