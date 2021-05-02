from typing import Counter
import things
import utilities
from datetime import datetime
from PyInquirer import prompt


if __name__ == "__main__":
    answers = utilities.askForTimeFrame()
    print(answers)
