from typing import Counter
import things
import utilities
from datetime import datetime
from PyInquirer import prompt


if __name__ == "__main__":
    timeFrame = utilities.askForTimeFrame()
    print(timeFrame)
