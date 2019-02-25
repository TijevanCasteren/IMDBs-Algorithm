#   output =(tconst|primaryTitle|averageRating|numVotes|diversityScore)

def combineIt():

    lineArray = []
    lineCurrent = 0

    with open("data/diversityscore.txt", "rt") as openDiv:
        divContent = openDiv.read()
    lineArray = divContent.splitlines()
    output = [["" for x in range(0,5)] for y in range(len(lineArray))]
    for line in lineArray:
        x = line.split(' ', 1)[-1]
        x = (x.split('.txt', 1))[0]
        x = (x.split('Script_', 1))[-1]
        x = x.replace("_",":") #corrects the undersocre symbol back to : in the movie titles 
        y = line.split(' ', 1)[0]
        output[lineCurrent][1] = x
        output[lineCurrent][4] = y    
        lineCurrent = lineCurrent+1
    
    def imdb_ids():
        import imdb
        ia = imdb.IMDb()
        for outputPos in range (0,len(output)):
            title=output[outputPos][1]
            movies = ia.search_movie(title)
            if movies:
                movie = ia.get_movie(movies[0].movieID)
                output[outputPos][0] ='tt'+str(movies[0].movieID)

    def run_ratings():        
        with open("data/ratings.tsv","rb") as openRatings:
            for row in openRatings:      
                rowTemp = row.decode("utf-8")
                rowCurrent = rowTemp.split("\t")
                for outputPos in range(0,len(output)):
                    if output[outputPos][0] == rowCurrent[0]:
                        output[outputPos][2] = rowCurrent[1]
                        output[outputPos][3] = rowCurrent[2].splitlines()[0]
                        break
                    
    f = open("data/output.txt", "w")
    f.close()
    imdb_ids()
    run_ratings()
    with open("data/output.txt","w") as openOutput:
        for x in range(len(output)):
            lineOutput =""
            for y in range(0,5):
                if y == 4:
                    lineOutput = lineOutput + output[x][y]
                else:
                    lineOutput = lineOutput + output[x][y] + "|"
            openOutput.write(lineOutput+"\n")       
