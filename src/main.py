from itertools import count


with open('data/doc1.txt', 'r') as f:
    doc1 = f.read()

with open('data/doc2.txt', 'r') as f:
    doc2 = f.read()

with open('data/doc3.txt', 'r') as f:
    doc3 = f.read()

with open('data/doc4.txt', 'r') as f:
    doc4 = f.read()

with open('data/doc5.txt', 'r') as f:
    doc5 = f.read()

with open('data/doc6.txt', 'r') as f:
    doc6 = f.read()

documents = [doc1, doc2, doc3, doc4, doc5, doc6]

all_docs = doc1 + ' ' + doc2 + ' ' + doc3 + ' ' + doc4 + ' ' + doc5 + ' ' + doc6


words = all_docs.split()


# ! encoding errors like "\xe2\x80\x99" are currently being printed to console
def removePunc(word):
    disallowed_chars = ' 1234567890.,;?!\"\'\xe2\x80\x9d\x99\x98\x9c'
    new_string = word
    for char in disallowed_chars:
        new_string = new_string.replace(char, '')
    return new_string


# ? Interesting words in this case are long words without special characters "-" or " ' "
def letterCount(word):
    if len(word) < 7:
        return False
    else:
        return True


words_no_punc = map(removePunc, words)

words_filtered = filter(letterCount, words_no_punc)


unique_list = []


def find_unique(word):
    if word not in unique_list:
        unique_list.append(word)


for word in words_filtered:
    find_unique(word)

sorted_words = sorted(unique_list)


def wordCount(word):
    count = 0
    for i in words_filtered:
        if word in i:
            count += 1
    return {"word": word, "word_count": count}


word_counts = map(wordCount, sorted_words)

sorted_word_counts = sorted(
    word_counts, key=lambda d: d['word_count'], reverse=True)


print(sorted_word_counts)
