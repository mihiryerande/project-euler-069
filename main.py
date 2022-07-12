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

from typing import Tuple


def main(n: int) -> Tuple[int, float, int]:
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


if __name__ == '__main__':
    upper_limit = int(input('Enter a natural number (greater than 1): '))
    best_n, best_totient_ratio, relatively_prime_count = main(upper_limit)
    print('Number `n` (≤ {}) having greatest inverse totient ratio (n/φ(n)):'.format(upper_limit))
    print('  n      = {}'.format(best_n))
    print('  φ(n)   = {}'.format(relatively_prime_count))
    print('  n/φ(n) ≈ {.2f}'.format(best_totient_ratio))
