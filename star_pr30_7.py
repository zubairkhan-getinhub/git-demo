# 1. Print a 5x5 grid of asterisks.

for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()
# 2. Print a right triangle of asterisks with a height of 5.
# 
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()
# 3. Print an inverted right triangle of asterisks with a height of 5.

for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
# print('4. Print a pyramid of asterisks with a height of 5.')

for i in range(5):
    for j in range(5-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()
# print('5. Print an inverted pyramid of asterisks with a height of 5.')

for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(2*i-1):
        print('*', end=' ')
    print()
# 6. Print a hollow square of asterisks with a side length of 5.

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# print("7. Print a hollow right triangle of asterisks with a height of 5.")

for i in range(1, 6):
    for j in range(1, i+1):
        if j == 1 or j == i or i == 5:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 8. Print a diamond of asterisks with a height of 5.

for i in range(3):
    for j in range(3-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()
for i in range(2, -1, -1):
    for j in range(3-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()
# 9. Print a hollow diamond of asterisks with a height of 5.

for i in range(3):
    for j in range(3-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        if k == 0 or k == 2*i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(2, -1, -1):
    for j in range(3-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        if k == 0 or k == 2*i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 10. Print a checkerboard pattern of 8x8.

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 11. Print the multiplication table up to 5x5.

for i in range(1, 6):
    for j in range(1, 6):
        # print(i * j, end=' ')
        print(f'{i * j:2}', end=' ')
    print()
# 12. Print numbers in a pyramid pattern.

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()
# 13. Print a Floyd's triangle with 5 rows.

num = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print()
# 14. Print Pascal's triangle with 5 rows.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(5):
    for j in range(5-i-1):
        print(' ', end=' ')
    for k in range(i+1):
        print(factorial(i) // (factorial(k) * factorial(i - k)), end=' ')
    print()
# 15. Print a mirrored right triangle of asterisks with a height of 5.

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()
# 16. Print a hollow mirrored right triangle of asterisks with a height of 5.

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(i):
        if k == 0 or k == i-1 or i == 5:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
# 17. Print a pyramid of numbers.

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(k, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()
# 18. Print a diamond of numbers.

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(k, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()
for i in range(4, 0, -1):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(k, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()
# 19. Print a square of numbers with side length 5.

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()
# 20. Print a square of numbers with ascending numbers in each row.
print()
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=' ')
    print()
print()
# 22. Print an inverted right triangle of numbers.

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
# 23. Print a hollow square of numbers with side length 5.

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
print()
# 24. Print a checkerboard pattern of numbers with 8x8 grid.

for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
print()
# 25. Print a number pattern with alternating rows.

for i in range(1, 6):
    for j in range(1, 6):
        if i % 2 == 0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
# 26. Print a spiral matrix of size 5x5.

def spiralPrint(m, n, a):
    k = 0
    l = 0
    while k < m and l < n:
        for i in range(l, n):
            print(a[k][i], end=' ')
        k += 1
        for i in range(k, m):
            print(a[i][n - 1], end=' ')
        n -= 1
        if k < m:
            for i in range(n - 1, l - 1, -1):
                print(a[m - 1][i], end=' ')
            m -= 1
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=' ')
            l += 1

a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]

spiralPrint(5, 5, a)
# 27. Print a multiplication table from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i*j:2}', end=' ')
    print()
# 28. Print a reverse pyramid of numbers with a height of 5.

for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(i):
        print(i, end=' ')
    print()
# 29. Print an hourglass pattern with numbers.

for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(i):
        print(i, end=' ')
    print()
for i in range(2, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(i):
        print(i, end=' ')
    print()
# 30. Print a square pattern of alternating numbers 0 and 1.

for i in range(5):
    for j in range(5):
        print((i+j) % 2, end=' ')
    print()
# 31. Print a binary right-angled triangle of height 5.

for i in range(1, 6):
    for j in range(1, i+1):
        print(j % 2, end=' ')
    print()
# 32. Print an ASCII art square of size 5 with different characters.

chars = ['@', '#', '$', '%', '&']
for i in range(5):
    for j in range(5):
        print(chars[j], end=' ')
    print()
# 33. Print an ASCII art pyramid of characters.

chars = ['A', 'B', 'C', 'D', 'E']
for i in range(5):
    for j in range(5-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print(chars[i], end=' ')
    print()
# 34. Print a hollow square of side length 5 using '@'.

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('@', end=' ')
        else:
            print(' ', end=' ')
    print()
# 35. Print a square of numbers in ascending order from 1 to 5.

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=' ')
    print()
# 36. Print a pattern of numbers increasing from 1 to 5 and then decreasing back to 1.

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    for k in range(i-1, 0, -1):
        print(k, end=' ')
    print()
# 37. Print a pyramid of numbers where each row has consecutive numbers.

num = 1
for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end=' ')
    for k in range(i):
        print(num, end=' ')
        num += 1
    print()
# 38. Print a half diamond pattern of numbers.

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
for i in range(4, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
# 39. Print an hourglass pattern using numbers with descending order.

for i in range(5, 0, -1):
    for j in range(5, 5-i, -1):
        print(j, end=' ')
    print()
for i in range(2, 6):
    for j in range(5, 5-i, -1):
        print(j, end=' ')
    print()
# 40. Print a diamond pattern with numbers.

for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(k, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()
for i in range(4, 0, -1):
    for j in range(1, 6-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print(k, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()
# 41. Print a number pattern in a zigzag shape.

for i in range(1, 10):
    for j in range(1, 10):
        if (i + j) % 2 == 0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
# 42. Print a pyramid with an inverted pattern of asterisks.

for i in range(5, 0, -1):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(2*i-1):
        print('*', end=' ')
    print()
# 43. Print a half pyramid using numbers from 5 to 1.

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
# 44. Print an inverted half pyramid of numbers.

for i in range(1, 6):
    for j in range(1, 6-i+1):
        print(j, end=' ')
    print()
# 45. Print a binary triangle pattern.

for i in range(1, 6):
    for j in range(1, i+1):
        print(j % 2, end=' ')
    print()
# 46. Print a pattern of alternating rows of 0 and 1.

for i in range(1, 6):
    for j in range(1, 6):
        print(i % 2, end=' ')
    print()
# 47. Print a diamond pattern of letters.

chars = ['A', 'B', 'C', 'D', 'E']
for i in range(5):
    for j in range(5-i-1):
        print(' ', end=' ')
    for k in range(i+1):
        print(chars[k], end=' ')
    for l in range(i-1, -1, -1):
        print(chars[l], end=' ')
    print()
for i in range(3, -1, -1):
    for j in range(5-i-1):
        print(' ', end=' ')
    for k in range(i+1):
        print(chars[k], end=' ')
    for l in range(i-1, -1, -1):
        print(chars[l], end=' ')
    print()
# 48. Print a square pattern of incremented numbers.

for i in range(5):
    for j in range(5):
        print(j+i+1, end=' ')
    print()
# 49. Print a mirrored right triangle pattern using numbers.

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(1, i+1):
        print

# 51. Print a triangle of numbers.

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
# 52. Print a triangle of asterisks with increasing spaces.

for i in range(1, 6):
    for j in range(5 - i):
        print(' ', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()
