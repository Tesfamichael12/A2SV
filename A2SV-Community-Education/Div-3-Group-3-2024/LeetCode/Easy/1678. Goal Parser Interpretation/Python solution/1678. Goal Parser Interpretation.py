class Solution:
    def interpret(self, command: str) -> str:
        out = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                out += "G"
            elif command[i] == '(' and command[i + 1] == ')':
                out += "o"
            elif command[i] == '(' and command[i + 1] == 'a':
                out += "al"
            i += 1
        return out

        # Or simply use the replace method 
        # return command.replace("()", "o").replace("(al)", "al")
        