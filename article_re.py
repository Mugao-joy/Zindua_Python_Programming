import re 

#def article_re():
with open('article.txt', mode = 'r') as file:
    text = file.readlines()
#print(text)
#file_path = 'article.txt'
#extract - pattern 
def extracted_nums(text):
    pattern = re.compile(r'^[\b(?:\d+(?:,\d{3})*(?:\.\d+)?|\.\d+)\b]')
    #\b -boundary btn word and non-word character
    #\d+ -This matches one or more digits.
    #?: - groups enclosed expression without capturing matched text
    #(?:,\d{3})* - comma separated thousands(comma followed by exactly 3 digits)
    #(?:\.\d+) - period(decimal) followed by one or more digit
    #|\.\d+ - numbers with ony a decimal part eg .25
    #\b - ensures word ends at a boundary
    matches = pattern.findall(text)
    print(matches)