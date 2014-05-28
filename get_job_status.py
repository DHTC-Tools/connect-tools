#!/usr/bin/env python

# Copyright 2014 University of Chicago

import pwd
import os
import sys

import htcondor

VERSION = '0.01'
JOB_STATUS = {0: 'Unexpanded',
              1: 'Idle',
              2: 'Running',
              3: 'Removed',
              4: 'Completed',
              5: 'Held',
              6: 'Submission Error'}

schedd = htcondor.Schedd()
user = pwd.getpwuid(os.getuid())[0]
jobs = schedd.query("Owner == \"{0}\"".format(user), ['ProcId', 'ClusterId', 'JobStatus'])
user_job_status = {}
for job in jobs:
    status = JOB_STATUS[job['JobStatus']]
    if status in user_job_status:
        user_job_status[status] += 1
    else:
        user_job_status[status] = 1



sys.stdout.write("{0:<30} {1:<30}\n".format('Status', '# of Jobs'))
for status in user_job_status:
    sys.stdout.write("{0:<30} {1:<30}\n".format(status, user_job_status[status]))
sys.stdout.write("{0:<30} {1:<30}\n".format('Total', len(jobs)))
