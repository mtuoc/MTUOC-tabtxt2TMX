This program shows the help with the option -h:

```
python3 MTUOC-tabtxt2TMX.py -h
usage: MTUOC-tabtxt2TMX.py [-h] -i FENTRADA -o FSORTIDA -s L1 -t L2

MTUOC-tabtxt2TMX: A script to convert a parallel corpus in tabbed text into a TMX file.

options:
  -h, --help            show this help message and exit
  -i FENTRADA, --input FENTRADA
                        The input file to convert.
  -o FSORTIDA, --output FSORTIDA
                        Fix some issues in PDF conversion.
  -s L1, --L1code L1    The language code for the source language.
  -t L2, --L2code L2    The language code for the target language.
```

To convert the file corpus-eng-spa.txt in tab txt format into the TBX file corpus-eng-spa-eng.tmx, using the codes en-US for the source language and en-ES for the target language, you can write:


`python3 MTUOC-tabtxt2TMX.py -i corpus-eng-spa.txt -o corpus-eng-spa.tmx -s en-US -t es-ES`

You alternativelly can use the GUI version of the program, MTUOC-tabtxt2TMX, offering a simple GUI interface:

![](https://github.com/mtuoc/tutorials/blob/main/images/MTUOC-tabtxt2TMX-GUI.JPG)
