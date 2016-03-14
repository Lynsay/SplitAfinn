#!/usr/bin/env python

'''
	File: split_afinn_list.py
	Version: 1.0
	Date: March 2016
	Author: Lynsay A. Shepherd
	
	Description: This script reads in a file of affective words produced by AFINN.  Splits the list in to postitive and negative words.
	
	Notes:
			- Website for the AFINN affective wordlist is here- http://neuro.imm.dtu.dk/wiki/AFINN
			- Useful library for pasrsing the affective wordlist- https://github.com/fnielsen/afinn
	
	
'''

#imports required
import io
import sys


#Parse the initial AFINN wordlist, create a new pos and neg file
def read_file():
	try:
		print "In read_file method"
		file = open('AFINN-111.txt', 'r')

		for line in file:
			
			#split the word from the score
			assert len(line.split('\t')) == 2
			phrase, score = line.split('\t')

			#the score needs to be an int
			#but don't write the int to a file....that breaks things
			scoreval = int(score)
			
			if scoreval<0:
				write_to_neg(phrase, score)
				
			else:
				write_to_pos(phrase, score)		
			
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"


#write to positive file
def write_to_pos(phrase, score ):
	try:
		print "In write_to_pos method"
		print phrase
		print score
		print "--------------"
		
		f = open('afinn_pos.txt','a')
		f.write(phrase+","+score)
		f.close()
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
		

#write to negative file
def write_to_neg(phrase, score):
	try:
		print "In write_to_neg method"
		print phrase
		print score
		print "--------------"
		
		f = open('afinn_neg.txt','a')
		f.write(phrase+","+score)
		f.close()
	
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
		
#main method   	
def main():
	try:
		print "***running the main method***"
		read_file()
		
	except Exception,e:
		print "+++ Something has gone wrong. "+str(e)+" +++"
    


if __name__ == "__main__":
    main()
    	
