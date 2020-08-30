def romanToInt(s: str) -> int:
    number_conv_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if len(s) == 1:
        return number_conv_dict.get(s[0])
    
    num = 0
    while len(s) > 0:
        f_letter = s[0]
        if len(s) > 1:
            n_letter = s[1]

        minus_i = f_letter == 'I' and n_letter in ['V', 'X']
        minus_x = f_letter == 'X' and n_letter in ['L', 'C']
        minus_c = f_letter == 'C' and n_letter in ['D', 'M']

        if minus_c or minus_x or minus_i:
            num += number_conv_dict.get(n_letter) - number_conv_dict.get(f_letter)
            
            # Remove pair from list
            s = s[2:]
        
        else:
            num += number_conv_dict.get(f_letter)
            s = s[1:]

    return num
        