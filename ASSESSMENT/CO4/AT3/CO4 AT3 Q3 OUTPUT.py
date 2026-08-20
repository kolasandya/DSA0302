Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
========= RESTART: C:/Users/K sandhya/OneDrive/Documents/CO4 AT3 Q3.py =========
Sentence: She saw the man with a telescope

Number of possible CFG parses: 2

Parse 1
      S                                    
  ____|___________                          
 |                VP                       
 |     ___________|________                 
 |    |       |            PP              
 |    |       |        ____|___             
 NP   |       NP      |        NP          
 |    |    ___|___    |     ___|______      
PRON  V  DET      N   P   DET         N    
 |    |   |       |   |    |          |     
She  saw the     man with  a      telescope


Parse 2
      S                                
  ____|_______                          
 |            VP                       
 |     _______|___                      
 |    |           NP                   
 |    |    _______|____                 
 |    |   |   |        PP              
 |    |   |   |    ____|___             
 NP   |   |   |   |        NP          
 |    |   |   |   |     ___|______      
PRON  V  DET  N   P   DET         N    
 |    |   |   |   |    |          |     
She  saw the man with  a      telescope

