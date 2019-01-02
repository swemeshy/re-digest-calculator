def list_w_commas(str):
    """
    >>> list_w_commas('12, 34, 45, 90')
    [12, 34, 45, 90]
    """
    items = iter(list(str))
    number = ''
    lst = []
    # assert isinstance(int(list(str)[0]), int), 'Must be a list of numbers separated by commas and spaces'
    for i in items:
        if i == ',':
            if next(items) != ' ':
                raise TypeError('Must be a list of numbers separated by commas and spaces')
            lst.append(int(number))
            number = ''
        elif isinstance(int(i), int):
            number += i
    lst.append(int(number))
    return lst




def re_digest():
    # """
    # >>> re_digest([9224, 38880], 44174)
    # [14518, 29656]
    # >>> re_digest([4227, 7893, 11022, 12315, 13261, 24333, 27118, 28237, 33463], 44174)
    # [946, 1119, 1293, 2785, 3129, 3666, 5226, 11072, 14938]
    # """
    cuts = list_w_commas(input('List of cuts: '))
    cuts.sort()
    total = int(input('Total bp: '))
    cuts_inv = cuts[::-1]
    assert len(cuts) > 1
    assert cuts_inv[0] <= total
    pieces = []
    pieces.append(total - cuts_inv[0] + cuts[0])
    while len(cuts) > 1:
        pieces.append(cuts[1] - cuts[0])
        cuts.remove(cuts[0])
    pieces.sort()
    return pieces

while True:
    x = str(re_digest())
    x = x[1:len(x) - 1]
    print('Pieces: ' + x)
    print('*********************************************')


def _test():
    import doctest
    doctest.testmod()

# if __name__ == '__main__':
#     _test()
