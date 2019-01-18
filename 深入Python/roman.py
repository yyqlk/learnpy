# AUTHOR : YYQLK
#一个简单的罗马字符准换

number_roman = {100: 'C',
                90: 'XC',
                50: 'L',
                40: 'XL',
                10: 'X',
                9: 'IX',
                5: 'V',
                4: 'IV',
                1: 'I',}


def to_roman(n):
    roman = ''
    for key, value in number_roman.items():
        while n >= key:
            roman += value
            n -= key
    return roman



