import sys
import re
import random


v0 = "mu"
v1 = "uim"
v2 = "muumuu"
v3 = "uiiumiuuimuiiumiuuimuiiu"

# the function check_rx return true is the rule may 
# be used for a transformation

def check_r1(s):
    if s[-1] == "i":
        return True
    else:
        return False

def apply_r1(s):
    # Rule 1: If you have a string with last letter i, you 
    # can add a u at the end
    if s[-1] == "i":
        return s + "i"
    else:
        print("You didn't check rule 1!")
        sys.exit()

def check_r2(s):
    try:
        a = s.index('m')        # this gets the first m in string
        if len(s) - 1 == a:     # if first 'm' found is at the end of string
            return False
        else:
            return True
    except ValueError:
        return False

def apply_r2(s):
    # Assumes the M is at the start of the string, not ideal
    sub = s[1:]
    ex = s + sub
    return ex

# Rule 1 and 2 can only be applied to one location in the string
# Rule 3 and 4 can be multi-positioned ... 

# the apply functions for 3 and 4 will just pick the index at random

def get_indices(s, sub):
    # input: string s, substring sub
    # output: list of ints, each int an index of sub in string s
    indices = [m.start() for m in re.finditer('(?=' + sub + ')', s)]
    if indices:
        return indices
    else:
        print("There was a call to get_indexes but returned ", indices)
        return indices
    

# Rule 3: iii becomes u
# from umiiimu -> umumu
# from miiii -> miu OR mui
# from miii -> mu

def check_r3(s):
    if 'iii' in s:
        return True
    else:
        return False

def apply_r3(s):
    sub = 'iii'
    indices = get_indices(s, sub)
    index = random.choice(indices)
    n = s[:index] + 'u' + s[index+3:]
    return n

def check_r4(s):
    if 'uu' in s and len(s) > 3:
        return True
    else:
        return False

def apply_r4(s):
    # Rule 4: uu can be dropped
    # from uuu -> u
    # from muuuiii -> muiii

    # fails on muu
    sub = 'uu'
    indices = get_indices(s, sub)
    index = random.choice(indices)
    n = s[:index] + s[index+2:]
    return n

def decide_next(s):
    # Input: string
    # Decide when of the four rules may be applied to the string
    # then select one and apply it
    res = check_r1(s), check_r2(s), check_r3(s), check_r4(s)
    applys = [apply_r1, apply_r2, apply_r3, apply_r4]
    opts = list(zip(applys, res))
    valids = [x for x in opts if x[1]]      # Checks that returned True
    decided = random.choice(valids)
    print("Using: ", decided)
    return decided[0](s)
    
def run():
    start = "mi"
    s = decide_next(start)
    print("first: ", s)
    print()
    while True:
        s = decide_next(s)
        print()
        print(s)
        
run()       
