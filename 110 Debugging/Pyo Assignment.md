#           Pyo!

## What did you do?
-  I used the pyo module to play a beautiful dulcimer sound
### How did you do it?
- I took the code Rachel gave me and ran it inside idle
### the problems you faced
- well first I took the code and debugged it in vscode, because it has a really nice debugging feature where it logs the errors as they appear. and in line 4 I got this error message

```
Exception has occurred: TypeError
cannot unpack non-iterable NoneType object
  File "/Users/dom/Desktop/DomLMSC261/DomLMSC261/dulcimer.py", line 5, in <module>
    snd = SndTable("/Users/dom/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
    ```
    Which at first confused the hell of me, but then I realized it was because the directory of the file it was trying to find didnt exist, because I am not 'rrome' and the user it was looking for was 'rrome' in the directory. As a side note I will be changing my directory name to 'rrome' to play chess in this absurd game of checkers (not really but that was such a small thing to see and without vscode I would of been absurdly lost).

## Code you took from elsewhere
- No code was taken from anywhere besides Rachel Rome.

- Rachel Rome's GitHub: https://github.com/rdwrome/lmsc261fa21
