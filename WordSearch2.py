'''We use trie in this question, but i haven't learnt trie yet, so this is my tl e appraoch'''


def wordSearch2(board,words):
    m = len(board)
    n = len(board[0])

    output = []
    visited = set()


    def dfs(i,j,word):
        if len(word) == 0:
            return True

        if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[0]:
            return False

        temp = board[i][j]
        board[i][j] = '0'
        result = dfs(i+1,j,word[1:]) or dfs(i-1,j,word[1:]) or dfs(i,j+1,word[1:]) or dfs(i,j-1,word[1:])
        board[i][j] = temp
        return result

    for word in words:
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if word not in visited:
                        if dfs(i,j,word):
                            visited.add(word)
                            output.append(word)

    return output

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]

print(wordSearch2(board,words))