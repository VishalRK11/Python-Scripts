## Video Lectures: https://www.youtube.com/watch?v=V-sEwsca1ak
## Code Source: https://en.wikipedia.org/wiki/Longest_palindromic_substring

## Key Points:
    # Case 1: Totally contained under the current palindrome (Line 33-35)
    # Case 2: Palindrome expands till the right edge and it's mirror expands the till the left edge. This case forms a perfect prefix and is made as the centre. [Lines: 39-51]
    # Case 3: Palindrome expands till the right edge and it's mirror expands beyond the left edge. [Lines: 39-42]


def add_boundaries(s):
    ret = []
    for c in s:
        ret.extend(['$', c])
    ret.append('$')
    return "".join(ret)


def remove_boundaries(s):
    return s.replace('$', '')


def find_longest_palindromic_substring(s):
    s = add_boundaries(s)
    p = [0] * len(s)

    c, r, n, m = 0, 0, 0, 0

    for i in range(1, len(s)):
        if i > r:
            p[i] = 0
            m, n = i-1, i+1

        else:
            i2 = 2*c-i
            if p[i2] < r-i-1:
                p[i] = p[i2]
                m = -1
            else:
                p[i] = r-i
                n = r+1
                m = 2*i-n

        while m >= 0 and n < len(s) and s[m] == s[n]:
            p[i] += 1
            m -= 1
            n += 1

        if i+p[i] > r:
            c = i
            r = i+p[i]

    max_len = max(p)
    max_idx = p.index(max_len)

    max_palindromic_substring = s[max_idx-max_len:max_idx+max_len+1]
    return remove_boundaries(max_palindromic_substring)

def manachers_algorithm():
    s = input()
    return find_longest_palindromic_substring(s)


def main():
    print(manachers_algorithm())


if __name__ == '__main__':
    main()