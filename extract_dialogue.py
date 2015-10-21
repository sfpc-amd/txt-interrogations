import sys
import inspect
import unicodedata
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice #, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import PDFPageAggregator
# from pdfminer.cmapdb import CMapDB
# from pdfminer.image import ImageWriter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar

DIALOGUE_BBOX_MIN = 150
DIALOGUE_BBOX_MAX = 300;

laparams = LAParams()
rsrcmgr = PDFResourceManager()

def setup(path):
	# Open a PDF file.
	fp = open(path, 'rb')
	# Create a PDF parser object associated with the file object.
	parser = PDFParser(fp)
	# Create a PDF document object that stores the document structure.
	# Supply the password for initialization.
	document = PDFDocument(parser)
	# Check if the document allows text extraction. If not, abort.
	if not document.is_extractable:
	    raise PDFTextExtractionNotAllowed
	# Create a PDF device object.
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	# Create a PDF interpreter object.
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	# Process each page contained in the document.

	# now extract dialogue from 
	for i, page in enumerate(PDFPage.create_pages(document)):
		# skip the title page
		if i > 0:
			# process page with interpreter
			interpreter.process_page(page)
			# get layout info
			layout = device.get_result()
			# iterate through layout objects
			for obj in layout:
				# we only want to bother with LTTextBox and LTTextLine
				if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine):
					# only extract text segments within a certain margin range
					if obj.bbox[0] > DIALOGUE_BBOX_MIN and obj.bbox[0] < DIALOGUE_BBOX_MAX:
						# need to convert unicode characters
						converted = unicodedata.normalize('NFKD', obj.get_text()).encode('ascii', 'ignore')
						print(converted)


# run program
if len(sys.argv) > 1:
	setup(sys.argv[1])