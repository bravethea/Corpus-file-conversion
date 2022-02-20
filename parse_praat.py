#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
File type = "ooTextFile"
Object class = "TextGrid"

xmin = 0
xmax = 100
tiers? <exists>
size = 3
item []:
    item [1]:
        class = "IntervalTier"
        name = "Mary"
        xmin = 0
        xmax = 100
        intervals: size = 9
        intervals [1]:
            xmin = 0
            xmax = 0.1390510564699631
            text = ""
        intervals [2]:
            xmin = 0.1390510564699631
            xmax = 1.388316601821478
            text = "kako umemo"
        intervals [3]:
            xmin = 1.388316601821478
            xmax = 1.5931324612478241
            text = ""
        intervals [4]:
            xmin = 1.5931324612478241
            xmax = 2.5458491670429924
            text = "a sWg ne mOemo"
    item [2]:
        class = "IntervalTier"
        name = "John"
        xmin = 0
        xmax = 100
        intervals: size = 5
        intervals [1]:
            xmin = 0
            xmax = 3.4043675794551733
            text = ""
        intervals [2]:
            xmin = 3.4043675794551733
            xmax = 4.171074504151386
            text = "pa jEste"
        intervals [3]:
            xmin = 4.171074504151386
            xmax = 4.51364310768235
            text = ""

    item [3]:
        class = "TextTier"
        name = "bell"
        xmin = 0
        xmax = 100
        points: size = 2
        points [1]:
            number = 5.731567954179178
            mark = ""
        points [2]:
            number = 7.836776329751645
            mark = ""

"""

import codecs
import re

praat_file_path = "/Users/teodoravukovic/Google Drive (not syncing)/PycharmProjects/VIAN-file-conversion/PRAAT/samples/Mary_John_bell.TextGrid"

class Convert:
    def __init__(self, input_path):
        if input_path.endswith(".TextGrid"):
            self.input_praat = input_path
        else:
            print("incorrect input format")
            pass

    def parse_praat(self):
        praat_dict = {}
        with codecs.open(self.input_praat, 'r') as input_praat:
            print(input_praat)

            for line in input_praat:
                print(line.encode('utf8'))


if __name__ == "__main__":
    input_source = Convert(praat_file_path)
    input_source.parse_praat()
