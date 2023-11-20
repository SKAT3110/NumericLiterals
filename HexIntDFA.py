class HexIntDFA:
    states = {"q1", "q2", "q3", "q4", "q5", "q6", "q7"} # Set of States of decimal integer DFA
    acceptstates = {"q5"} # Set of accept States of decimal integer DFA
    start_state = "q1" # initial state
    alphabet = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F", "x", "X"} # alphabet for decimal integer
    hexDigits = alphabet - {"x", "X", "_"}
    transition = {}

    def __init__(self):
        self.transition = { # transition function for all states
            "q1": lambda c: "q2" if c == "0" else "q7", 
            "q2": lambda c: "q3" if c == "x" or c =="X" else "q7",
            "q3": lambda c: "q5" if c in self.hexDigits else ("q4" if c=="_" else "q7"),
            "q4": lambda c: "q5" if c in self.hexDigits else "q7",
            "q5": lambda c: "q5" if c in self.hexDigits else ("q6" if c=="_" else "q7"),
            "q6": lambda c: "q5" if c in self.hexDigits else "q7",
            "q7": lambda c: "q7"
        }
    
    def accepts(self, str):
        state = self.start_state # set start state
        for char in str: # Step through characters in input
            state = self.transition[state](char) # apply lambda based on state
        if state in self.acceptstates: 
            return True # accept if final state is in accept states
        else:
            return False
