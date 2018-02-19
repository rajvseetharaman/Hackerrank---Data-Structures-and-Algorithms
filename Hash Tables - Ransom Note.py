from collections import Counter
def ransom_note(magazine, ransom):
    if len(magazine) < len(ransom):
        return False
    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransom)
    for word, count in ransom_counter.items():
        if word not in magazine_counter or magazine_counter.get(word) < count:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
