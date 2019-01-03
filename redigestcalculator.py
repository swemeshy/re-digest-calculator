import re


def list_w_commas(string):
    """
    A function that converts a string of numbers
    separated by commas into a list.
    >>> list_w_commas('12, 34, 45, 90')
    [12, 34, 45, 90]
    >>> list_w_commas('')
    >>> list_w_commas('100,23,45')
    [100, 23, 45]
    """
    if not re.search(r'(([0-9]+), )*([0-9]+)', string):
        return None
    return list(map(int, re.split(r',', string)))


def re_digest(cuts, total):
    """
    Takes in a list of numbers CUTS and the plasmid size
    TOTAL (in bp). Returns the lengths of the pieces
    (in bp) after a restriction digest with the inputted
    cut sites.
    >>> re_digest([9224, 38880], 44174)
    [14518, 29656]
    >>> re_digest([4227, 7893, 11022, 12315, 13261, 24333, 27118, 28237, 33463], 44174)
    [946, 1119, 1293, 2785, 3129, 3666, 5226, 11072, 14938]
    """
    cuts.sort()
    cuts_inv = cuts[::-1]
    assert len(cuts) >= 1
    assert cuts_inv[0] <= total
    pieces = [total - cuts_inv[0] + cuts[0]]
    while len(cuts) > 1:
        pieces.append(cuts[1] - cuts[0])
        cuts.remove(cuts[0])
    pieces.sort()
    return pieces


# Uncomment code below to test

# def _test():
#     import doctest
#     doctest.testmod()
#
#
# _test()


print("Type 'exit' to quit")
while True:
    c = list_w_commas(input('List of cuts: '))
    if not c:
        print('Must be a list of numbers separated by commas. Cannot be empty.')
        continue
    if c == 'exit':
        break
    inp_t = input('Total bp: ')
    if re.search(r'\W+', inp_t):
        print('Must be a single number.')
        continue
    if inp_t == 'exit':
        break
    t = int(inp_t)
    if t < max(c):
        print('Plasmid size should be greater than all cut sites')
        continue
    x = str(re_digest(c, t))
    x = x[1:len(x) - 1]
    print('Pieces: ' + x)
    print('*********************************************')
