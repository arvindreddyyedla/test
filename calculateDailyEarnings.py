from standardDeviation import calculateStandardDeviation
from mean import calculateMean 
from generateListFromFile import createListFromFile
if __name__ == "__main__":
    # taking input of file name from the user 
    # example input openPrice.txt
    openFile = input("\nPlease enter the text file for open prices : ")
    closeFile = input("\nPlease enter the text file for close prices : ")

    #generate list from the open and close files
    openPriceList = createListFromFile(openFile)
    closePriceList = createListFromFile(closeFile)

    dailyEarnings = []

    #calculate dailyEarnings for each price

    for i in range(len(openPriceList)):

        dailyEarnings.append(round(closePriceList[i] - openPriceList[i], 6))

    
    print("\nFollowing is the Daily Earnings list: \n\n",dailyEarnings, "\n")

    stdDev = calculateStandardDeviation(dailyEarnings)
    mean = calculateMean(dailyEarnings)

    print("\nMean of Daily Earnings  =  ",mean,"\n")

    print("\nStandard Deviation of Daily Earnings = ",stdDev, "\n")

    # defining daily earnings deviation dict
    dailyearningsDict = {
        "one standard deviation" : [],
        "two standard deviation" : [],
        "three standard deviation": []
    }

    for earning in dailyEarnings:

        if earning > (mean - stdDev) and earning < (mean + stdDev):

            dailyearningsDict["one standard deviation"].append(earning)

        if earning > (mean - 2*stdDev) and earning < (mean + 2*stdDev):

            dailyearningsDict["two standard deviation"].append(earning)

        if earning > (mean - 3*stdDev) and earning < (mean + 3*stdDev):

            dailyearningsDict["three standard deviation"].append(earning)



    print("\nDictionary of the daily earnings is following : \n\n",dailyearningsDict, "\n")