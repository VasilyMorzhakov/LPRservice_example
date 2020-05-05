# LPRservice_example
An example of using our LPR server

To run, you have python3 installed (or python2, just choose another import in the script)

Then, export environmental variables: LPR_GATE,LPR_SERVER,LPR_PORT, we provide.

Linux:
```
export LPR_GATE="*****"
export LPR_SERVER="*****"
export LPR_PORT="*****"
```

or in Windows:
```
set LPR_GATE=****
set LPR_SERVER=****
set LPR_PORT=****
```

then just run ```python3 example.py```

Feel free to change the image to send in ```f = open("example.jpg","rb") ```
