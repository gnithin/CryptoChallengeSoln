#!/usr/bin/env python
import challenge_2 as c2

def bin_xor(a,b):
    op_str= ""
    for i in xrange(len(a)):
        op_str += str(int(a[i])^int(b[i]))
    return op_str


def encrypt_repeating_xor(s, key):
    bin_str = "".join(bin(ord(e))[2:].zfill(8) for e in s)

    key_counter = 0
    key_size = len(key)

    op_str = ""
    for i in xrange(0, len(bin_str), 8):
        bin_key = bin(ord(key[key_counter]))[2:].zfill(8)

        op_str += bin_xor(bin_key, bin_str[i:i+8])

        key_counter = (key_counter + 1)%key_size

    # Converting results to hex format
    hex_op_str = ""
    for j in xrange(0, len(op_str), 4):
        hex_op_str += hex(int(op_str[j:j+4],2))[2:]
    return hex_op_str

if __name__ == "__main__":
    ip_str = '''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
    key = "ICE"
    op_str = encrypt_repeating_xor(ip_str, key)
    expected_op_str = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''
    c2.assert_(op_str == expected_op_str)
