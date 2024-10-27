#full_ops
#
# Usage: python3 full_ops.py c_in n_wv.

# Arguments:
#c_in: input channel count
#n_wv: number of weight vectors

# Output:
#print(int(c_out)) # output channel count
#print(int(h_out)) # output height count
#print(int(w_out)) # output width count
#print(int(adds))  # number of additions performed
#print(int(muls))  # number of multiplications performed
#print(int(divs))  # number of divisions performed

# Written by Samuel Jacobson
# Other contributors: None

# import Python modules
import math  # math module
import sys  # argv

# Constants
w = 7.292115 * 10 ** -5


# initialize script arguments
c_in = float('nan')
n_wv = float('nan')

# Parse Script Arguments
if len(sys.argv) == 3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
else:
    print( \
        'python3 conv_ops.py c_in n_wv' \
        )
    exit()

# Script

c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv * c_in
mults = n_wv * c_in
divs = 0

print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))  # number of additions performed
print(int(mults))  # number of multiplications performed
print(int(divs))  # number of divisions performed
