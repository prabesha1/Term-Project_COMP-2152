# ally.py

class Ally:
    def __init__(self, name, boost, threshold):
        """
        Initializes an ally with:
        - name: the name of the magical ally
        - boost: the amount of damage or support this ally gives
        - threshold: the monster's health threshold for this ally to become active
        """
        self.name = name
        self.boost = boost
        self.threshold = threshold

    def __str__(self):
        return f"{self.name} (Boost: {self.boost}, Threshold: {self.threshold})"
