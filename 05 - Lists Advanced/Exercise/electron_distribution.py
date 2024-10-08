distributed_el = []
shell = 0
num_e = int(input())
while num_e > 1:
    shell += 1
    shell_nums = 2 * (shell**2)
    if num_e < shell_nums:
        shell_nums = num_e
        num_e = 0
    else:
        num_e -= shell_nums
    distributed_el.append(shell_nums)
print(distributed_el)