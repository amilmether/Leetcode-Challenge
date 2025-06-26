# 804. Unique Morse Code Words [Easy]
# Tags: misc

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        d=[".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--","-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_set=set()
        for word in words:
            morse_word=""
            for char in word:
                index=ord(char)-ord('a')
                morse_word+=d[index]
            morse_set.add(morse_word)
        return len(morse_set)
        
