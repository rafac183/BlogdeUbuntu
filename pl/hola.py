def swapText(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    print(result)
swapText("HoLa A tOdOs")