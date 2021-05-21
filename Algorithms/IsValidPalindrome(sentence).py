def IsValidPalindrome(sti):
    sti, x = sti.split(' '), []
    sti = ''.join(sti)
    sti = sti.lower()
    for i in range(len(sti)):
        if sti[i].isalnum():
            x.append(sti[i])
    sti = ''.join(x)
    rev_sti = sti[::-1]
    return rev_sti == sti 

print(IsValidPalindrome("A man, a plan, a canal: Panama"))