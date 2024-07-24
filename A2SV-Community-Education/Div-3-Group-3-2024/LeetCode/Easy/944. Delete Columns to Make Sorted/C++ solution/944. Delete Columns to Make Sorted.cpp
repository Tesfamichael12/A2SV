class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int c = strs[0].size();
        int delete_count = 0;
        string all_strs = "";
        for (int i = 0; i < n; i++)
            all_strs += strs[i];
        
        for (int i = 0; i < c; i++)
        {
            int a = i, b = i + c;
            for (int j = 0; j < n - 1; j++)
            {
                if (all_strs[a] > all_strs[b])
                {
                    delete_count++;
                    break;
                }
                a += c;
                b += c;
            }
        }
        return delete_count;
    }
};