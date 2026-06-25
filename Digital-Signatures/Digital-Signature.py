
import hashlib

# List of inputs
inputs = ["hello", "ChatGPT", "123456", "OpenAI", "md5 test"]

for text in inputs:
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    print(f"Input: {text}\nMD5:   {md5_hash}\n")












"""

// Digital Signature: Creation at sender and signature verification at receiver

#include <stdio.h>
#include <math.h> // Required for pow()

int main() {
    char M1 = 'A';
    char M2 = 'B'; //Message=AB
    double p=3, q=11, e=7, d=3;      //RSA p, q prime numbers
    char h = M1 ^ M2;
    double h1=(double)h;
    int s =(int)pow(h1, e) % (int)(p*q);

    printf("\n message is: AB, signature is: %d", s);
    printf("\n message signed successfully");

   char g = M1 ^ M2;
   int h2=(int)g;
   int h3= (int)pow(s, d) % (int)(p*q);
   printf("\n h2=%d, h3=%d",h2, h3);

   if(h2==h3)
          printf("\n Signature verified successfully");
   return 0;
}

Output: 
 message is: AB, signature is: 9
 message signed successfully
 h2=3, h3=3
 Signature verified successfully
 
 """
