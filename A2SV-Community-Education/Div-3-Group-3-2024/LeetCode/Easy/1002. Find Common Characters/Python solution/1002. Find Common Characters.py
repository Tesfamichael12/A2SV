class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []

        # Initialize common_character_counts with the characters from the first word
        common_character_count = collections.Counter(words[0])

        # Store the characters of the current word in current_character_count
        for i in range(1, len(words)):
            current_character_count = collections.Counter(words[i])

            # Update common_character_count to keep the minimum count
            for ch in common_character_count.keys():
                common_character_count[ch] = min(common_character_count[ch], current_character_count[ch])

        # Append the common characters
        for ch, count in common_character_count.items():
            for _ in range(count):  # if count > 1, ch occured count times in all the words
                res.append(ch)
        
        return res
        # Or without the need for appending the common characters just return the following 
        # return common_character_counts.elements()

                      
            
