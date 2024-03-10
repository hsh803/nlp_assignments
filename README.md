# nlp_labs
NLP labs from Language Technology Mater's program, Uppsala university

## 1. Tokenization and Sentence Segmentation

### Data
1) Tokenizer: tokenizer.py
- Precision/Recall are over 95%
3) Raw data: sentences_input.txt (from NLP course material, J. Sjons)
- Float numbers like 3.7 are treated as single tokens.
- Logograms like % and $ are treated as separate tokens.
- Contractions like it’s and don’t are split into two tokens.
- Double quotation marks (") have been changed to opening (‘‘) or closing (’’) quotation marks.
4) Tokenized data: tokens_output.txt
5) Gold standard: gold_standard.txt (from NLP course material, J. Sjons)
6) Measure precision, recall, F-score: socre score_tokens.py (from NLP course material, J. Sjons)

### Command lines
1) Tokenization
```
   python3 tokenizer.py < sentences_input.txt > tokens_output.txt
```
2) Get scores
```
  python3 socre score_tokens.py gold_standard.txt tokens_output.txt
```

## 2. Language modeling (SRILM toolkit)

