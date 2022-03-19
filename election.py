# Import copy module for use in functions where elements are removed in order to keep the original whole.
import copy
import openpyxl

wBook = openpyxl.load_workbook("voting.xlsx")
values = wBook.active


def generatePreferences(values):
    """
    Produces two lists from an inputted worksheet, one from the column indices and the other from the values of each cell in a row.
    These are used to sort the valuations (cell values) before being used as the values in a dictionary.

    Parameters:
        values: a worksheet object.
    Returns:
        dictionary - named preferenceDict, with voters as keys and candidates as values.
    """
    preferenceDict={}

    for row in values.rows:
        # List of column indices (candidates).
        candidateNum = [(col[0].column) for col in values.columns]

        # List of values for each voter (valuations).
        voterValuation = [(cell.value) for cell in row]

        # Join above lists to make list of tuples.
        joinList = list(zip(candidateNum, voterValuation))

        # Sort by second element of tuple in decending order.
        joinList.sort(key=lambda x: (x[1],x[0]), reverse=True)

        # Make list from first element (candidates).
        candidatesList = [(i[0]) for i in joinList]

        # Dictionary with voter as key and valuation as value.
        voterDict = {row[0].row: candidatesList}
        preferenceDict.update(voterDict)
    return(preferenceDict)


def dictator(preferenceProfile, voter):
    """
    An voter is inputted as an integer and is checked to ensure it exists in the dictionary.
    If so that voter's first choice is returned as the winner.

    Parameters:
        preferenceProfile: a dictionary with voters as keys and candidates as values.
        voter: an integer corresponding to an voter.
    Returns:
        integer - the winning candidate.
        or 
        string - error message for when the integer inputted does not correspond to an voter.
    """
    # Check the inputted voter corresponds to an voter.
    if voter in preferenceProfile:
        # First choice of designated voter.
        return preferenceProfile[voter][0]
    else:
        return str("Sorry, this voter does not exist")

def scoring(preferences, scoreVector, tieBreak):
    """
    A dictionary is created and each candidate (key) has a score (value) assigned.
    The score is taken from the scoreVector inputted and correlates to each voter's preference.
    The scores are updated each round and the winner is the candidate with the highest total.
    Prints a statement if the inputted scoreVector list is not equal in length to the number of candidates.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        scoreVector: an int used to determine the length of the scoring list.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function).
            or
        boolean - False.
    """

    # Check if scoreVector equals the number of candidates.
    if len(scoreVector) == len(preferences[1]):
        
        # Sort scoreVector in decending order.
        scoreVector.sort(reverse = True)

        # Dictionary of candidates and their assigned scores.
        totalScore = scoreRound(preferences, scoreVector)

    # If the length of scoreVector does not equal the number of candidates.
    else:
        print("incorrect Input")
        return False

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(totalScore)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def mostOftenFirst(preferences, tieBreak):
    """
    The first choice of each voter is collected from the preference profile and each occurance is tallied.
    candidate(s) with the highest tally counts are potential winners.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function).
    """
    # List the first choice of each voter.
    firstChoice = voterFirstChoice(preferences)

    # Dictionary of each candidate and their frequency.
    tally = tallyResult(firstChoice)

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(tally)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def removeLeast(preferences,tieBreak):
    """
    Creates a copy of the dictionary to be used so that removing elements does not effect the original.
    Removes the least preferred candidate of each voter, these are assigned 0 points so don't need to be counted.
    Counts the frequency of each of the remaining candidates as they are assigned 1 point each.
    candidate(s) with the highest tally counts are potential winners.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function).
    """
    # Copy of preferences dictionary in order to remove elements without editing the original
    preferencesCopy = copy.deepcopy(preferences)

    # Remove least preferred candidate of each voter.
    for row in preferencesCopy.values():
        row.pop()

    # New list of lists minus least preferred, 1 point assigned to each
    onePoint = [preferencesCopy[i] for i in preferencesCopy]

    # Flatten list to be able to tally
    flatOnePoint = [i for subList in onePoint for i in subList]

    # List the candidates with the highest frequency.
    tally = tallyResult(flatOnePoint)

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(tally)

    # Run tieBreaking if needed and return winner
    return selectWinner(possibleWinList, preferences, tieBreak)


