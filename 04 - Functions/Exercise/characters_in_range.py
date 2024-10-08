def characters(first, second):
    for i in range(ord(first) + 1, ord(second)):
        print(chr(i), end=" ")

first_chr = input()
second_chr = input()
characters(first_chr, second_chr)