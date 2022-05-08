#operadores logios, permite contruir expresiones logicas, se obtiene de resultados booleanos
"""
AND         and
OR          or
NEGACION    not
"""
print("OPERADORES LOGICOS")
print("""Operador and
Operador1 operador   operador2 Resultado
True        and        True     True
True        and        False    False
False       and        True     False
False       and        False    False
""")


print("""\nOperador or
Operador1 operador   operador2 Resultado
True        and        True     True
True        and        False    True
False       and        True     True
False       and        False    False
""")

print("""\nOperador not
Operando        Resultado
not (True)      False
not (False)     True
""")

#prioridad de los operadores logicos
"""
lo priemro que se evalua en la sentencia 
1. NOT
2. AND
3. OR
"""

a=10
b=12
c=13
d=10
Resultado=((a>b) or (a<c))and((a==c)or(a>=b))
""" F   or    T     and         F  or      F
        T            and           F
                F
"""
print("\n",Resultado, "linea 48")


#Prioridad de los operadores en General
"""
1. ()
2.**
3. *,/,mod, not
4. +,-,and
5. >,<,==,>=,<=,!=, or
"""


a=10
b=15
c=20
resultado = not((a>b) or (b<c))
print("\n",resultado)