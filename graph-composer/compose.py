"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
from ssl import HAS_NEVER_CHECK_COMMON_NAME
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # remove text in brackets
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # replace all whitespace with a single space
        text = text.lower() # make lower case
        
        # just remove all the punctuation
        text = text.translate(str.maketrans('','', string.punctuation))
    
    return text.split()

def make_graph(words):
    g = Graph()
    prev_word = None
    for word in words:
        # get the vertex to add edges to, creates one if it doesn't exist
        word_vertex = g.get_vertex(word)
        if prev_word:
            prev_word.increment_edge(word_vertex)
        prev_word = word_vertex
    g.generate_probability_mappings()
    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    while len(composition) < length:
        composition.append(word.value)
        word = g.get_next_word(word.value)
    return composition


def main(artist):
    # step 1 : get words from text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for songFile in os.listdir(f'songs/{artist}'):
        if songFile == '.DS_Store': continue

        songWords = get_words_from_text(f'songs/{artist}/{songFile}')
    
    words.extend(songWords)

    # step 2 : make a  graph using these words
    g = make_graph(songWords)

    # step 3 : get the next word from the graph a number of times chosen by the user
    composition = compose(g, songWords, 20)

    # step 4 : show the user!
    return ' '.join(composition)


if __name__ == '__main__':
    artist = 'green_day'
    print(main(artist))