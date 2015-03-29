#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

techterm = [
    "python",
    "CSS",
    "APIs",
    "C++",
    "IDEs",
    "Ruby",
    "Javascript",	
    ]

manterm = [
    
    "boys",
    "men",
    "bros",
    "men folk",
    "dudes",
    "guys",
    ]

code_language = [

    "python",
    "CSS",
    "APIs",
    "C++",
    "IDEs",
    "Ruby",
    "Javascript",

        ]

guystereo = [
    "gaming",
    "sports",
    "statistics",
    "man math",
    "fishing",
    "engineering",
    ]

def gotthis_gen():
    return("Don't worry about %s, the %ss will handle that." %(random.choice(techterm),random.choice(manterm))

print(gotthis_gen())


def weknowbetter_gen():
    return("It's ok if you can't %s; I taught myself for %s you wouldn't understand." %(random.choice(code_language),random.choice(guystereo))
"""

tfile = open("tweets.txt", "w")
for numtweets in range(0,100):
    tfile.write(story_gen())
    tfile.write("\n")

tfile.close()
