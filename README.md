# Unique to this forked repository
## To run the code
- Ensure your working directory is `casos`.
- Run the command `python3 main.py --cn 0`.

## Results
- The output from running the code is located in [output.log](output.log).
- The results of each experiment (RMSE values in mmol/L) are located in [D1NAMO/scores_subset/Caso_0/Caso_0_pacientes_relevantes_scores.csv](D1NAMO/scores_subset/Caso_0/Caso_0_pacientes_relevantes_scores.csv).
- Only certain branches contain updated versions of these files, as detailed below.

## Branch structure
- **corrected-methodology**: this branch contains our corrected methodology's results (in output.log and Caso_0_pacientes_relevantes_scores.csv)
- **naive-model-performance**: this branch contains our naive approach's results (only printed out in output.log)
- **reproduce-original-results**: this branch contains our replicated results (in output.log and Caso_0_pacientes_relevantes_scores.csv)

# Glucose prediction

The dataset and processed files are in D1NAMO.

The code and graphs are in casos.

The models in tf format are in models.
There are several cases.
Caso_0: There are independent patients. Any of them has 7 experiments (trynumber). There are 6 patients * 7 experiments = 42 models.
        They are generated several times, 1 for each execution. In total 420 models. 
        Maybe it is posible to train them just once, and then save and load, and use them several times for 10 executions.
        
        


