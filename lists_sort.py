h=[1, 2, 3, 5.5, 8.2, 'x']

def list_sort(h):

    character = []
    odds = []
    evens = []
    mydict = dict()

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


print(list_sort([1, 2, 3, 5.5, 8.2, 'x']))