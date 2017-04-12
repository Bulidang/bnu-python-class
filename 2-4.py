speech = '''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
   Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''
s = speech.split()
wordlist = []
for i in s:
    word = i.lower().strip('-,.')
    if word:
        wordlist.append(word)
uniqWord = set(wordlist)


with open('Declaration.txt') as f:
    s = f.read()
s = s.split()
wordlist2 = []
for i in s:
    word = i.lower().strip('-:;,.')
    if word:
        wordlist2.append(word)
uniqWord2 = set(wordlist2)

u = uniqWord | uniqWord2
i = uniqWord & uniqWord2
d = uniqWord - uniqWord2
rd = uniqWord2 - uniqWord
print('所用单词数量分别为{}和{}'.format(len(uniqWord), len(uniqWord2)))
print('两篇文章一起所用单词数量为{}'.format(len(u)))
print('两篇文章共用单词数量为{}'.format(len(i)))
print('文章1有但文章2没有的单词数量为{}'.format(len(d)))
print('文章1没有但文章2有的单词数量为{}'.format(len(rd)))
print('两篇文章共有的单词：')
ilist = list(i)
ilist.sort()
for i in range(0, len(ilist), 5):
    for j in ilist[i:i+5]:
        print('{:<20}'.format(j), end='')
    print()