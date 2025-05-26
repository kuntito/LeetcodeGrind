arr = [
    ["Year:Month:Day:Hour:Minute:Second", "2016:01:01:01:01:01", "2017:01:01:23:00:00"]
]

split_cols = lambda x: x.split(":")

for zero, one, two in arr:
    lst_zero = split_cols(zero)
    lst_one = split_cols(one)
    lst_two = split_cols(two)

    for z, a, b in zip(lst_zero, lst_one, lst_two):
        print(f"{z} {a} {b}")
