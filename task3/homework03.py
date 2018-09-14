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
    elif type(val) == str: 
        return encode_str(val)
    elif type(val) == bytes:
        return encode_byte(val)

def decode(val):
    if get_type(val) == int:
        return decode_int(val)
    elif get_type(val) == str:
        return decode_str(val)
    elif get_type(val) == bytes:
        return decode_byte(val)

def get_type(val):
    # val = val.decode('utf-8')
    if val == None:
        return
    if str(val)[0] == "i":
        return int
    elif str(val)[0].isdigit():
        return str
    elif str(val)[0] == 'b':
        return bytes

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
    return str(len(val)) + ":" + val

def decode_str(val):
    """
    Decoding string value
    """
    return str(val)[(str(val).find(':'))+1:].encode()

def encode_byte(val):
    """
    Encoding bytes values
    """
    # if val == None or val == b'':
    #     return '0:\'\''
    # if type(val) == bytes:
    result = bytearray()
    result += str.encode(str(len(val)))
    result += b':'
    result += val
    return bytes(result)
    # return str(len(val)) + ":" + val

def decode_byte(val):
    # if val == None or val == '0:':
    #     return b''
    return str(val)[(str(val).find(':'))+1:-1].encode()   



# print(encode('asd3').decode('utf-8'))
# print(decode('4:asd3').decode('utf-8'))
# print(encode(b'asd3'))
# print(decode(b'4:asd3'))
# print(encode(None))
# print(encode(b''))
# print(decode(None))
# print(encode(b''))
# print(decode(b'0:'))
# print(encode(b'spam'))
# print(decode(b'4:spam'))
# print(encode(None))
# print(decode(None))
# print(b'\\x00'.hex())
# print(ord('\x00'))

# print(encode(b'0'))
# print(decode(b'1:0'))

print(encode(b'\x00'))
# print(decode(b'1:0'))