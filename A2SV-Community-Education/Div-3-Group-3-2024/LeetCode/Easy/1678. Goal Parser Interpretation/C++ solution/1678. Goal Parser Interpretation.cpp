class Solution {
public:
    string interpret(string command) {
        string out = "";
        int i = 0;
        while(i < command.length())
        {
            if (command[i] == 'G')
                out += "G";
            else if (command[i] == '(' and command[i + 1] == ')')
                out += "o";
            else if (command[i] == '(' and command[i + 1] == 'a')
                out += "al";
            i++;
        }
        return out;
    }
};