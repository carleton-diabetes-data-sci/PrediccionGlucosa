#processed 

There are the processed files of the patients from diabetes_subset:

* datos_procesadosAccel.csv -> glucose and acceleration processed data

* insulina_procesada.csv -> processed insulin data

* comidas_procesada.csv -> processed food_dates_00x data

* datos_procesados.csv-> final file from the rest of files


There are several cases:

* Caso_0_ -> (Laura) Patient 1, acceleration, filter night windows, 10 executions, 1 h prediction

* Caso_1_ -> Relevant patients, acceleration, filter night windows, 1 h prediction

* Caso_2_ -> Relevant patients, no acceleration, no filter night windows, 1 h prediction


There are different patients:

* 001: ok

* 002: ok

* 003: few acceleration data

* 004: ok

* 005: without hours in food

* 006: ok

* 007: ok 

* 008: ok

* 009: few acceleration data


RUN

previos


Caso_0_mean/min/max_scores_relevant_patients_bugtf.csv -> 24/04 9h
1 -> 10 repeated times
2-> 10 different times
4,6,7,8 -> 1 time because it is repeated
mean_10_case_0_patient_1,0.6460036039352417,0.3206895887851715,0.295489102602005,0.2478715181350708,0.2413831502199173,0.3330800831317901,0.3379960656166076
mean_10_case_0_patient_2,0.6395263671875,0.5095070004463196,0.3727599382400512,0.4003938734531402,0.377368152141571,0.3809887766838074,0.4038296043872833
mean_1_case_0_patient_4,1.049528956413269,1.0183007717132568,0.9614747166633606,0.7967254519462585,0.5541543960571289,0.8515512347221375,0.3633622825145721
mean_1_case_0_patient_6,0.776907742023468,0.3541607856750488,0.4342478513717651,0.30638387799263,0.3967848122119903,0.3046422004699707,0.4797336161136627
mean_1_case_0_patient_7,1.389892578125,0.7343825697898865,0.6301084160804749,0.7123239636421204,0.8684800267219543,0.6256209015846252,0.6361172795295715
mean_1_case_0_patient_8,0.7662490606307983,0.5132066011428833,0.5580753087997437,0.5321452617645264,0.69416743516922,0.5363557934761047,0.8519701361656189
mean_mean_relevant_patients_case_0,0.8780180513858795,0.5750412195920944,0.5420258889595667,0.4993073244889577,0.5220563287536303,0.505373165011406,0.5121681640545527


Caso_0_mean/min/max_scores_relevant_patients_bugtf_2.csv 24/04 11 h
1,2 4,6,7,8 -> 1 time because it is repeated, from Laura dataprocesado.csv

 
