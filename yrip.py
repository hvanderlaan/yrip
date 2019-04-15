#!/usr/bin/env python3

""" main python script for downloading youtube music videos """

# =========================================================================== #
# File     : yrip.py                                                          #
# Purpose  : Download music vidoes from youtube and convert them to mp3       #
#                                                                             #
# Author   : Harald van der Laan                                              #
# Date     : 2019-04-15                                                       #
# Version  : v1.0.0                                                           #
# =========================================================================== #
# Changelog:                                                                  #
#  - v1.0.0: Initial version                                                  #
# =========================================================================== #
# Copyright (c) 2019, Harald van der Laan                                     #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining       #
# a copy of this software and associated documentation files (the "Software") #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included     #
# in all copies or substantial portions of the Software.                      #
#                                                                             #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,             #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES             #
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.   #
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, #
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,               #
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE  #
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                               #
# =========================================================================== #

import sys
from argparse import ArgumentParser
from libyrip import youtube


def _get_args():
    parser = ArgumentParser()
    parser.add_argument('-t', '--title', type=str, help='title of song',
                        required=True)
    parser.add_argument('-a', '--auto', type=int, help='auto download nummer')

    return parser.parse_args()


def main():
    """ main function """
    args = _get_args()
    results = youtube.find_song(args.title)

    if args.auto:
        if args.auto >= 1:
            downloadurl = list(results.values())[args.auto - 1]
            youtube.download(downloadurl)
            sys.exit(0)
        else:
            sys.stderr.write('[-]: -a value should be between 1 and 20.\n')
            sys.exit(1)

    youtube.display(results)
    print('')
    downloadnum = input('please select a number to download: ')
    print('')

    if int(downloadnum) >= 1:
        downloadurl = list(results.values())[int(downloadnum) - 1]
        youtube.download(downloadurl)
    else:
        sys.stderr.write('[-]: -a value should be between 1 and 20.\n')
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
