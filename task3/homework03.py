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

from django.conf import settings

if not settings.configured:
    settings.configure(
        # DEBUG=True,
        # ROOT_URLCONF=__name__,
    )

def encode(val):
    if type(val) == int:
        return encode_int(val)
    else: 
        return encode_str(val)
   
def decode(val):
    if str(val)[0] == 'i':
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
    if len(val) == 0:
        return b'0:'
    val = val.decode('utf-8')
    res = str(len(val)) + ':' + val
    return str.encode(res, 'utf-8')

def decode_str(val):
    """
    Decoding string value
    """
    val = val.decode('utf-8')
    return (str(val)[(str(val).find(':'))+1:]).encode()

print(encode('b\x80'))
print(decode(encode('\x80')))