def ranked(preferences, tieBreak):
    """
    A dictionary is created and each candidate (key) has a score (value) assigned.
    The score starts at 0 for the voter's least preferred and increases by one in order of preference.
    The scores are updated each round and the winner is the candidate with the highest total.
    candidate(s) with highest tally counts are potential winners.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function).
    """
    numcandidates = len(preferences[1])

    # List with highest value equal to one less than the number of candidates down to 1.
    rankedScore = [i for i in range(numcandidates-1, -1, -1)]

    # Dictionary of candidates and their assigned scores.
    totalScore = scoreRound(preferences, rankedScore)

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(totalScore)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def harmonic(preferences, tieBreak):
    """
    A dictionary is created and each candidate (key) has a score (value) assigned.
    The score starts at 1 for the voter's preferred candidate and decreases by (1 divided by position) in order of preference.
    candidate(s) with highest tally counts are potential winners.
    TieBreaking function is run if needed and winner is returned.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function)
    """
    numcandidates = len(preferences[1])

    # List of the position of each candidate taken from index.
    position = [i for i in range(1, numcandidates+1)]

    # List with highest value equal to one and reducing for each candidate equal to 1/position.
    harmonicScore = []
    for i in position:
        posDivision = 1/i
        harmonicScore.append(posDivision)

    # Dictionary of candidates and their assigned scores.
    totalScore = scoreRound(preferences, harmonicScore)
    print (totalScore)

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(totalScore)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def singleTransferable(preferences, tieBreak):
    """
    First preferences of voters are tallied.
    candidates not in that list are assigned 0 so they can be removed.
    All losing candidates for that round are added to a list and then removed.
    candidate(s) with highest tally counts are potential winners.
    TieBreaking function is run if needed and winner is returned.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        int - the winning candidate (via selectWinner function)
    """
    # Copy of preferences dictionary in order to remove elements without editing the original.
    preferencesCopy = copy.deepcopy(preferences)


    while (len(preferencesCopy[1]) > 1):

        # All possible preferences.
        preferenceList = preferencesCopy[1]

        firstChoice = voterFirstChoice(preferencesCopy)
        tally = tallyResult(firstChoice)

        # Any candidates not one of the first choices have frequency of 0.
        for i in preferenceList:
            if i not in firstChoice:
                tally[i] = 0

        # List of least chosen candidates.
        loseList = [key for key, value in tally.items() if value == min(tally.values())]

        # Remove losing candidates.
        for row in preferencesCopy:
            for candidate in loseList:
                preferencesCopy[row].remove(candidate)

    # List the candidates with the highest frequency.
    possibleWinList = highestCountWins(tally)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def rangeVoting(values, tieBreak):
    """
    Each candidate's valuations are added together.
    The winner is the candidate with the maximum sum of all valuations.
    Result is accessed by index and then converted to the voter's number by adding 1.

    Parameters:
        values: a worksheet object.
        tiebreak: tie-breaking rule to apply if needed.
    Returns:
        integer - the winning candidate (via selectWinner function)
    """
    totalSums = []

    # Access valuations.
    for col in values.columns:
        colValue = [(cell.value) for cell in col]

    # Sum of valuations and update total list.
        sumCol = (sum(colValue))
        totalSums.append(sumCol)
    maxVal = [(max(totalSums))]

    # Find index of highest value(s).
    winningIndex = [i for i in range(len(totalSums)) if totalSums[i] in maxVal]

    # +1 to change from index to position (voter).
    possibleWinList = [i + 1 for i in winningIndex]

    # Access preference dicttionary to pass into tieBreaking function as argument.
    preferences = generatePreferences(values)

    # Run tieBreaking if needed and return winner.
    return selectWinner(possibleWinList, preferences, tieBreak)


