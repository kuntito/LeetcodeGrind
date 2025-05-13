it was an LLD problem
i was told i'd be given a list of IP addresses
and they could be in one of three formats:

123.456.789.12
123.456.789.1-100
123.456.7890.0/16 or 123.456.7890.0/24

the third type stumped me and i'd need some explanation on IP addresses.
i've learnt that the set of numbers separated by periods are known as octets.

the input is a string of the following formats:
a plain IP address
an IP address where the last octet is a range

the third one is what confused me, my interviewer said, for 0/16
it meant the first two octets are constant and the last two are variable

and for 0/24, the first three octets are constant and the last one is variable

and given a sample input like ["123.456.789.12", "123.456.789.1-100", "123.456.7890.0/16", "123.456.7890.0/24"], i should store the addresses such that if given a new address, i can tell if it exists or not

i started with the first two types, since i understood them better.
the first IP address can simply be stored in a set.

and we can check new addresses for uniqueness using this set.

and for the second type, i'd use a hashmap.
the difference between both types is the last octet.

for type one, the octet is a digit and for type two the octet is a range, specifically it contains an hyphen
when storing the input, i can use string manipulation `rsplit` to obtain the last octet.

if it contains an hyphen, it's type 2 else type 1