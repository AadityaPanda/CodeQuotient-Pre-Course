def isVowel(ch):
  return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'
def countVowelSubstr(str):
  count = 0;
  n = len(str);
  i = 0;
  while i<n :
    if( isVowel(str[i])):
      count = (count + (n - i) % 10007) % 10007;
    i+=1;
  return count;