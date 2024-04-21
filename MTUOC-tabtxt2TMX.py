#!/usr/bin/python3
#    MTUOC-tabtxt2TMX
#    Copyright (C) 2024  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import codecs
from xml.sax.saxutils import escape
import unicodedata

import argparse

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

parser = argparse.ArgumentParser(description='MTUOC-tabtxt2TMX: A script to convert a parallel corpus in tabbed text into a TMX file.')
parser.add_argument('-i','--input', action="store", dest="fentrada", help='The input file to convert.',required=True)
parser.add_argument('-o','--output', action="store", dest="fsortida", help='Fix some issues in PDF conversion.',required=True)

parser.add_argument('-s','--L1code', action="store", dest="l1", help='The language code for the source language.',required=True)

parser.add_argument('-t','--L2code', action="store", dest="l2", help='The language code for the target language.',required=True)

args = parser.parse_args()
fentrada=args.fentrada
fsortida=args.fsortida
l1=args.l1
l2=args.l2

entrada=codecs.open(fentrada,"r",encoding="utf-8")
sortida=codecs.open(fsortida,"w",encoding="utf-8")



cadena='<?xml version="1.0" encoding="UTF-8" ?>'
sortida.write(cadena+"\n")
cadena='<tmx version="1.4">'
sortida.write(cadena+"\n")
cadena='<header/>'
sortida.write(cadena+"\n")
cadena='  <body>'
sortida.write(cadena+"\n")

for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split("\t")
    try:
        segment1=camps[0]
        segment2=camps[1]
        if len(escape(remove_control_characters(segment1))) and len(escape(remove_control_characters(segment1))):
            cadena='   <tu>'
            sortida.write(cadena+"\n")
            cadena='      <tuv xml:lang="'+l1+'"><seg>'+escape(remove_control_characters(segment1))+'</seg></tuv>'
            sortida.write(cadena+"\n")
            cadena='      <tuv xml:lang="'+l2+'"><seg>'+escape(remove_control_characters(segment2))+'</seg></tuv>'
            sortida.write(cadena+"\n")
            cadena='    </tu>'
            sortida.write(cadena+"\n")
    except:
        pass
    
cadena='  </body>'
sortida.write(cadena+"\n")
cadena='</tmx>'
sortida.write(cadena+"\n")
