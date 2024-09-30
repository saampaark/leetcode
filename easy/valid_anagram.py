def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
        
    s_letters = {}
        
    for char in s:
        if char in s_letters:
            s_letters[char] += 1
        else:
            s_letters[char] = 1
        
    for char in t:
        if char in s_letters:
            s_letters[char] -= 1
            if s_letters[char] < 0:
                return False
        else:
            return False

    return all(count == 0 for count in s_letters.values())
