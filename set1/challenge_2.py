#!/usr/bin/env python

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

def xor(a, b):
    '''
    xor(str, str) => str
    Takes in 2 hex strings and returns a hex string 
    which is a xor of the 2.
    '''
    # Helper function to convert hex to bin
    hex_to_bin = lambda x:"".join((bin(int(e,16))[2:]).zfill(4) for e in x)
    a = hex_to_bin(a)
    b = hex_to_bin(b)
    c = "" 
    for i in xrange(len(a)):
        c += str(int(a[i]) ^ int(b[i]))
    d = ""
    for j in xrange(0,len(c),4):
        d += str(hex(int(c[j:j+4], 2)))[2:]
    return d 

if __name__ == "__main__":
    ip_str_1 = "1c0111001f010100061a024b53535009181c"
    ip_str_2 = "686974207468652062756c6c277320657965"
    
    op_str = xor(ip_str_1, ip_str_2)

    expected_op_str = "746865206b696420646f6e277420706c6179"

    assert_(op_str == expected_op_str)
