def get_combination_of_index(length):
    """
    Create a combination of index

    Parameters
    ----------
    length - int
        Size of the list of words

    Returns
    -------
    generator
        A generator of possible combination of index
    """
    # list of index
    indexes = list(range(length))
    # define max index
    indexes.reverse()
    max_index = int(''.join(str(i) for i in indexes))+1
    indexes.reverse()
    i = 0
    # generate str of index to max_index
    while i < max_index:
        item = list(str(i).zfill(length))
        tmp_result = []
        for index in indexes:
            tmp_result.append(str(index) in item)
        if not False in tmp_result:
                yield item
        i += 1

def get_combination_of_names(words):
    """
    Create a combination of name based on possible index and word list

    Parameters
    ----------
    words : list
        List of words

    Returns
    -------
    generator
        A generator for all possible names
    """
    for indexes in get_combination_of_index(len(words)):
        tmp_result = []
        i = 0
        name = ''
        for index in indexes:
            try:
                name += words[int(index)][i]
                i += 1
            except IndexError:
                name += ''
        yield name
