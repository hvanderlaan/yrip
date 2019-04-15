#!/usr/bin/env python3

""" youtube helper package for yrip """

# =========================================================================== #
# File     : libyrip/youtube.py                                               #
# Purpose  : helper package for yrip                                          #
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

from collections import OrderedDict

from requests import get
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL


def find_song(title):
    """ function for finding song on youtube """
    results = OrderedDict()
    youtubeclass = 'spf-prefetch'
    youtubeurl = 'https://www.youtube.com'
    youtubesearchurl = '/results'

    html = get(youtubeurl + youtubesearchurl, params={'search_query': title})
    soup = BeautifulSoup(html.text, 'html.parser')

    for result in soup.findAll('a', {'rel': youtubeclass}):
        songurl = youtubeurl + (result.get('href'))
        songtitle = (result.get('title'))
        results.update({songtitle: songurl})

    return results


def display(songs):
    """ function for displaying results """
    counter = 1
    for song in songs:
        print(f'[{counter}]: {song}')
        counter += 1


def download(url):
    """ function to download and convert song """
    opts = {
        'format': 'besraudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(opts) as ydl:
        ydl.download([url])
