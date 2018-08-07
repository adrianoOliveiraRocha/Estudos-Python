import numba

# install: pip3 install numba

# Just-in-time (JIT) compiling is a method of dynamically compiling (parts) an 
# application during runtime

@numba.jit
def sum(numbers):
    total = 0.0
    for value in numbers:
        total += value
    return total

numbers = [2, 3, 5, 6, 76, 56]
print(sum(numbers)

