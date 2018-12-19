import pandas as pd
import csv
import sys
maxInt = sys.maxsize
decrement = True

while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt / 10)
        decrement = True

if __name__ == '__main__':
    bs_training_data = []
    bs_sentence = ''
    bs_tags = ''
    with open("BMEStest.data", "r", encoding="utf-8") as csvfile:
        read = csv.reader(csvfile)
        for item in read:
            print(item)
            if len(item) != 0:
                if len(item[0]) != 0:
                    bs_sentence += item[0][0]
                    if len(item[0]) > 2:
                        bs_tags_data = item[0][2]
                    else:
                        bs_tags_data = item[0][len(item) - 1]
                    if bs_tags_data == 'B':
                        bs_tags += 'B'
                    elif bs_tags_data == 'M' or bs_tags_data == 'E':
                        bs_tags += 'I'
                    else:
                        bs_tags += 'O'
            else:
                train_item = (bs_sentence, bs_tags)
                bs_training_data.append(train_item)
                bs_sentence = ''
                bs_tags = ''
        print(bs_training_data)
        a = []
        b = []
        for sentence, tags in bs_training_data:
            a.append(sentence)
            b.append(tags)
    dataframe = pd.DataFrame({'a': a, 'b': b})
    dataframe.to_csv("test_BMES.csv", index=False, sep=',')

