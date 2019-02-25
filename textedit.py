#output =(tconst|primaryTitle|averageRating|numVotes|diversityScore|TO|VBN|WP|UH|VBG|JJ|VBZ|VBP|NN|DT|PRP|WP$|NNPS|PRP$|WDT|RB|RBR|RBS|VBD|IN|FW|RP|JJR|JJS|PDT|MD|VB|WRB|NNP|EX|NNS|SYM|CC|CD|POS)
    
def textProcessing():
    """Main function tasked with processing the movie scripts

    Meant to asses and proess the text
    """

    import nltk
    nltk.download('stopwords')
    from nltk.tokenize import PunktSentenceTokenizer
    import os
    custom_sent_tokenizer = PunktSentenceTokenizer()
    nltk.download('averaged_perceptron_tagger')
    from nltk.data import load
    nltk.download('tagsets')
    import re
    
    def process_content(mytokenized):
                taggedlist = []
                try:
                    for i in mytokenized:
                        words = nltk.word_tokenize(i) # tokenize the sentences into words
                        tagged = nltk.pos_tag(words) # tag words as parts of speech
                        taggedlist.append(tagged)                  
                except Exception as e:       
                    taggedlist.append(str(e)) 
                return taggedlist
            
    def filename_strip(x): #function to strip movie script file name into the movie title
        x = (x.split('.txt', 1))[0]
        x = (x.split('Script_', 1))[-1]
        return(x)
    
    ratingfile=open("data/output_.txt", "rt") #open ratings file
    ratings=ratingfile.readlines()
    fileout = open("data/testoutput.txt", "w") # final dataset file with all the features and responses 
    
    for filename in os.listdir("data/scripts"): 
        if filename.endswith(".txt"): 
            file=open("data/scripts/"+filename, encoding="utf8")
            sampletext =file.read()         #this reads every file
            tokenized = custom_sent_tokenizer.tokenize(sampletext) #spit the text into sentences
            sent_num=len(tokenized) #number of sentences
            content = process_content(tokenized) #assigning the result to a variable
            totalwords=0
            tagdict = load('help/tagsets/upenn_tagset.pickle') 
            mydict=tagdict #make an dictionary from a standard list of tags
            
            for t in mydict.keys():
                mydict[t] = 0 #assigning the dict values to 0
                
            for lists in content: #loop over the content
                for tuples in lists:
                    word, tag = tuples
                    totalwords +=1  #counts the total number of words
                    if tag in mydict:
                        mydict[tag] += 1 #now we've got a dictionary with the counts of every tag
                        
            finaldict = dict() # final dict with frequences of each tag 
            for tag, count in mydict.items():
                percentage = int(count)/totalwords #dividing the percentages
                finaldict[tag] = str(percentage) #making it strings for output
    
            finaldict['AVS'] = str(totalwords/sent_num) #average sentence length
           
            symbols = ['#','$','(',')',',','.',':','``',"''","--","LS"] 
            for symbol in symbols:
                if symbol in finaldict:    #removing senseless tags
                   del finaldict[symbol]       
    
            outputline1=''
            outputline2=''
            my_reg=r'tt\d+\|'+re.escape(filename_strip(filename))+r'\|.*' #regex to match the movie line in the input file with ratings and lexical richness  
    
            for ln in ratings:
                if re.search(my_reg,ln): #matching the regex
                    outputline1=ln.splitlines()[0]+"|"
                    outputline2="|".join((finaldict.values())) # merging the dict values into the line
                    outputline1+=outputline2+"\n" #merging the line from the rating file and new feature values 
                    print(outputline1)
                    fileout.write(outputline1) #printing to file
    
            file.close()      
        
    ratingfile.close()
    fileout.close()
