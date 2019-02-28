def list_sort(h):

    character = []
    odds = []
    evens = []
    mydict = dict()
    if not isinstance(h, list):
        return 'Invalid Input'

    if not h:
        
        mydict['chars'] = character
        mydict['odds'] = odds
        mydict['evens'] = evens
        return mydict

    for n in h:

        if isinstance(n, int):
            if n % 2 == 0:
                evens.append(h)
            
            else:
                odds.append(n)

        elif isinstance(n, str):
            character.append(n)

    mydict['chars'] = sorted(character)
    mydict['odds'] = sorted(odds)
    mydict['evens'] = sorted(evens)
    return mydict


print(list_sort([4, 8, 9, 5, 'r']))