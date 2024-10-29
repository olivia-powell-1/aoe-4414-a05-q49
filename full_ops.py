# fullOps,py
#
# Usage: python3 full_ops.py c_in n_wv
#  Text explaining script usage
# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors
#  ...
# Output:
#  print(int(c_out)) # output channel count
#  print(int(h_out)) # output height count
#  print(int(w_out)) # output width count
#  print(int(adds))  # number of additions performed
#  print(int(muls))  # number of multiplications performed
#  print(int(divs))  # number of divisions performed
#
# Written by Olivia Powell
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math as m

# "constants"
r_e_km = 6378.1363 # radius of the earth
e_e = 0.081819221456 # eccentricity of earth

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_in = float('nan')
n_wv = float('nan')

# parse script arguments
if len(sys.argv)==3:
   c_in = float(sys.argv[1])
   n_wv = float(sys.argv[2])
   ...
else:
   print(\
    'Usage: '\
    'python3 full_ops.py c_in n_wv'\
   )
   exit()

# write script below this line
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed