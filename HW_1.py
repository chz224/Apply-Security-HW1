#Cheng Hao Zheng
#HW 1 Spell Checker
#Github user name: chz224

#import spellchecker library
from spellchecker import SpellChecker

def main():
    spell = SpellChecker()
    #change the file to the text file you want to spell check
    #currently spell checking file MisspelledText.txt
    misspelledFile = open('MisspelledText.txt', 'r')

    #output file that contains the correction for the file spell checked
    #currently output to file CorrectedText.txt
    correctedFile = open('CorrectedText.txt', 'w')
    for line in misspelledFile:
        for word in line.split():
            correctedFile.write(spell.correction(word))
            correctedFile.write(' ')
        correctedFile.write('\n')

if __name__=="__main__":
    main()

