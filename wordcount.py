# -*- encoding=utf-8 -*-
# Run with: python wordcount.py my-file.ipynb
import sys
import json

wordCount = 0
filename = "Final Project.ipynb"
with open(filename, encoding='utf-8') as f:
    notebookRaw = f.read()
    notebookParsed = json.loads(notebookRaw)
    for cell in notebookParsed['cells']:
        if cell['cell_type'] == "markdown":
            contents = ''.join(cell['source'])
            words = contents.replace('#','').strip().split(' ')
            wordCount += len(words)
            print(words)
print(filename + ": {} words".format(wordCount))