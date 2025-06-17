def num_letter_counts(n):
    total = 0
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 
            'sixty', 'seventy', 'eighty', 'ninety']

    for i in range(1, n + 1):
        word = ''
        num = i

        if num == 1000:
            word = 'onethousand'
            total += len(word)
            continue 

        if num >= 100:
            word += units[num // 100] + 'hundred'
            num %= 100
            if num != 0:
                word += 'and'  

        if num >= 20:
            word += tens[num // 10]
            num %= 10
        elif 10 <= num <= 19:
            word += teens[num - 10]
            num = 0 

        if 1 <= num <= 9:
            word += units[num]
        
        total += len(word)
    
    return total

print(num_letter_counts(1000))