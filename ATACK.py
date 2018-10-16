import sqlite3
import fastDic
import sys
import re

_from = 1
_to = 93000
db_file = sys.argv[1]
outfile = sys.argv[2]

file = open(outfile , "w+")

db = sqlite3.connect(db_file)
db = db.cursor()

try:
    for word_id in range(_from , _to):
        try:
            print(word_id + ": " , end="")
            db.execute(f"SELECT * FROM english_words where english_word_id={word_id}")
            english_word = db.fetchone()
            english_word = re.search('\'(.*)\'' , str(english_word)).group(1)
            translated = fastDic.find_meaning(english_word)
            str_to_file = str(english_word) + ": " + str(translated) + "\n"
            print (str_to_file)
            file.write(str_to_file)
        except KeyboardInterrupt:
            file.close()
            print("KeyboardInterrupt")
            sys.exitx(0)
        except :
            pass
except KeyboardInterrupt:
    file.close()
    print("KeyboardInterrupt")
file.close()
