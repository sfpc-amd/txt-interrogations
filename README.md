Txt Interrogations
====================

The idea is to extract questions and answers from movie scripts and mix them up. Possibly if I feel really ambitious I will use [videogrep](https://github.com/antiboredom/videogrep) to turn into a supercut. 

First try: _The Wolf of Wall St._ vs _The Great Gatsby_.

Usage
------


### Converting PDF to .txt

The quickest & easiest way I was able to do this was to use Automator on a Mac. See `bin/pdf2txt.workflow`. Currently it will simply output the text to your `Desktop` folder. This isn't the best solution but it gets the job done.

It would make sense to find a good python workflow for this, some possible resources:

 * http://code.activestate.com/recipes/511465-pure-python-pdf-to-text-converter/
 * http://victorwyee.com/python/convert-pdf-to-text-pypdf-pdfminer-first-impression/

Possible command-line solutions:

 * http://www.foolabs.com/xpdf/download.html