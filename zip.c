// Author: Evan Glazer
// Zip.c
// This program will compress string data to read out the string with a number and letter.
// EX: 3A1G5F.....ETC

#include <stdio.h>
#include <string.h>

int main() {
    
     // Starting Variables
     int zip, i, word;
     char input[30000];
     strcpy(input, word);
     char* read = input;
     char* compress = input;
     
     // Open and Read File
     FILE* ifp;
     ifp = fopen("zip.txt", "r");
     fscanf(ifp, "%s", input);
     
     // For loop to read lines of string to compress
     for (i=0; i<zip+1;i++){
         fscanf(ifp,"%s", input);
         }
     
     // Counting the string, along with compressing it to read output 3B...
     // Use point by reference to manipulate strings
	 
	 // Accumlators
     char c = input[0];
	 int count = 0;
	 // Looping statement with conditional statements
	 while ( *read != '\0' ) {
      fscanf(ifp,"%s", input);
	  if ( *read == c ) {
	   count++;
	  }
	  else {
	   *compress++ = c;
	   *compress++ = count + '0';
	   count = 1;
	  }
	  c = *read;
	  read++;
	 }
	 *compress++ = c;
	 *compress++ = count + '0';
	 *compress = '\0';
	 
     
     // Output the compressed string data
     printf(input, "\n");
     
     system("PAUSE");
	 return (0);
	}



	
