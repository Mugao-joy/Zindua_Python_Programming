import re
pattern = r'^[a-z]+$'
name = 'joy'
if re.match (pattern, name):
    print('matched')
else:
    print('not matched')

#3 lowercase letters
#3-5 digits
#one symbol
#upto two uppercase letters
pattern2 = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")