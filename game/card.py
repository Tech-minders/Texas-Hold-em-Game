class Card():

    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITES = ["HEART", "DIAMOND", "SPADE", "CLUBS"]

    def __init__(self, suite, rank):

        # Checks if the provided suite is actually text (a string)
        if not isinstance(suite, str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}") #__name__ solves the formatiing issue
        

        # Check if the provided rank is actually text (a string)
        if not isinstance(rank, str):
            raise TypeError(f"Suite expected to be a string got {type(rank).__name__}")

        # Convert inputs to uppercase to ensure they match the accepted lists
        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        # Validation: check if the rank is in the allowed list
        if rankUpper in Card.RANKS:
            pass # Does nothing if valid
        else:
            raise TypeError(f"Added rank not in rank list {Card.RANKS}")

        # Validation: check if the suite is in the allowed list
        if suiteUpper in Card.SUITES:
            pass # Does nothing if valid
        else:
            raise TypeError(f"Added suite not in suite list {Card.SUITES}")

        # If all checks pass, save the values to the specific card instance (self)
        self.rank = rankUpper
        self.suite = suiteUpper

    def printCard(self): # A method to display the card's information
        print("Rank", self.rank)
        print("Suite", self.suite)

if __name__ == "__main__": #Execution Control, Decides whether to run the test code or keep it hidden.
    
    # Try to create a card with an invalid suite ("Joker"), it will trigger a TypeError
    card1 = Card(suite="Joker", rank="A")
    card1.printCard()

    # Creates a valid card and prints its details
    card2 = Card(suite="Clubs", rank="3")
    card2.printCard()
