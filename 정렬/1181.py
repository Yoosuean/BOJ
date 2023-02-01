#BOJ 1181 단어정렬
import sys
input=sys.stdin.readline
n=int(input())
words=[]

for _ in range(n):
    word=str(input())
    word_len=len(word)
    words.append((word,word_len))

words = list(set(words))

words.sort(key = lambda word: (word[1], word[0]))

for word in words:
    print(word[0],end='')