from collections import Counter 

def mininmumSubstring(s,t):
    counter1 = Counter(t)

    def Helper(counter):

        for keys,v in counter1.items():
            if keys not in counter or v > counter[keys]:
                return False 
        return True

    ans = float('inf')
    substring = ""
    size = len(s) 

    for i in range(size):

        for j in range(i+1):
            temp = Counter(s[j:i+1])

            if Helper(temp): 
                ans = min(ans,i-j)
                substring = s[j:i+1]
            
                
    return substring

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"

    print("Minimum substring : ",mininmumSubstring(s,t))