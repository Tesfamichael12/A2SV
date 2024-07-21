class Solution {
public:
    string freqAlphabets(string s) {
        string s_mapped = "";
        int i = 0;

        while (i < s.length())
        {
            if (i + 2 < s.size() && s[i + 2] == '#')
            {
                int num = stoi(s.substr(i, 2)); // use the stoi method with strings only for a single char just subtract '0' with a singl quotation
                s_mapped += (char) (num + 97 - 1);
                i += 3;
            }
            else
            {
                int num = (s[i]) - '0'; // if it is a singe char the use this techniqe to change a char to int
                s_mapped += (char) (num + 97 - 1);
                i += 1;
            }
        }
        return s_mapped;
    }
};