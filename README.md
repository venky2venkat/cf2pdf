# cf2pdf
gets problems from codeforces in pdf format

### Instructions ###
  
  Download the python scipt 'topdfscript.py' and run it from python shell  
  It has 2 functions :
    gettags() and contestpdf()
    
    gettags() gets problems by tags 
    call it by topdfscript.gettags()
    further it will ask for path and tags
    
    
    contestpdf() gets problems by contestId
    call it by topdfcript.contestpdf()
    
    It has two parameters
    
    The first parameter is the path
    pass the path as a string or pass an empty 
    string for the present working directory to be path
    
    and the followed by contestId as a string
    
    eg: topdfscript.contestpdf("","1")
        or
        topdfscript.contestpdf("/users/","1")
        
  Both these commands will download the files   
  and store them as pdfs in a folder named by   
  the date and time of function call in the specified directory   
  
  
### Pre Requisites    
  pdfkit (https://pypi.python.org/pypi/pdfkit)  
  python 3.4  
  
  
    
    
    
