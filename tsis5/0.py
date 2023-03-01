# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.
import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern,  text):
        print 'found a match!'
    else:
        print 'no match'
