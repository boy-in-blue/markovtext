s = 'dsfdsfdsfds\n\nCHAPTER I ddsdsfdsfdsfdsfdsfds\nCHAPTER II dsfdsfdsfssfdsfddsf\n\n'
import re
pat = r'CHAPTER\s[A-Z]{1,2}'
r = re.split(pat, s, maxsplit=10)

print(r)
