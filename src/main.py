with open('data/doc1.txt') as f:
    doc1 = f.read()

with open('data/doc2.txt') as f:
    doc2 = f.read()

with open('data/doc3.txt') as f:
    doc3 = f.read()

with open('data/doc4.txt') as f:
    doc4 = f.read()

with open('data/doc5.txt') as f:
    doc5 = f.read()

with open('data/doc6.txt') as f:
    doc6 = f.read()

doc1_word_list = doc1.split()


def letterCount(x):
    if len(x) < 6:
        return False
    else:
        return True


doc1_list_sorted = filter(letterCount, doc1_word_list)


print('------------------unsorted----------------- :', doc1_word_list,
      '-----------------sorted------------------------- :', doc1_list_sorted)

# print(doc1, doc2, doc3, doc4, doc5, doc6)
