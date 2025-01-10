class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        ans=''
        rem=0

        for i in range(len(a)-1,-1,-1):
            #print(f"Going to Index {i} {a} {b} {ans} {rem}")
            
            num = (int(a[i]) + int(b[i]) + rem) % 2
            #print(f"Num is {num}")
            rem = 0 if (int(a[i]) + int(b[i]) + rem) <= 1 else 1
            ans = str(num) + str(ans) 

        return str(rem) + ans  if rem else ans          
        
