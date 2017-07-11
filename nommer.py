def get_list_index(seq):
    """
    Return a list of index corresponding to the number of index in seq

    Parameters
    ----------
    seq : list
        A list of words

    Returns
    -------
    List
        A list of integer that represent index of seq
    """
    list_index = []
    for i in range(len(seq)):
        list_index.append(i)
    return list_index

def find_index_range(seq):
    """
    Return an integer representing the max integer of index list

    Parameters
    ----------
    seq : list
        A list of words

    Returns
    -------
    int
    """
    seq.reverse()
    return int(''.join(str(el) for el in seq))

def create_list_integer_range(end, fill):
    """
    Return a list of string of number
    Create a list of all integer possible between 0 to the max integer returned
    by find_index_range() and convert each value to string

    Parameters
    ----------
    end : integer
        The max index number to create the list based on range
    fill : integer
        A len to fill the number with leading 0

    Returns
    -------
    list
        A list of all integer from 0 to range(end+1)
    """
    integer_list = []
    #add end+1 to get end in list
    for i in range(end+1):
        integer_list.append(str(i).zfill(fill))
    return integer_list

def create_possible_index_string(list_index, all):
    """
    Create a list of string that represent a sequence of index

    Parameters
    ----------
    list_index : list
        List of index number we want
    all : list
        List of integer from a range

    Returns
    -------
    list
        A list of string that represent a sequence of integer which contains
        all index in list_index
    """
    result = []
    for possible_index in all:
        tmp_result = []
        for i in list_index:
            tmp_result.append(str(i) in possible_index)
        if False not in tmp_result:
            result.append(possible_index)
    return result

def create_possible_index(seq):
    """
    Create a list of index for all possible combination

    Parameters
    ----------
    seq : list
        List of all index in string

    Returns
    -------
    list
        Each item of contain a list of index
    """
    result = []
    for i in seq:
        result.append(list(int(i) for i in list(i)))

    return result

def create_combination(word_list, index_list):
    """
    Create a list of combination of words based on index list

    Parameters
    ----------
    word_list : list
        The original list of words
    index_list : list
        The list of all possible combination of index

    Returns
    -------
    list
        A list with all possible combination of words
    """
    result = []
    for list_index in index_list:
        subresult = []
        for index in list_index:
            subresult.append(word_list[index])
        result.append(subresult)
    return result

def create_name(combination):
    """
    Create list of name from combination list
    Each name follows this pattern n letter of n word for n letter for
    the name. First letter of the first word for the first letter of the name,
    second letter of the second word for second letter of the name, and so on.

    Parameters
    ----------
    combination : list
        List of all combination of words

    Returns
    -------
    list
        A list of name
    """
    for el in combination:
        i = 0
        name = ''
        for word in el:
            try:
                name += word[i]
                i += 1
            except IndexError:
                name += ''
        yield name

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
