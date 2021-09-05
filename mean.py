def calculateMean(numList):
  #this method returns the mean of a numeric list
  sum  = 0
  # loop to add items in the list
  for x in numList:
      sum += x
  mean = sum / len(numList)
  return mean