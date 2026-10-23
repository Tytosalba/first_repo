# This code obtains a 10 digit number in the format xxx-xxx-xxxx and changes any alphabetic characters to their numeric counterparts.

alph ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '2223334445556667778889999'
lookup = dict(zip(alph, num))

phone_number = str(input("Please enter a phone number in the format xxx-xxx-xxxx: "))

phone_conv = ''
for n in phone_number:
    if n.isalpha():
        phone_conv += lookup[n.upper()]
    else:
        phone_conv += n

print(phone_conv)