# Problem 69:
#     Totient Maximum
#
# Description:
#     Euler's Totient function, φ(n) [sometimes called the phi function],
#       is used to determine the number of numbers less than n which are relatively prime to n.
#     For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#
#         |  n |  Relatively Prime | φ(n) |   n/φ(n)  |
#         |----|-------------------|------|-----------|
#         |  2 | 1	               |  1   | 2         |
#         |  3 | 1, 2	           |  2   | 1.5       |
#         |  4 | 1, 3	           |  2   | 2         |
#         |  5 | 1, 2, 3, 4        |  4   | 1.25      |
#         |  6 | 1, 5              |  2   | 3         |
#         |  7 | 1, 2, 3, 4, 5, 6  |  6   | 1.1666... |
#         |  8 | 1, 3, 5, 7        |  4   | 2         |
#         |  9 | 1, 2, 4, 5, 7, 8  |  6   | 1.5       |
#         | 10 | 1, 3, 7, 9	       |  4   | 2.5       |
#
#     It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
#     Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

def main(n):
    """
    Returns the number `x` (≤ `n`) having the greatest inverse totient ratio, x/φ(x),
      as well as the ratio itself, and the totient function's value for `x`.

    Args:
        n (int): Natural number greater than 1

    Returns:
        (Tuple[int, float, int]):
            Tuple of ...
              * `x` (≤ `n`) having the greatest inverse totient ratio
              * Inverse totient ratio for `x`
              * Totient of `x`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 1

    # Keep track of totient function value per integer `i` using sieve method
    phi = [i for i in range(n+1)]

    for i in range(2, n+1):
        if phi[i] == i:
            # Found a prime number, so discount it from all multiples above
            for j in range(i, n+1, i):
                phi[j] -= phi[j] / i
        else:
            continue

    n_best = ratio_best = totient_best = 0
    for x in range(1, n+1):
        ratio_x = x / phi[x]
        if ratio_x > ratio_best:
            print('{} is better!'.format(x))
            n_best = x
            ratio_best = ratio_x
            totient_best = phi[x]

    return n_best, ratio_best, totient_best

    # # Idea:
    # #     Iterate up towards `n_max`.
    # #     Keep track of factors of each integer along the way.
    # #     Use factors of previous numbers to determine relative primeness.
    # #     Relatively prime numbers should only share 1 as a factor.
    #
    # n_best = totient_ratio_best = totient_best = 0
    #
    # # factors_by_num = {1: {1}}
    # for x in range(2, n_max+1):
    #     # x_factors = set()
    #     # x_mid = floor(sqrt(x)) + 1
    #     # for f in range(1, x_mid):
    #     #     if x % f == 0:
    #     #         x_factors.add(f)
    #     #         x_factors.add(x//f)
    #     #     else:
    #     #         continue
    #
    #     # Count relatively prime numbers below `x`
    #     x_totient = 0
    #     for y in range(1, x):
    #         if gcd(x, y) == 1:
    #             x_totient += 1
    #         # if len(x_factors.intersection(factors_by_num[y])) == 1:
    #         #     x_totient += 1
    #         # else:
    #         #     continue
    #
    #     # Check if inverse totient ratio is better
    #     x_ratio = x / x_totient
    #     if x_ratio > totient_ratio_best:
    #         print('{} is better!'.format(x))
    #         n_best = x
    #         totient_ratio_best = x_ratio
    #         totient_best = x_totient
    #
    #     # Keep track of x's factors for later
    #     # factors_by_num[x] = x_factors
    #
    # return n_best, totient_ratio_best, totient_best


if __name__ == '__main__':
    upper_limit = int(input('Enter a natural number (greater than 1): '))
    best_n, best_totient_ratio, relatively_prime_count = main(upper_limit)
    print('Number `n` (≤ {}) having greatest inverse totient ratio (n/φ(n)):'.format(upper_limit))
    print('  n      = {}'.format(best_n))
    print('  φ(n)   = {}'.format(relatively_prime_count))
    print('  n/φ(n) ≈ {.2f}'.format(best_totient_ratio))
