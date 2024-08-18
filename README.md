# Natural language processing
NLP course labs and assignments from Language Technology Mater's program, Uppsala university

## 1. Tokenization and Sentence Segmentation (Language: English)
- Improve simple tokenization to reach at least 95% precision and recall.
  
### Tokenizer and data
1) Tokenizer: tokenizer_simple.py (simple code, from NLP course material, J. Sjons), tokenizer.py (improved)
- Precision/Recall/F-score of improved tokenizer: over 95%
2) Raw data: sentences_input.txt
- Float numbers like 3.7 are treated as single tokens.
- Logograms like % and $ are treated as separate tokens.
- Contractions like it’s and don’t are split into two tokens.
- Double quotation marks (") have been changed to opening (‘‘) or closing (’’) quotation marks.
3) Tokenized data: tokens_output.txt
4) Gold standard: gold_standard.txt (Penn Tree bank standard)
5) Measure precision, recall, F-score: socre score_tokens.py

### Command lines
1) Tokenization
```
   python3 tokenizer.py < sentences_input.txt > tokens_output.txt
```
2) Get scores
```
  python3 socre score_tokens.py gold_standard.txt tokens_output.txt
```

## 2. Imporve lemmatization (Language: English)
- Improve simple lemmatizer to reach at least 85% accuracy

### Rule-based lemmatizer and data
1) Lemmatizer: lemmatizer_simple.py (simple code, from NLP course material, J. Sjons), lemmatizer.py (improved)
- Accuracy of improved lemmatizer: 89%
2) Input data: ewt-dev-wt.txt (English Web Treebank)
3) Lemmatized data: ewt-dev-out.txt
4) Gold standard: ewt-dev-wtl.txt (English Web Treebank)
5) Measure score: score_lemma.py

### Command lines
1) Lemmatize
```
python lemmatizer.py < ewt-dev-wt.txt > ewt-dev-out.txt
```

2) Get scores
```
python score.py lemma ewt-dev-wtl.txt ewt-dev-out.txt
```
