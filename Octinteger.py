class Octinteger:
    states = {"q1", "q2", "q3", "q4", "q5", "q6"} # list of states used
    acceptState = "q5"
    startState = "q1"
    octDigits = {"0", "1", "2", "3", "4", "5", "6", "7"}
    octMark = {"o", "O"}
    octBreak = "_"

    def transition(self, char, state):
        if state == "q1":
            if char == "0":
                return "q2"
            else:
                return "q6"
        if state == "q2":
            if char in self.octMark:
                return "q3"
            else:
                return "q6"
        if state == "q3":
            if char == self.octBreak:
                return "q4"
            elif char in self.octDigits:
                return "q5"
            else:
                return "q6"
        if state == "q4":
            if char in self.octDigits:
                return "q5"
            else:
                return "q6"
        if state == "q5":
            if char in self.octDigits:
                return "q5"
            elif char == self.octBreak:
                return "q4"
            else: return "q6"

    def accepts(self, str):
        state = self.startState
        for char in str:
            state = self.transition(char, state)
        if state == self.acceptState:
            return True
        else:
            return False