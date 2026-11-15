#scissor

alphabet = "abcdefghijklmnopqrstuvwxyz "
alphabetlist = list(alphabet)
numberlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
# alphabet += alphabet*2
# skibidi = 26

string_tuff = input("Please type in a string: ")
other_string = []
a = 0
b = 0
while a < len(string_tuff):
    while b < 26:
        if string_tuff[a] == alphabet[b]:
            other_string += numberlist[b]
        b += 1
    a += 1
print(other_string)