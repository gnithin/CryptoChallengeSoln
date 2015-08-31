#!/usr/bin/env python
import challenge_3 as c3

if __name__ == "__main__":
    with open("challenge_4_ip.txt") as fp:
        ipList =[ip.strip() for ip in fp.readlines() if ip.strip() != ""]

    max_count = -1
    max_str = ""
    for i,ip in enumerate(ipList):
        print "\nProcessing line Number "+str(i)
        count, op_str = c3.decrypt_single_xor_str(ip)
        if count > max_count:
            max_count = count
            max_str = op_str
            print "Max : count - "+str(max_count) +"\nstr: "+ max_str
        print "-"*30 + "\n"
    
    print "\n\n"
    print "The string that was single char XOR'ed was - \n"
    print max_str
