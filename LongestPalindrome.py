'''We have to return se length of the longest palindrome, the thing to keep in mind is that
In every palindrome there are even number of letter and maybe one odd, on this loginc our answer is based'''


def longestPalindrome(s):
    freq = set()

    for char in s:
        if char not in freq:
            freq.add(char)
        else:
            freq.remove(char)


    return len(s)-len(freq)+1 if len(freq)>0 else len(s)