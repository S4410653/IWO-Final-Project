#Filename: clean_data.py
#Description: This program preprocesses the text given and checks whether the user is or is not from the Randstad,
#using the given word lists with json extension. The input comes from the Linux shell.
#Author: Sijbren van vaals

import sys
import re 
import json
from text_preprocessing import * 

def preprocessed_text(text):
	"""This function preprocesses a given text file, it converts to lowercase, removes url's, \
		normalizes the text and removes punctuations"""
	clean_text = []
	for line in text:
		
		line = to_lower(line)
		line = re.sub(r"http\S+", "", line) # Searches for URLs add replaces it with nothing
		line = normalize_unicode(line) # Converts the characters to normal unicode (e.g. é to e), this also removes tags, hastags and smileys
		line = remove_punctuation(line)
		clean_text.append(''.join(line))
	clean_text[-1] = clean_text[-1] + "\n" # Last item does not have a '\n' so here we add one,
										   # because we are concatenating text files 
	return clean_text

def check_in_wordlist(text, wordfile_RS, wordfile_not_RS):
	"""This functions checks whether the sender of the tweet lives in one of the relevant places"""
	tweets_RS = []
	tweets_not_RS = []
	user_location = re.compile(r"   +(.*)$") # The line so the Tweet can be splitted from the user location on a tab. It was automatically converted to four spaces, sometimes three spaces between the text and the user location. That is why I chose for three or more spaces
	for place_names in wordfile_RS.values(): # check if sender of the Tweet lives in the Randstad
		for place_name in place_names:
			for sentence in text:
				location = user_location.search(sentence) # search for the tab to split on
				if location: # check if there was a tab to split on
					location = location.group(1)
				else:
					location = "" # If there was no tab to split on (i.e. no user location) give empty string as user location
				index = location.find(place_name)		
				if index != -1:
					tweets_RS.append(sentence)

	for place_names in wordfile_not_RS.values(): # check if sender of the Tweet does not live in the Randstad
		for place_name in place_names:
			for sentence in text:
				location = user_location.search(sentence) # search for the tab to split on
				if location: # check if there was a tab to split on
					location =location.group(1)
				else:
					location = "" # If there was no tab to split on (i.e. no user location) give empty string as user location
				index = location.find(place_name)
				if index != -1:
					tweets_not_RS.append(sentence)

	return tweets_RS, tweets_not_RS

def main(argv):

	if len(argv) == 4:
		with open(argv[1], 'r') as file:
			text = file.readlines()
			cleaned_text = preprocessed_text(text)
			
		with open(argv[2]) as word_file:
			wf_Randstad = json.load(word_file)
			
		with open(argv[3]) as word_file:
			wf_not_Randstad = json.load(word_file)
		
		relevant_text = check_in_wordlist(cleaned_text, wf_Randstad, wf_not_Randstad)

		f = open("all_tweets_RS.txt", "a") 
		for line in relevant_text[0]:
			f.write(line)
		f.close()
		f = open("all_tweets_not_RS.txt", "a")
		for line in relevant_text[1]:
			f.write(line)
		f.close()
	else:
		print("Usage: {}, please give five commands. Interpreter, Python file, text file, wordlist Randstad and wordlist not Randstad.".format(argv[0], file=sys.stderr))
		exit(-1)
	

if __name__ == "__main__":
	main(sys.argv)
