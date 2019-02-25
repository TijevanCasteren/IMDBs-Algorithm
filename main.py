import time
import datetime

#grabs the files that are needed
from divscore import diversityScore
from combiner import combineIt
from textedit import textProcessing
from ml import ml

while True:
    #main loop, runs untill the user quits ('quit' or 'q')
    t1=t2=t3=t4=t5=0   #keeps track of time spent doing certain operations
    userinput = ""
    print("Possible actions : \n\n")
    print("\t-Calculate lexical diversity ('div')")
    print("\t-Complete package ('complete')")
    print("\t-Combine the scripts ('combi')")
    print("\t-Text Processing ('txtp')")
    print("\t-Run Machine learning alglorythm ('ml')")
    userinput = input("Please select an action : ").lower()
    #the following passage is meant to recieve an input from the user and run a specific set of functions
    if userinput == "q" or userinput == "quit":
        #breaks out of the main loop, allowing the user to cancel
        break
    elif userinput == "complete":
        t1=time.time()
        diversityScore()
        t2=time.time()
        combineIt()
        t3=time.time()
        textProcessing()
        t4=time.time()
        ml()
        t5=time.time()
        print ("div time : ",str(datetime.timedelta(seconds=t1-t2)))
        print ("combiner time : ",str(datetime.timedelta(seconds=t2-t3)))
        print ("txtp time : ",str(datetime.timedelta(seconds=t3-t4)))
        print ("ml time : ",str(datetime.timedelta(seconds=t4-t5)))
        print ("Total time : \n\n",str(datetime.timedelta(seconds=t5-t1)))
        #time taken  = finishing time - initial time
    elif userinput == "div":
        t1=time.time()
        diversityScore()
        t2=time.time()
        print ("div time :",str(datetime.timedelta(seconds=t1-t2)))
    elif userinput == "combi":
        t1=time.time()
        combineIt()
        t2=time.time()
        print ("combi time :",str(datetime.timedelta(seconds=t1-t2)))
    elif userinput == "txtp":
        t1=time.time()
        textProcessing()
        t2=time.time()
        print ("txtp time :",str(datetime.timedelta(seconds=t1-t2)))
    elif userinput == "ml":
        t1=time.time()
        ml()
        t2=time.time()
        print ("ml time :",str(datetime.timedelta(seconds=t1-t2)))
    else:
        print("Unknown syntax\n\n\n\n")
