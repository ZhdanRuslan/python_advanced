# bencoding
# http://www.bittorrent.org/beps/bep_0003.html

# Strings are length-prefixed base ten followed by a colon and the string.
# For example 4:spam corresponds to 'spam'.

# Integers are represented by an 'i' followed by the number in base 10 followed by an 'e'.
# For example i3e corresponds to 3 and i-3e corresponds to -3.
# Integers have no size limitation. i-0e is invalid.
# All encodings with a leading zero, such as i03e, are invalid,
# other than i0e, which of course corresponds to 0.

# Lists are encoded as an 'l' followed by their elements (also bencoded) followed by an 'e'.
# For example l4:spam4:eggse corresponds to ['spam', 'eggs'].

# Dictionaries are encoded as a 'd' followed by a list of alternating keys
# and their corresponding values followed by an 'e'.
# For example, d3:cow3:moo4:spam4:eggse corresponds to {'cow': 'moo', 'spam': 'eggs'}
# Keys must be strings and appear in sorted order (sorted as raw strings, not alphanumerics).

from functools import reduce

from django.conf import settings

if not settings.configured:
    settings.configure(

    )


def collapse(data):
    return reduce(lambda x, y: x + y, data)


def encode(val):
    if type(val) == int:
        return encode_int(val)
    elif type(val) == list:
        return encode_list(val)
    elif type(val) == dict:
        return encode_dict(val)
    else:
        return encode_str(val)


def decode(val):
    if type(val) == list:
        return decode_list(val)
    elif str(val)[0] == 'i':
        return decode_int(val)
    else:
        return decode_str(val)


def encode_int(val):
    """
    Encoding integer values
    """
    return "i" + str(val) + "e"


def decode_int(val):
    """
    Decoding an integer values
    """
    decoded_int = val[1:val.index('e')]

    if len(decoded_int) > 1 and decoded_int[0] == "0":
        raise Exception("Value with leading zero is incorrect")
    return int(decoded_int)


def encode_str(val):
    """
    Encoding string values
    """
    if type(val) == str:
        val = val.encode()

    return bytes((str(len(val)).encode()) + b':' + val)


def decode_str(val):
    """
    Decoding string value
    """
    return val[val.find(b':') + 1:]


def encode_list(val):
    """
    Encoding lists
    """
    result_list = []
    result_list.append('l')
    for elem in val:
        elem = encode(elem)
        result_list.append(elem)
    result_list.append('e')
    return result_list


def decode_list(val):
    """
    Decoding lists
    """
    val = list(val)
    val = val[1:-1]
    result_list = []
    for elem in val:
        result_list.append(decode(elem))
    return result_list


def encode_dict(val):
    if val == {}:
        return 'de'
    return 'd' + str(collapse([encode_str(key) + encode(val[key]) for key in sorted(val.keys())])) + 'e'


def decode_dict(val):
    pass