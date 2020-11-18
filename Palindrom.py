def isPalindrome(i):
   if len(i) <= 1:
       return True
   else:
       if i[0] != i[len(i)-1]:
           return False
       else:
           return isPalindrome(i[1:len(i)-1])
print(isPalindrome("kajak"))