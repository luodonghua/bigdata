#!/usr/bin/python2.7

import textract
text = textract.process("/home/donghua/source/email-sample.pdf")
print text
