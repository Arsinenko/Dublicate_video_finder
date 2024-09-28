import binascii
import imagehash

def hash_to_bytearray(img_hash):
    return bytearray.fromhex(str(img_hash))

def bytearray_to_hash(bytea):
    hash_as_str = binascii.hexlify(bytea)
    return imagehash.hex_to_hash(hash_as_str)
