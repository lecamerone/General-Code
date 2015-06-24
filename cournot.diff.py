# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:40:40 2015

@author: Alexander
"""

"Define fixed point algorithm"

def fixedp1(cn1, cn2, q1, maxiter = 10):
    itr = 0
    qp1 = []
    qp2 = []
    while itr < maxiter:
        q_1 = cn1(q1)
        qp1.append(q_1)        
        q_2 = cn2(q_1)
        qp2.append(q_2)        
        q1 = q_2
        itr = itr + 1
    return qp1, qp2, q_1, q_2

cn1 = lambda q: 55 - 0.5*q
cn2 = lambda q: 60 - 0.5*q

