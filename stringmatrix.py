import numpy as np
import re
a_str = '''
−0.322 0.052 0.028 −1.12 0.002
0 0 1 −0.001 0
−10.6 0 −2.87 0.46 −0.65
6.87 0 −0.04 −0.32 −0.02
0 0 0 0 −7.5
'''
print(repr(a_str))

a_str = re.sub(' ', ', ', a_str)
a_str = re.sub('−', '-', a_str)
a_str = re.sub('\n(.+?)(?=\n)', '[\g<1>],\n', a_str)

print(a_str)
