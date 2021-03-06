#!/usr/bin/env python

import sys

def assert_(bool_val, print_val=''):
    '''
    assert(boolean, [str]) => None
    This is a helper function to help assert values.
    eg- assert_(1==2)
    '''
    try:
        assert bool_val
    except AssertionError:
        print "Assertion Failed -\n" + print_val
    else:
        print "Assertion Passed -\n" + print_val
    print "-"*30 + "\n"

def lib_hex_to_base64(hex_str):
    '''
    lib_hex_to_base64(str) => str
    This is a function using python built-ins.
    This will be used for testing the custom function.
    This takes as input hex string and produces a base64 string.
    '''
    # Two ways to do this - 
    # 1. Using str.encode()
    # Vanilla str.encode("base64") adds a trailing "\n"
    # character. Documented [here](http://bugs.python.org/issue17714)
    # That's why strip() is needed
    # hex_str.decode("hex").encode("base64").strip()
    # 
    # 2. Using base64 lib(Works out of the box)
    import base64
    return base64.b64encode(hex_str.decode("hex"))

def hex_to_base64(hex_str):
    '''
    hex_to_base64(str) => str
    Custom function to convert hex to base64.
    '''
    # Simple algorithm explanation [here](http://www.herongyang.com/encoding/Base64-Encoding-Algorithm.html)
    ## Helper function 
    def bin_to_base_64_map(int_val):
        helper = lambda l,u:[chr(i) for i in xrange(ord(l),ord(u) + 1)]
        con_map = helper('A','Z') + \
                helper('a', 'z') + \
                helper('0', '9') + \
                ['+', '/']
        return con_map[int_val]
    ##

    bin_str = ""
    for e in hex_str:
        # have to convert hex to bin and keep it at length
        # for 4 bits (A really difficult to find bug :P)
        bin_str += (bin(int(e,16))[2:]).zfill(4)

    # Checking the amount of padding
    num_padding = ((len(hex_str)/2) % 3)
    if num_padding:
        num_padding = 3 - num_padding

    # Adding the padding
    bin_str += "0"*(8 * num_padding)

    base64_str = ""

    # Take it in blocks of 24 Bits
    for i in xrange(0, len(bin_str), 24):
        b_24 = bin_str[i:i+24]

        #Take it in blocks of 6 bits
        for j in xrange(0, len(b_24), 6):
            b_6 = b_24[j:j+6]
            base64_str += bin_to_base_64_map(int(b_6, 2))
    
    # override the padding bytes with `=`
    subs = "="*(num_padding)
    base64_str = base64_str[:(len(base64_str) - len(subs))] +  subs
    return base64_str


if __name__ == "__main__":
    base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    ip_hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    # Testing the output given in matasano website
    assert_(hex_to_base64(ip_hex_str) == base64_str, ip_hex_str)

    # Testing other examples from the wikipedia page. 
    wiki_example_list = [
            '''Man is distinguished, not only by his reason, but by this singular passion from
    other animals, which is a lust of the mind, that by a perseverance of delight
    in the continued and indefatigable generation of knowledge, exceeds the short
    vehemence of any carnal pleasure.''',
            "any carnal pleasure",
            "any carnal pleasur",
            "any carnal pleasu",
            "any carnal pleas",
    ]

    for eg in wiki_example_list:
        hex_str = eg.encode("hex")
        op = hex_to_base64(hex_str)
        expected_op = lib_hex_to_base64(hex_str)
        assert_(op == expected_op, eg)
