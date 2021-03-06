#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

#Create word lists 
"""
computer_adjectives = [
    "minimal",
    "neural",
    "synaptic",
    "solid state",
    "asymptotic",
    "concurrent",
    "multithreaded",
    "augmented",
    "presingularity",
    "responsive",
    "Cartesian",
    "extreme",
    "critical",
    "Matrioshka",
    "meatspace",
    "trinary",
    "recursive",
    "Pythonic",
    "functional",
    "imperitive",
    "backend",
    "trontend",
    "social",
    "bio",
    "strategic",
    "sustainable",
    "value added",
    "holistic",
    "nano",
    "granular",
    "cloud",
    "content",
    "core",
    "brick-and-mortar",
    "digital",
    "cyber",
    "mono",
    "uni",
    "duplo",
    "curve",
    "cloud",
    "geodesic",
    "colocal",
    "electronic",
    "transcendant",
    "programatic",
    "media agnostic",
    "immersive",
    "technocratic",
    "AI",
    "VC",
    "procedural",
    "effective",
    "full spectrum",
    "analytic",
    "peer-to-peer",
    "b2b",
    "semiotic",
    "best practice",
    "new",
    "viral",
    "zero-sum",
    "maker",
    "convergence",
    ]

"""
techterm = [
    "Java",
    "python",
    "CSS",
    "APIs",
    "C++",
    "IDEs",
    "Ruby",
    "Javascript",	
    "SQL",
    "the Command line",
    ]

manterm = [
    "boys",
    "men",
    "bros",
    "men folk",
    "dudes",
    "guys",
    "manalytics",
    ]

code_language = [

    "python",
    "CSS",
    "APIs",
    "C++",
    "IDEs",
    "Ruby",
    "Javascript",
    "Django"

        ]

guystereo = [
    "gaming",
    "sports",
    "statistics",
    "man math",
    "fishing",
    "engineering",
    "mobius strips",
    "craft beer",
    "boys' business",
    "carpentry",
    "building things",
    "practical",
    "useful",
    ]

hashtag = [
    "#brocode",
    "#brogrammers",
    "#gotthis",
    "#yolo",
    "#realtalk",
    ]

domestic = [
    "shopping",
    "putting on makeup",
    "baking a pie",
    "getting dressed",
    "pillow fighting",
    "having a monthly",
    "powdering your nose",
    "wearing high heels",
    "standing in line for the bathroom",
    "horoscopes",
    "having girls night",
    "doing your hair",
    ]

manadj = [
    "tough",
    "burly",
    "stronger",
    "serious",
    "not girly",
    "macho",
    "muscular",
    "adult",
    "brave",
    "rugged",
    "male",
    "studly",
    "redblooded",
    "heavy-duty",
    "brawny",
    "mighty",
    "athletic",
    "with balls",
    "with a wrench",
    "like a beast",
    ]

lady = [
    "sweet",
    "young",
    "pretty",
    "sensitive",
    "prone to hysterics",
    "emotional",
    ]

male = [
    "boyfriend",
    "husband",
    "guy friend",
    "boss",
    ]

hashtags = [
    '#hashtag1',
    '#hashtag2',
    '#hashtag3',
    ]


#define function for each template

def gotthis_gen():
    return("Don't worry about %s, the %s will handle that." %(random.choice(techterm),random.choice(manterm)))

def weknowbetter_gen():
    return("It's ok if you can't do %s; it's a %s thing you wouldn't understand." %(random.choice(code_language),random.choice(guystereo)))

def cool_gen():
    return("Just imagine you're %s, only %s." %(random.choice(domestic), random.choice(manadj)))

def cute_gen():
    return("You're so cute when you try %s." %(random.choice(techterm)))

def confuze():
    return("Oh, it's simple. You just %s the %s." %(random.choice(techterm), random.choice(techterm)))

def chuckle():
    return("Oh, you don't get the difference between %s and %s? heh heh hehheh%shehehe" %(random.choice(techterm), random.choice(techterm), random.choice(techterm)))

def girly():
    return("That's impressive %s for someone so %s. Did your %s help you?" %(random.choice(techterm), random.choice(lady), random.choice(male)))

def oneup():
    return("Oh, you use %s? I guess that works if you don't know %s."%(random.choice(techterm), random.choice(techterm)))

# This function randonly picks one of the above templates
# and and rcalls it to create a sentence

def generate_sentence():
    tfile = open("brotweets.txt", "w")
    for xlx in range(0,100):
        rolldice = random.randint(0,7)
        if rolldice == 0:
            template = gotthis_gen()
        if rolldice == 1:
            template = weknowbetter_gen()
        if rolldice == 2:
            template = cool_gen()
        if rolldice == 3:
            template = cute_gen()
        if rolldice == 4:
            template = confuze()
        if rolldice == 5:
            template = chuckle()
        if rolldice == 6:
            template = girly()
        if rolldice == 7:
            template = oneup()

        while 1:
            if len(template) <= 140:
                for dothree in range(0,3):
                    hashtag = random.choice(hashtags)
                    if len(template) + len(hashtag) <= 140:
                        template = template + " " + hashtag
                    else:
                        pass
                tfile.write(template)
                tfile.write("\n")
                break
            else:
                pass
    tfile.close()

generate_sentence()

        


# Create variable for the site name and a random buzzword hashtag
#site = "CodeSplain.com"
#hashtag1 = " #" + random.choice(manterm) + random.choice(guystereo)


#sen1 = generate_sentence() + " " + site + hashtag1
#print(sen1)
#print(len(sen1))

# Wites 100 tweets to tweets.py
# If there's room, also adds two more hashtags to the tweet
# The /n creates a new line.
