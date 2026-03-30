class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        mp1_even = dict()
        mp1_odd = dict()

        mp2_even = dict()
        mp2_odd = dict()
        for i in range(len(s1)):
            if i % 2 == 0:
                if s1[i] not in mp1_even:
                    mp1_even[s1[i]] = 1
                else:
                    mp1_even[s1[i]] += 1

                if s2[i] not in mp2_even:
                    mp2_even[s2[i]] = 1
                else:
                    mp2_even[s2[i]] += 1
                
            else:

                if s1[i] not in mp1_odd:
                    mp1_odd[s1[i]] = 1
                else:
                    mp1_odd[s1[i]] += 1


                if s2[i] not in mp2_odd:
                    mp2_odd[s2[i]] = 1
                else:
                    mp2_odd[s2[i]] += 1
                
        
        return mp1_even == mp2_even and mp1_odd == mp2_odd
