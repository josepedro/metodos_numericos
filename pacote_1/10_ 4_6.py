#!/usr/bin/env python
# -*- coding: utf-8 -*-
# questao 10 - 4.6

import numpy as np
from sympy import *

x = Symbol('x')
w = Symbol('w')
a = Symbol('a')
b = Symbol('b')
t = Symbol('t')

print 'Aplicando o procedimento do algorítmo 4.3 da página 224: '
argument = (np.pi/2)*(w**2)
expression_c_t = cos(argument)
print 'Integral para c(t): '
print latex(Integral(expression_c_t))
expression_s_t = sin(argument)
print 'Integral para s(t): '
print latex(Integral(expression_s_t))
integral_s_t = integrate(expression_s_t,(w,a,t))
integral_c_t = integrate(expression_c_t,(w,a,t)) 
tempos = np.linspace(0.1, 1.0, num=(1.0)/0.1)
for tempo in tempos:
	c_t = integral_c_t.evalf(subs={a:0, t:tempo})
	s_t = integral_s_t.evalf(subs={a:0, t:tempo})
	print 'para t = %f; c(t) = %f; s(t) =  %f' % (tempo, c_t, s_t) 

