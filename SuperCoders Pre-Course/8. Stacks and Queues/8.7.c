#include<string.h>
char* reverseString(char *s)
{
   int len = strlen(s);  
   int i;  
   for(i=0;i<len;i++)  
        push(s[i]);  
   for(i=0;i<len;i++)  
        s[i]=pop(); 
   return(s);
}