import os

# TODO : set R environment

os.environ['R_HOME'] = r'/usr/local/Cellar/r/3.6.0_2'
os.environ['R_USER'] = r'\Users\onyx\Crasher\QMUL\DA\.venv\lib\python3.7\site-packages\rpy2'

import rpy2.robjects as robjects
# TODO : set twitter path environment
directory = r'\Users\onyx\Crasher\QMUL\DA\mine\DataAnalyticsProject\twitter_scrubbing\twitter.R'
r_source = robjects.r['source']
r_source(directory)
print('r script finished running')
