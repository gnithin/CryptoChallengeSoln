#!/usr/bin/env python
import base64
import challenge_3 as c3
import challenge_5 as c5

def hex_str_to_ascii_str(s):
    op_str = ""
    for i in xrange(0,len(s),2):
        op_str += chr(int(s[i:i+2],16))
    return op_str

def str_to_bin(s):
    return "".join([bin(ord(e))[2:].zfill(8)for e in s])
        
def hamming_distance(s1, s2):
    b1 = str_to_bin(s1)
    b2 = str_to_bin(s2)
    # Don't bother when the lengths are different
    if len(b1) != len(b2):
        return False
    
    hamming_dist = 0
    for i in xrange(len(b1)):
        if b1[i] != b2[i]:
            hamming_dist += 1
    return hamming_dist

def decrypt_str(s):
    s = base64.b64decode(s)

    # Step 1
    keysize_range = xrange(2, 41)

    # Step 3
    # Find the hamming distance between 1st and 2nd keysize
    # and 3rd and 4th
    keysize_ham_dist = {}
    for keysize in keysize_range:
        normalized_dist = sum(hamming_distance(s[i:i+keysize], s[i+keysize:i+(2*keysize)])/(keysize*1.0) for i in [0,(2*keysize)])/2
        keysize_ham_dist[keysize] = normalized_dist

    # Step 4
    keysize = min(keysize_ham_dist, key=keysize_ham_dist.get)

    # Step 5
    blocks = [s[i:i+keysize] for i in xrange(0,len(s),keysize)]

    # Step 6 transposing the block
    transpose_blocks =["" for _ in xrange(keysize)]
    for b in blocks:
        for i,e in enumerate(b):
            # Converting the value to hex
            transpose_blocks[i]+= hex(ord(e))[2:].zfill(2)

    # Step 7 - Solve single char XOR
    keys = ""
    for e in transpose_blocks:
        keys+=c3.decrypt_single_xor_str(e)[2]

    # Convert string to ASCII
    keys = hex_str_to_ascii_str(keys)

    # Step 8
    # repeated XOR key with s to get original message
    decrypted_str = c5.encrypt_repeating_xor(s, keys)

    return decrypted_str

    
if __name__ == "__main__":
    with open("challenge_6_ip.txt") as fp:
        ip = "".join([ip.strip() for ip in fp.readlines()])
    a = decrypt_str(ip)
    print len(a)

