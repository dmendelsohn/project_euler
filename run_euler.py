import sys
import traceback
import operator
import importlib
import re
import pyximport; pyximport.install()
from datetime import datetime as dt 

ERROR = 'RUNTIME ERROR'
sys.dont_write_bytecode = True # Because pyc files are annoying

def run_problem(n, verbose=False):  # Returns (answer, description, runtime) as (int, str, timedelta) tuple
    sys.stdout.write('Problem %d ' % (n,))
    sys.stdout.flush()
    t = dt.now()
    try:
    	m = importlib.import_module('solutions.problem_%03d' % (n,))
    	result = m.compute(verbose)
    except:  # Since problems are independent, generic except clause is okay.
    	if verbose:
    		print(traceback.format_exc())
    	result = (-1, ERROR)
    return result + (dt.now()-t,)

def get_answers():
    answers = {}
    lines = open('answers.txt').read().split('\n')
    for line in lines:
    	match = re.match('Problem (\d{3}): (-?\d*\.?\d*)', line)
    	if match:
    		answers[int(match.group(1))] = match.group(2)  # Notice numberic answer is kept as string
    return answers

def format_result(prob_num, result, exp_answer): # n is int, result is (numeric num, str text, timdelta runtime) tuple, exp_answer is str!
    if result[1] == ERROR:
    	correct = ERROR
    elif exp_answer == None:
    	correct = "UNCHECKED"
    elif exp_answer != str(result[0]):  # Recall expected answer is in string form
    	correct = "WRONG"
    else:
    	correct = "CORRECT"
    s = '%s in %s' % (correct, result[2])
    if correct != ERROR:
    	s += ': %s (%s)' % (result[0], result[1])
    if correct == "WRONG":
    	s += '; Expected answer = %s' % (exp_answer,)
    return s

if __name__ == '__main__':
    if len(sys.argv) > 1:
    	verbose = False
    	for arg in sys.argv: # verbose is true if any arg contains 'verbose'`
    		verbose = (verbose or ('verbose' in arg))
    	sys.argv = list(filter(lambda arg: 'verbose' not in arg, sys.argv))  # Remove any 'verbose' args
    	answers = get_answers()
    	t_start = dt.now()
    	computed_answers = {}
    	for arg in sys.argv[1:]:
    		if '-' in arg:
    			(a, b) = map(int, arg.split('-'))
    			for n in range(a, b+1):
    				result = run_problem(n, verbose=verbose)
    				print(format_result(n, result, answers.get(n, None)))
    				computed_answers[n] = result[0]
    		else:
    			n = (int(arg))
    			result = run_problem(int(arg), verbose=verbose)
    			print(format_result(n, result, answers.get(n, None)))
    			computed_answers[n] = result[0]
    	if len(computed_answers) > 1:
    		correct, wrong, unknown, error = set(), set(), set(), set()
    		for n in computed_answers:
    			if computed_answers[n] == -1:
    				error.add(n)
    			elif n not in answers:
    				unknown.add(n)
    			elif str(computed_answers[n]) != answers[n]:  # Recall answers contains answer as str
    				wrong.add(n)
    			else:
    				correct.add(n)
    		if correct:
    			print("Correct: %s" % (str(sorted(list(correct))),))
    		if wrong:
    			print("Wrong: %s" % (str(sorted(list(wrong))),))
    		if unknown:
    			print("Unknown: %s" % (str(sorted(list(unknown))),))
    		if error:
    			print("Error: %s" % (str(sorted(list(error))),))
    		print("For %d problems, total runtime %s" % (len(computed_answers), str(dt.now()-t_start)))
    else:
    	print("Please include a problem number") 
