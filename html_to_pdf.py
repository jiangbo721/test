#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project: test
# author: liujiangbo
# file: html_to_pdf.py
# ide: PyCharm
# time: 2019-09-08 17:19


#########demo 1 ############
from html2pdf import HTMLToPDF

path = '/Users/mac/Downloads/test.pdf'
HTML = """
    <!DOCTYPE html>
    <html>
        <body>
        <h1>Hello World</h1>
        </body>
    </html>
"""
with open(path, 'wb') as f:
    h = HTMLToPDF(HTML, f)


#########demo 2 #############
from wkhtmltopdf import HTMLURLToPDF

make_pdf = HTMLURLToPDF(
    url='http://www.example.com',
    output_file='~/example.pdf',
)
make_pdf.render()