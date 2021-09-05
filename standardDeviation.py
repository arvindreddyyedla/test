#Following method returns the standard deviation of the list
from mean import calculateMean
def calculateStandardDeviation(numList):

    individualDeviations = [(element - calculateMean(numList)) ** 2 for element in numList]

    #according to formula we now calculate the standard deviation
    sumOfDeviations  = 0
    for oneItem in individualDeviations:
        sumOfDeviations += oneItem
   
    standardDeviation = (sumOfDeviations / len(numList))**0.5
    # returning the standard deviation calculated
    return standardDeviation