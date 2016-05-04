import sys
execfile('myparser.py')
sys.argv = ['DBN.py','train']
execfile('DBN.py')
sys.argv = ['DBN.py','sample']
execfile('DBN.py')