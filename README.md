Txt Interrogations
====================

The idea is to extract questions and answers from movie scripts and mix them up. Possibly if I feel really ambitious I will use [videogrep](https://github.com/antiboredom/videogrep) to turn into a supercut. 

First try: _The Wolf of Wall St._ vs _The Great Gatsby_.

Setup
-----

```bash
 $ pip -r requirements.pip
```

Usage
------

### Extracting dialogue from screenplay PDFs

We're using the [pdfminer](https://github.com/euske/pdfminer) library to extract dialogue from movie script PDFs. The scripts follow a standard formatting, but it's based on layout rather than text. So we need to be able to extract text based on margins, etc. `extract_dialogue.py` will take the path to a PDF file as the first argument, and simply grab all of the dialogue text and output to `stdin`. Example usage:

```bash
 $ python extract_dialogue.py data/Great-Gatsby.pdf > data/Great-Gatsby_dialogue.txt
```

PDFminer:

 * https://github.com/euske/pdfminer
 * https://euske.github.io/pdfminer/programming.html
