# 1. Right-Angled Triangle Star Pattern
# markdown
# Copy code
# *
# **
# ***
# ****
# *****
# Code:

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print('*' * i)
print('* * * * * *')
# 2. Inverted Right-Angled Triangle Star Pattern
# markdown
# Copy code
# *****
# ****
# *** 
# **
# *
# Code:

# python
# Copy code
n = 5
for i in range(n, 0, -1):
    print('* ' * i)
# 3. Isosceles Triangle Star Pattern
# markdown
# Copy code
#     *
#    ***
#   *****
#  *******
# *********
# Code:

# python
# Copy code
print('      allah       ')
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print('      allah       ')
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print(' ' * (5 - 1) + '*' * (2 * 1 - 1))
print(' ' * (5 - 2) + '*' * (2 * 2 - 1))
print(' ' * (5 - 3) + '*' * (2 * 3 - 1))
print(' ' * (5 - 4) + '*' * (2 * 4 - 1))
print(' ' * (5 - 5) + '*' * (2 * 5 - 1))
print("bismillahbismillahbismillahbismillahbismillah")
print('    '+'*' * 1)
print('   '+'*' * 3)
print('  '+'*' * 5)
print(' '+'*' * 7)
print(''+'*' * 9)
print("bismillahbismillahbismillahbismillahbismillah")
print("bismillahbismillahbismillahbismillahbismillah")
print(' ' * 4 + '*' * 1)
print(' ' * 3 + '*' * 3)
print(' ' * 2 + '*' * 5)
print(' ' * 1 + '*' * 7)
print(' ' * 0 + '*' * 9)
print("bismillahbismillahbismillahbismillahbismillah")
print("bismillahbismillahbismillahbismillahbismillah")
print('    *')
print('   ***')
print('  *****')
print(' *******')
print('*********')
# 4. Inverted Isosceles Triangle Star Pattern
# markdown
# Copy code
# *********
#  *******
#   *****
#   ****
#   ***
#    **
#     *
# Code:

# python
# Copy code
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print('      allah       ')
# 5. Diamond Star Pattern
# markdown
# Copy code
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# Code:

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print('      allah       ')
# 6. Hollow Diamond Star Pattern
# markdown
# Copy code
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# Code:

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))
for i in range(n - 1, 0, -1):

    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))

print('bismillahbismillahbismillahbismillahbismillahbismillahbismillah')
print(' ' * 4  +  '*'         + ' ' * -1          + ('*' if 1 != 1 else ''))
print(' ' * 3  +  '*'         + ' ' *  1          + ('*' if 2 != 1 else ''))
print(' ' * 2  +  '*'         + ' ' *  3          + ('*' if 3 != 1 else ''))
print(' ' * 1  +  '*'         + ' ' *  5          + ('*' if 4 != 1 else ''))
print(' ' * 0  +  '*'         + ' ' *  7          + ('*' if 5 != 1 else ''))
print(' ' * 1  +  '*'         + ' ' *  5          + ('*' if 4 != 1 else ''))
print(' ' * 2  +  '*'         + ' ' *  3          + ('*' if 3 != 1 else ''))
print(' ' * 3  +  '*'         + ' ' *  1          + ('*' if 2 != 1 else ''))
print(' ' * 4  +  '*'         + ' ' * -1          + ('*' if 1 != 1 else ''))



n = 5
for i in range(1, n + 1):
    print('*' * i)
# . Inverted Right-Angled Triangle Star Pattern
# markdown
# Copy code
# *****
# ****
# ***
# **
# *
# Code:

# python
# Copy code
n = 5
for i in range(n, 0, -1):
    print('*' * i)
# 3. Isosceles Triangle Star Pattern
# markdown
# Copy code
#     *
#    ***
#   *****
#  *******
# *********
# Code:

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
# 4. Inverted Isosceles Triangle Star Pattern
# markdown
# Copy code
# *********
#  *******
#   *****
#    ****
#    ***
#    **
#     *
# Code:

# python
# Copy code
n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
# 5. Diamond Star Pattern
# markdown
# Copy code
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# Code:

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
# 6. Hollow Diamond Star Pattern
# markdown
# Copy code
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# Code: 

# python
# Copy code
n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i != 1 else ''))