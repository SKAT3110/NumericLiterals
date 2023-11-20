class Hexint:
    states = {"q1", "q2", "q3", "q4", "q5", "q6"} # q6 is the trap state
    acceptState = "q5"
    startState = "q1"
    hexDigits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
    hexMark = {"x", "X"}
    hexBreak = "_"

    def transition(self, char, state):
         if state == "q1":
            if char == "0":
               return "q2"
            else:
               return "q6" # continue to state q2 or else trap state
         
         if state == "q2":
            if char == self.hexMark:
               return "q3"
            else:
               return "q6" # continue to state q3 or else trap state
            
         if state == "q3":
            if char == self.hexBreak:
               return "q4"
            elif char == self.hexDigits:
               return "q5" # continue to state q4 if there is hexBreak or accept state q5 if hexDigit
            else:
               return "q6" # if neither hexBreak or hexDigit enter trap state
            
         if state == "q4":
            if char in self.hexDigits:
               return "q5" 
            else:
               return "q6" # continue to accept state q5 or else trap state
            
         if state == "q5":
            if char == self.hexDigits:
               return "q5"
            elif char == self.hexBreak:
               return "q4" # continue to next state or else trap state
            else:
               return "q6" # stay in accept if hexDigit, move back to q4 if hexBreak, or trap state if neither
            
    def accepts(self, str): 
      state = self.startState # set starting state to q1
      for char in str: 
         state = self.transition(char, state) # loop through until end of string
      if state == self.acceptState: # check if final state is the accept state
         return True
      else:
         return False