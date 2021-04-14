import argparse

def case_zero():
    en=10
    tn=7
    ph=12
    pn=1
    pi=1
    st=0
    a=1
    fw=1
    return en, tn, ph, pn, pi, st, a, fw

def case_one():
    en = 10
    tn = 7
    ph = 12
    pn = 6
    pi = 0
    st = 0
    a = 1
    fw = 1
    return en, tn, ph, pn, pi, st, a, fw

def case_two():
    en=4
    tn=7
    ph=12
    pn=6
    pi=0
    st=0
    a=0
    fw=0
    return en, tn, ph, pn, pi, st, a, fw


def case_three():
    en = 0
    tn = 0
    ph = 0
    pn = 0
    pi = 0
    st = 0
    a = 0
    fw = 0
    return en, tn, ph, pn, pi, st, a, fw


def case_four():
    en = 0
    tn = 0
    ph = 0
    pn = 0
    pi = 0
    st = 0
    a = 0
    fw = 0
    return en, tn, ph, pn, pi, st, a, fw


def switch_cases(cn):
    switcher = {
       0: case_zero,
       1: case_one,
       2: case_two,
       3: case_three,
       4: case_four
    }

    func = switcher.get(cn, lambda: "Invalid case")
    #print(func)
    en, tn, ph, pn, pi, st, a, fw = func()
    #print("cn:", cn, "en:", en, "tn:", tn, "ph:", ph, "pn:", pn, "pi:", pi, "st:", st, "a:", a, "fw:", fw)
    return cn, en, tn, ph, pn, pi, st, a, fw


def parser_variables():
    parser = argparse.ArgumentParser(description='Define the experiments')
    parser.add_argument('--cn', dest='cn', type=int, help='number of the case')
    #parser.add_argument('--en', help='number of executions for the group of experiments (int)')
    #parser.add_argument('--tn', help='number of tries or experiments for a case (int)')
    #parser.add_argument('--ph', help='prediction horizon (6: half an hour, 12: hour)')
    #parser.add_argument('--pn', help='amount of patients considered (int)')
    #parser.add_argument('--pi', help='id of the patient considered (0: patients 1,2,4,6,7,8,  1: patient 1)')
    #parser.add_argument('--st', help='type of the validation split (0: 60.20.20)')
    #parser.add_argument('--a', help='if the acceleration is considered (0: No, 1: Yes, 2: Yes night)')
    #parser.add_argument('--fw', help='if the night windows are filtered (0: No, 1: Yes, 2: No with estimated accel)')
    #parser.add_argument('--wn', help='number of windows')
    args = parser.parse_args()
    #print(args)
    cn = (args.cn)
    #print("cn is ", cn)
    cn, en, tn, ph, pn, pi, st, a, fw = switch_cases(cn)
    #print("cn:", cn, "en:", en, "tn:", tn, "ph:", ph, "pn:", pn, "pi:", pi, "st:", st, "a:", a, "fw:", fw)


    return cn, en, tn, ph, pn, pi, st, a, fw

#parser_variables()