from collections import deque

def word_sequence (start, end, dictionary):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        word = path[-1]

        if word == end:
            return path
        
        for i in range(len(word)):
            for c in "abcdefghijklmnoppqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append(path + [new_word])

    return []


start = "hit"
end = "cog"
dictionary = {"hot","dot","dog","lot","log","cog"}

print(word_sequence(start, end, dictionary))