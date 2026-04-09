def text_to_ints(text : str) -> list[int]:
    text = ''.join(c for c in text.upper() if c.isalpha())
    res = []
    for char in text:
        res.append(ord(char)-65)
    
    return res

def ints_to_text(ints: list) -> str:
    res = []
    for num in ints:
        res.append(chr(num+65))

    return "".join(res)

def pad(ints: list[int], n: int) -> list[int]:
    l = [0]*((n-len(ints)%n)%n)
    ints.extend(l)
    return ints


    