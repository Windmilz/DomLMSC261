#           Pyo!

## What did you do?
-  I downloaded a module for Python
### How did you do it?
- I went through and firstly downloaded pip, which is an installer for python, then I had to install homebrew and then finally I got to install the module "pyo"
### the problems you faced
- I ran into a problem after downloading the homebrew and trying to install pyo where it would say "sndfile.h does not exist". I just googled it because code never breaks once and I found a GitHub thread where this exact issue has been solved. Turns out there were some other directories that weren't installed in the original brew of my homebrew, so I just needed to install those seperately and then I was good to go :)

**The individual directories**
brew install libsndfile

brew install portaudio

brew install portmidi

brew install liblo


## Code you took from elsewhere
- The github I got help from: https://github.com/belangeo/pyo/issues/77

gittir - ziggear
