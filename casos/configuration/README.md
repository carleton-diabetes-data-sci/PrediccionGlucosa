# configuration

The main file is config.py:

* config -> define configuration
    * paths -> for the project, the dataset, the input files, processed files and output graphs and scores
    * variables -> parser variables with --cn (case number). 
        * en -> execution number -> number of executions 
        * tn -> tries number -> number of experiments
        * ph -> prediction horizon -> 12 is 1 h and 6 is half an hour
        * pn -> patient number -> amount of patients
        * pi -> patient id -> id of the patient. 0 means 1,2,4,6,7,8
        * st -> split type -> way of separate train-val-test. 0 means 60-20-20.
        * a -> acceleration -> if there is acceleration data. 0 means no and 1 yes.
        * fw -> filter night windows -> if the acceleration (and glucose) night windows are erased. 0 means no and 1 yes.

        
   
## Cases definition in variables.py
    
* (--cn==0) -> case_zero:
    * en=10
    * tn=7
    * ph=12
    * pn=1
    * pi=1
    * st=0
    * a=1
    * fw=1

* (--cn==1) -> case_one:
    * en = 10
    * tn = 7
    * ph = 12
    * pn = 6
    * pi = 0
    * st = 0
    * a = 1
    * fw = 1

* (--cn==2) -> case_two:
    * en=4
    * tn=7
    * ph=12
    * pn=6
    * pi=0
    * st=0
    * a=0
    * fw=0

* (--cn==3) -> case_three:
    * en = 0
    * tn = 0
    * ph = 0
    * pn = 0
    * pi = 0
    * st = 0
    * a = 0
    * fw = 0

* (--cn==4) -> case_four:
    * en = 0
    * tn = 0
    * ph = 0
    * pn = 0
    * pi = 0
    * st = 0
    * a = 0
    * fw = 0
