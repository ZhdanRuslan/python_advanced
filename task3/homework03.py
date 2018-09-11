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

def encode(val):
    if get_type(val) == 'int':
        encode_int(val)
    elif get_type(val) == 'str':
        encode_str(val)

def decode(val):
    if get_type(val) == 'int':
        decode_int(val)
    elif get_type(val) == 'str':
        decode_str(val)

def get_type(val):
    if val[0] == "i":
        return int
    elif val[0].isdigit():
        return str
    
def encode_str(val):
    """
    Encoding string values
    """
    return str(len(val)) + ":" + val

def decode_str(val):
    """
    Decoding string value
    """
    return str(val)[(str(val).find(':'))+1:]

print(decode_str('8:asdasdasdasd'))

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
