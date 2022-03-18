import sys
import theater

def main():
    if (len(sys.argv) != 2):
        print("You must pass an input file as the argument", file = sys.stderr)
        return
    try:
        movieTheater = theater.Theater() #executing class Theater from theater.py
        with open(sys.argv[1], 'r') as inputFile: #open input file in read mode
            outputFile = open("output.txt", 'w') #open output file in write mode
            allLines = inputFile.read().splitlines() #split lines from input file
            sortedLines = []
            for line in allLines: 
                input = line.split(" ") #separate by space
                reservationNo = input[0] #put reservation number from input file into array
                numRequested = int(input[1]) 
                sortedLines .append((reservationNo, numRequested))
            sortedLines.sort(key = lambda x: x[1], reverse=True)
            for line in sortedLines:
                outputList = movieTheater.book(line) #running def book from theater.py
                if (len(outputList) > 0):
                    outputString = ",".join(outputList) #separate bookeed seats by comma
                    outputFile.write("%s %s\n" % (line[0], outputString))
            print("output.txt")
    except FileNotFoundError:
        print("Input file %s does not exist" % sys.argv[1])



if __name__ == "__main__":
    main()