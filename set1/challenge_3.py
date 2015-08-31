#!/usr/bin/env python
import challenge_2 as c2

def decrypt_single_xor_str(s):
    freq_dict = {}
    for j in xrange(256):
        decrypted_str = ""
        xor_key = hex(j)[2:].zfill(2)
        freq_dict[xor_key] = {}
        freq_dict[xor_key]["count"] = 0

        for i in xrange(0,len(s),2):
            encrypted_str = s[i:i+2]
            decrypted_str += c2.xor(encrypted_str, xor_key)

        decrypted_str = decrypted_str.decode("hex")
        freq_dict[xor_key]["str"] = decrypted_str

        for e in decrypted_str:
            if e.isalpha() or e == " ":
                freq_dict[xor_key]["count"] += 1

    #Finding the maximum count
    max_count = -1
    max_str = ""
    for k in freq_dict:
        if int(freq_dict[k]["count"]) > max_count:
            max_count = freq_dict[k]["count"]
            max_str = freq_dict[k]["str"]

    return max_count, max_str

if __name__ == "__main__":
    ip_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    print decrypt_single_xor_str(ip_str)
