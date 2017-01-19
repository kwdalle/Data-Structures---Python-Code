Text Mining V 1.0.0 4/22/15

GENERAL USAGE NOTES
----------------------------------------------------------------------------------------------
- All characters, including numbers less than three characters long have been
  removed from the file that is given.
- Any word that has an apostrophe or hyphen in the word or directly preceeding
  or directly after the word will still have a apostrophe or hyphen in the 
  index, and your lookup should reflect this. I.E. if the word in the original 
  book is aft--man then must enter aft--man as your search word. This was done 
  to prevent words from being smashed together during the pre-processing portion 
  of the program.
- Numbers greater than or equal to three characters were left in the book after
  processing to allow for the lookup of years if they pertain to your query. 
  This done in the assumption of people following the general rule that if the 
  number is under three characters long that it would be written out instead of
  in number format.
- The stopwords list that is used in this program is a free list that was posted
  on google code, the text file describing this file is included in the file 
  package of this software.
- All lookups will be converted to lower case, so the software is not case sen-
  sitive, however it will not remove numerals or suggest spelling fixes if a 
  word is misspelled or misstyped.
- If you wish to dump the index to a text file for reference later than you need
  to just press enter with nothing on the command line to bring up the option
  to dump the index to a text file. This text file will be named index.txt, if
  you are using this program to analyze multiple files you will need to either
  manually rename this file or take other precautions to make sure that it will
  not be overwritten.
- To run this program enter: ipython project4.py example.txt
- example.txt is a placeholder for your text file to be analyzed. It will take
  a few seconds for the preprocessing to be finished, so do not worry if it do-
  es not ask for a query immediately.
- Note that the only way for the program to exit on its own is dump the index.
  Otherwise you can use the keyboard interrupt command at any point to end the
  program.
- Included with this software package will be a text file of the book Moby Dick,
  this may be used as a test for the software if the user so wishes. Otherwise
  make sure that the text file you are analyzing is within the same directory 
  as the software, unless you know how to use linux to access other directories.
  Also included is the index and pre-processed file for this as examples for the
  user.
- Pre-processed files just add the string "preprocessed" to the original file
  name.