def tieBreaking(possibleWinList, preferences, tieRule):
    """
    Inputs the potential winners as a list from the voting function used.
    Then sorts the potential winners before selecting a winner depending on the tie-breaking rule selected.

    Parameters:
        possibleWinList: list of potential winners.
        preferences: a dictionary with voters as keys and candidates as values.
        tieRule: tie-breaking rule selected.
    Returns:
        integer - the winning candidate depending on the tie-breaking rule chosen.
            or
        string - error message for when the integer inputted does not correspond to an voter.
            or
        string - error message for when the input does not relate to a tie-breaking option.
    """
    # Sort the potential winners ascendingly.
    possibleWinList.sort()

    # Select a tie-breaking rule to apply depending on input.
    # Selects the winner with the highest number. The last element of the sorted list.
    if tieRule == "max":
        return possibleWinList.pop()

    # Selects the winner with the lowest number. The first element of the sorted list.
    if tieRule == "min":
        return possibleWinList.pop(0)

    # Selects the winner from the corresponding voter's preferred choice.
    if type(tieRule) == int:

        # Check integer corresponds to an voter.
        if tieRule in preferences:
            voterPref = preferences[tieRule]

            # Compare potential winners with chosen voter's preferences.
            voterChoice = [i for i in voterPref if i in possibleWinList]

            # Select highest ranked.
            return voterChoice[0]
        else:
            return str("Sorry, this voter does not exist")

    # If input is not "max,"min" or an integer.
    else:
        return str("Sorry, that isn't a tie-breaking option")


def scoreRound(preferences, score):
    """
    Assigns a set of scores to each candidate in order of preference.
    Does this for each voter's preference and puts reults in a dictionary.

    Parameters:
        preferences: a dictionary with voters as keys and candidates as values.
        score: list of numerical values to be assigned to candidates.
    Returns:
        dictionary - keys are candidates, values are their scores.
    """
    totalScore = {}

    roundOne = True
    for row in preferences:
        # Create a dictionary with that voter's candidates and their assigned scores.
        initialScore = dict(zip(preferences[row], score))

        for key in initialScore:
            # For the first round populate the totalScore dictionary with the first set of scores.
            if roundOne == True:
                totalScore.update(initialScore)

            # For subsequent rounds add the scores to those that already exist.
            elif key in totalScore:
                totalScore[key] = totalScore[key] + initialScore[key]
        roundOne = False
    return totalScore


def tallyResult(result):
    """
    Takes list of candidates and counts them together into a dictionary with their frequency.

    Parameters:
        result: list of candidates.
    Returns:
        dictionary - keys are candidates, values are their frequency.
    """
    tally = {i: result.count(i) for i in result}
    return tally


def voterFirstChoice(preferences):
    """
    Creates a list of all of the first choice candidates of all of the voters.

    Parameters:
        preferenceDict: a global dictionary with voters as keys and candidates as values.
    Returns:
        list - preferred candidate for each voter.
    """
    firstChoice = [(preferences[i][0]) for i in preferences]
    return firstChoice


def highestCountWins(tally):
    """
    Takes a dictionary of candidates and their frequencies and identifies the most common candidate(s).

    Parameters:
        tally: keys are candidates, values are their frequency
    Returns:
        list - all possible winners.
    """
    # Create a list of candidates that appear most frequently.
    possibleWinList = [key for key, value in tally.items() if value == max(tally.values())]
    return possibleWinList


def selectWinner(possibleWinList, preferences, tieBreak):
    """
    Checks if the list of potential winners contains more than one candidate and so there is a tie.
    If only one candidate then that candidate is returned as an integer.
    If more than one candidate is a possible winner then the tieBraking function is called.

    Parameters:
        possibleWinList: all possible winners.
        preferenceDict: a global dictionary with voters as keys and candidates as values.
        tiebreak: tie-breaking rule to apply if needed.

    Returns:
        integer - the winning candidate either via the selectWinner function or directly if only one possibility.
    """
    # Checks if the number of possible winners is more than 1.
    if len(possibleWinList) >1:
        return tieBreaking(possibleWinList, preferences, tieBreak)
    else:
    # Make single element list into an integer.
        winner = possibleWinList[0]
        return winner