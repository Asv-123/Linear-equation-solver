import streamlit as st
import numpy as np
import scipy
from scipy.optimize import fsolve
from scipy.linalg import solve

st.title('Algebraic equation solver ')


def quadratic(x):
    return a * x ** 2 + b * x + c

option = st.selectbox('Choose the type of equation to solve:',('Quadratic','Cubic','Linear '))

if option == 'Quadratic':
    st.header('Solve Quadratic equation ')
    st.write('Equation Format: ax² + bx + c = 0')

    a = st.number_input('Enter the coefficient of a:',value=1)
    b = st.number_input('Enter the coefficient of b:', value=2)
    c = st.number_input('Enter the coefficient of c:', value=0.0)

    if st.button("Solve the Quadratic Equation "):
        if a == 0:
            st.write('This is not a Quadratic Equation ')
        else:
            roots = fsolve(quadratic,[0,0])
            st.write('The roots of the equation are x1: ',roots[0],'and x2: ',roots[1])


elif option == 'Cubic':
    st.header('Solve Cubic equation ')
    st.write('Equation Format: ax³ + bx² + cx + d = 0')
    a = st.number_input('Enter the coefficient of a:', value=1)
    b = st.number_input('Enter the coefficient of b:', value=2)
    c = st.number_input('Enter the coefficient of c:', value=0.0)
    d = st.number_input('Enter the coefficient of d:', value=0.0)

    if st.button('Solve the Cubic equation: '):
        if a == 0:
            st.write('This is not a cubic equation ')
            option1 = st.multiselect('Would you like the roots as a quadratic equation?','Yes','No')

            if option1 == 'Yes':
                roots = fsolve(quadratic, [0, 0])
                st.write('The roots of the equation are x1: ',roots[0],'and x2: ',roots[1])
            else:
                st.write('Thank you')







        else:

            def cubic(x):
                return a*x**3 + b*x**2 + c*x + d

            roots = fsolve(cubic,[0,0,0])
            st.write('The roots of the equation are x1: ', roots[0], 'and x2: ', roots[1],'and x3: ',roots[2])






