## Vigenere Cracking
### Byron Dowling
### 4143 Final Project

### Description:
Program that will autosolve a Vigenere cipher by utlizing the index of coincidence to determine the probable key length and then perform a dictionary attack on the key and score the results with the index of coincidence to determine the most likely result.

#### Succeesses:
- Program is very reliable at solving larger encrypted texts where there are more letters contributing to the overall I.O.C score
- Program performs this analysis very quickly and is accurate in detecting the key length on shorter texts

#### Shortcomings
- Smaller encrypted texts such as: TENSW PEZ YQB XYIMSG DMNV FHKZ JBQN VGZB GLMNM FWH can have incorrect results score higher than the actual English variant.
- That example should translate to: "HELLO CAN YOU PLEASE WEAR THIS BOMB VEST THANK YOU" and that text scores around a 0.041 I.O.C value.
- However, the following text: "LRSEL UAR LVN MDEEFL PBSR XUPL YGMF ILLQ LHEAR RLM" scores slightly higher at around 0.042 I.O.C value.
- This shortcoming can be improved with a sacrifice in time by doing a dictionary word for word lookup of the shifted text
