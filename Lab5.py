# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n <= 0:
        return ""
    rows = []
    i = 1
    while i <= n:
        if i == 1 or i == n:   # first or last row = full stars
            line = "*" * n
        else:                  # middle rows = star + spaces + star
            line = "*" + " " * (n - 2) + "*"
        rows.append(line)
        i += 1
    return "\n".join(rows)


# 1
# 12
# 123
# 1234
def number_pattern(n):
    if n <= 0:
        return ""
    rows = []
    i = 1
    while i <= n:
        j = 1
        line = ""
        while j <= i:
            line += str(j)
            j += 1
        rows.append(line)
        i += 1
    return "\n".join(rows)


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    if n <= 0:
        return ""
    rows = []
    i = 1
    while i <= n:
        spaces = n - i
        stars = 2 * i - 1
        line = " " * spaces + "*" * stars
        rows.append(line)
        i += 1
    return "\n".join(rows)