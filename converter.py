import binascii
import imagehash

def hash_to_bytearray(img_hash):
    return bytearray.fromhex(str(img_hash))

def bytearray_to_hash(bytea):
    hash_as_str = binascii.hexlify(bytea)
    return imagehash.hex_to_hash(hash_as_str)

def chunked(size, source):
    for i in range(0, len(source), size):
        yield source[i:i+size]

def hash_bytearray_to_hashes_array(byteshash):
    hashesbytes = list(chunked(32, byteshash))

    hashes = []
    for elem in hashesbytes:
        hashes.append(bytearray_to_hash(elem))