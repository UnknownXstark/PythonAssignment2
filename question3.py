import string
from collections import defaultdict

def anagram (sentences):
    groups = defaultdict(list)

    def normalize(s):
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return ''.join(sorted(cleaned))

    for sentence in sentences:
        key = normalize(sentence)
        groups[key].append(sentence)

    return list(groups.values())

sentences = ['Listen to me', 'Enlist to me', 'The eyes', 'They see']
print(anagram(sentences))