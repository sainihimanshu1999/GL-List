'''In palindrome partitions, we have to check prefix and suffix'''

def palindromePartition(words):
    result = []
    dic = {w:i for i,w in enumerate(words)}

    for i,w in enumerate(words):
        for j in range(len(w)+1):
            prefix = w[:j]
            suffix = w[j:]

            if prefix == prefix[::-1] and suffix[::-1]!=w and suffix[::-1] in dic:
                result.append([dic[suffix[::-1]],i])

            if j!= len(w) and suffix==suffix[::-1] and prefix[::-1]!= w and prefix[::-1] in dic:
                result.append([i,dic[prefix][::-1]])


    return result

words = ["abcd","dcba","lls","s","sssll"]
print(palindromePartition(words))