
import os
import time

from openpyxl import load_workbook, Workbook
from os.path import exists

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


def removePunc(word):
    disallowed_chars = ' 1234567890.,;?!‘’“”"\'\xe2\x80\x9d\x99\x98\x9c'
    new_string = word
    for char in disallowed_chars:
        new_string = new_string.replace(char, '')
    return new_string

    # Accomplished&#8221;


# ? Interesting words in this case are long words without special characters
def letterCount(word):
    if len(word) < 7:
        return False
    else:
        return True


words_no_punc = list(map(removePunc, words))

words_filtered = list(filter(letterCount, words_no_punc))

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

# print(sorted_word_counts)

print('Checking if DataSheet exists... ' +
      str(exists('./data/DataSheet.xlsx')))

if(exists('./data/DataSheet.xlsx')):
    workbook = load_workbook(filename='./data/DataSheet.xlsx')
else:
    workbook = Workbook()


sheet = workbook['Sheet']

sheet['A1'] = 'Word'
sheet['B1'] = 'Count'
sheet['C1'] = 'Appears in'
sheet['D1'] = 'testing'

for i in sorted_word_counts:
    sheet['A' + str(sorted_word_counts.index(i) + 2)] = i['word']
    sheet['B' + str(sorted_word_counts.index(i) + 2)] = i['word_count']

print('Appended data...')


if(exists('./data/DataSheet.xlsx')):
    print('Removing file...')
    os.remove('./data/DataSheet.xlsx')
    time.sleep(0.5)
    print('Removed file')

workbook.save(filename='./data/DataSheet.xlsx')

print('Creating new xlsx file...')
print('Finished')
