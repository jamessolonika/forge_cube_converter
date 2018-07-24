# settings.py:
#     -check if there is a saved file
#     -if yes, load saved json settings (can be previous run or user default)
#     -if no, load default settings and ask for forge folder
    
#     -Defaults needed:
#         -classes for all draft and sealed options
#         -oldest and newest dates
#         -number of players
#         -paths to cube, draft, sealed and editions folder within forge
#         -list of set types that count as premium

#     -Functions needed:
#         -when booster string is changed, count number of cards requested * number of players
#         -use forge path and default cube, draft, sealed and editions to create file paths

import json
import os

#Constant values. These will probably never change unless forge has major changes
default_oldest_day = 99
default_oldest_month = 99
default_oldest_year = 9999

default_newest_day = 00
default_newest_month = 00
default_newest_year = 0000

number_of_players = 8






#Sum all of the numbers in a booster to get the size of the booster
def sum_digits(booster)
    return sum(int(x) for x in booster if x.isdigit())


class Draft_settings():
    """A storage for the settings for draft"""

    def __init__(self,Name,DeckFile,Singleton,Booster,NumPacks,LandSetCode):
    """Initialize attributes"""
    self.Name = Name
    self.DeckFile = DeckFile
    self.Singleton = Singleton
    self.Booster = Booster
    self.NumPacks = NumPacks
    self.LandSetCode = LandSetCode
    self.card_count = 0

    def count_cards(self):
        """Count the number of cards requested in this draft"""
        card_count = number_of_players * sum_digits(self.Booster)


class Sealed_settings():
    """A storage for the settings for sealed"""

    def __init__(self,Name,DeckFile,IgnoreRarity,Booster,NumPacks,LandSetCode):
    """Initialize attributes"""
    self.Name = Name
    self.DeckFile = DeckFile
    self.IgnoreRarity = IgnoreRarity
    self.Booster = Booster
    self.NumPacks = NumPacks
    self.LandSetCode = LandSetCode
    self.card_count = 0

    def count_cards(self):
        """Count the number of cards requested in this draft"""
        card_count = number_of_players * sum_digits(self.Booster)