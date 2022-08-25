import math
import numpy as np
global termTypes
termTypes = []
global derivVals
derivVals = []
global evalVals
expVals = []
global evalVals2
expVals2 = []
global coefVals
coefVals = []
global coefVals2
coefVals2 = []
global seccoefVals
seccoefVals = []
global seccoefVals2
seccoefVals2 = []
global otherVals
otherVals = []
global otherVals2
otherVals2 = []
global derivValsa
derivValsa = []
global derivValsa2
derivValsa2 = []
global derivValsb
derivValsb = []
global derivValsb2
derivValsb2 = []
global x
func = int(input("Press 1 for derivative, press 0 for integral, press 2 for evaluated derivative, press 9 for definite integral, press 3 for function evaluation, press 4 for tangent line, press 5 for normal line: "))

#derivative
if func == 1:
  numTerm = int(input("enter number of terms: "))
  tempy = 0
  tem = 0
  tom = 0
  tim = 0
  termVal = 1
  for tempy in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    tempy += 1
    termTypes.append(funcType)
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      print("Derivative complete")
      print("a")
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal) + " exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      newCoef = str(exp*coef)
      newExp = str(exp-1)
      termVal += 1
      tem += 1
      tim += 1
      derivVals.append(newCoef+"x^"+newExp)
    elif termTypes[tim] == 0:
      coef = str(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      if fun == "sin(x)":
        derivative = "cos(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "cos(x)":
        derivative = "-sin(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "e^x":
        derivative = "e^x"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "ln(x)":
        derivative = "x^-1"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      derivVals.append(coef + "*" + derivative)
    if tem == numTerm:
      print("Derivative complete")
    if tem < len(termTypes):
      tem += 1
    if tim == len(termTypes):
      finalD = " + ".join(derivVals)
      print("f'(x) = ", finalD)
      print("Derivative complete")
      break


#integral
if func == 0:
  temp = 0
  numTerm = int(input("enter number of terms: "))
  temp = 0
  tem = 0
  tod = 0
  tim = 0
  termVal = 1
  for temp in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    temp += 1
    termTypes.append(funcType)
    print(termTypes)
    
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      print("Integral complete")
      print("a")
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal)+" exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      if exp == -1:
        newExp = "ln(x)"
        newCoef = coef
        derivVals.append("ln(x) + c")
      elif exp != -1:
        newExp = exp + 1
        newCoef = str(coef/newExp)
        newExpp = str(newExp)
      print("term", termVal, "coefficient is", newCoef)
      print("term", termVal, "exponent is", newExp)
      tim += 1
      tem += 1
      derivVals.append(newCoef+"x^"+newExpp)
      print(derivVals)
      if tem and tim == len(termTypes):
        print("integral complete")
        print("b")
        break
    elif termTypes[tim] == 0:
      coef = str(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      if fun == "sin(x)":
        integral = "-cos(x) + c"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Integral complete")
      if fun == "cos(x)":
        integral = "sin(x) + c"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "-sin(x)":
        integral = "cos(x) + c"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "-cos(x)":
        integral = "-sin(x) + c"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "e^x":
        integral = "e^x + c"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "ln(x)":
        integral = "(xln(x) - x + c)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      print(coef + "*" + integral)
      derivVals.append(coef + " * " + integral)
    termVal += 1
    print(derivVals)
    if tem == numTerm:
      print("integral complete")
      print("c")
      break
    if tem < len(termTypes):
      tem += 1
    else:
      print("integral complete")
      print("d")
      break



#evaluated derivative
if func == 2:
  numTerm = int(input("enter number of terms: "))
  point = float(input("enter desired point for derivative: "))
  tempy = 0
  tem = 0
  tod = 0
  tom = 0
  tim = 0
  termVal = 1
  for tempy in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    tempy += 1
    termTypes.append(funcType)
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      print("Derivative complete")
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal) + " exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      newCoef = float(exp*coef)
      newExp = float(exp-1)
      termVal += 1
      tem += 1
      tim += 1
      expVals.append(newExp)
      coefVals.append(newCoef)
    elif termTypes[tim] == 0:
      coef = float(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      if fun == "sin(x)":
        derivative = "cos(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "cos(x)":
        derivative = "-sin(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "e^x":
        derivative = "e^x"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      if fun == "ln(x)":
        derivative = "x^-1"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Derivative complete")
      seccoefVals.append(coef)
      otherVals.append(derivative)
    if tem == numTerm:
      print("Derivative complete")
    if tem < len(termTypes):
      tem += 1
    if tim == len(termTypes):
      x = point
      while tod < len(expVals) and len(coefVals):
        part = coefVals[tod] * (x**expVals[tod])
        tod += 1
        derivVals.append(part)
      while tom < len(otherVals) and len(seccoefVals):
        specific = otherVals[tom]
        if specific == "cos(x)":
          secPart = seccoefVals[tom] * math.cos(x)
        if specific == "-sin(x)":
          secPart = -1 * seccoefVals[tom] * math.sin(x)
        if specific == "e^x":
          secPart = seccoefVals[tom] * math.exp(x)
        if specific == "x^-1":
          secPart = seccoefVals[tom] * (1//x)
        derivVals.append(secPart)
        tom += 1
      pointVal = sum(derivVals)
      print("f'(",point,") = ", pointVal)
      print("Derivative complete")


#definite integral
if func == 9:
  temp = 0
  numTerm = int(input("enter number of terms: "))
  x = float(input("enter upper boundary: "))
  y = float(input("enter lower boundary: "))
  temp = 0
  tem = 0
  tod = 0
  ton = 0
  tom = 0
  top = 0
  tim = 0
  termVal = 1
  for temp in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    temp += 1
    termTypes.append(funcType)
    
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      print("Integral complete")
      print("a")
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal)+" exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      if exp == -1:
        newExp = "ln(x)"
        newCoef = coef
        derivVals.append("ln(x)")
        
      elif exp != -1:
        newExp = exp + 1
        newCoef = float(coef/newExp)
        newExpp = str(newExp)
        expVals.append(newExp)
        coefVals.append(newCoef)
        
      tim += 1
      tem += 1
    elif termTypes[tim] == 0:
      coef = int(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      seccoefVals.append(coef)
      if fun == "sin(x)":
        integral = "-cos(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("Integral complete")
      if fun == "cos(x)":
        integral = "sin(x)"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "e^x":
        integral = "e^x"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      if fun == "ln(x)":
        integral = "xln(x) - x"
        if tim < len(termTypes):
          tim += 1
        else:
          print("integral complete")
      otherVals.append(integral)
    termVal += 1
    if tim == len(termTypes):
      while tod < len(expVals) and len(coefVals):
        part = coefVals[tod] * (x**expVals[tod])
        tod += 1
        derivValsa.append(part)
      while tom < len(otherVals) and len(seccoefVals):
        specific = otherVals[tom]
        if specific == "-cos(x)":
          secPart = -1 * seccoefVals[tom] * math.cos(x)
        if specific == "sin(x)":
          secPart = seccoefVals[tom] * math.sin(x)
        if specific == "e^x":
          secPart = seccoefVals[tom] * math.exp(x)
        if specific == "xln(x)-x":
          secPart = x*math.log(x)-x
        derivValsa.append(secPart)
        tom += 1
      while ton < len(expVals) and len(coefVals):
        part = coefVals[ton] * (y**expVals[ton])
        ton += 1
        derivValsb.append(part)
      while top < len(otherVals) and len(seccoefVals):
        specific = otherVals[top]
        if specific == "-cos(x)":
          secPart = -1 * seccoefVals[top] * math.cos(y)
          print(secPart)
        if specific == "sin(x)":
          secPart = seccoefVals[top] * math.sin(y)
        if specific == "e^x":
          secPart = seccoefVals[top] * math.exp(y)
        if specific == "xln(x)-x":
          secPart = y*math.log(y)-y
        derivValsb.append(secPart)
        top += 1
      aVal = float(sum(derivValsa))
      bVal = float(sum(derivValsb))
      finalInt = aVal - bVal
      print("integral = ", finalInt)
      print("integral complete")
      break
    if tem == numTerm:
      
      break
    if tem < len(termTypes):
      tem += 1
    else:
      print("integral complete")
      break



#function evaluation
if func == 3:
  x = float(input("Enter point: "))
  numTerm = int(input("enter number of terms: "))
  tempy = 0
  tem = 0
  tom = 0
  tod = 0
  tim = 0
  termVal = 1
  for tempy in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    tempy += 1
    termTypes.append(funcType)
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal) + " exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      expVals.append(exp)
      coefVals.append(coef)
      tem += 1
      tim += 1
    elif termTypes[tim] == 0:
      coef = int(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      seccoefVals.append(coef)
      if fun == "sin(x)":
        otherVals.append(math.sin(x))
        tim += 1
      if fun == "cos(x)":
        otherVals.append(math.cos(x))
        tim += 1
      if fun == "ln(x)":
        otherVals.append(math.log(x))
        tim += 1
      if fun == "e^x":
        otherVals.append(math.exp(x))
        tim += 1
      if fun == "tan(x)":
        otherVals.append(math.tan(x))
        tim += 1
    while tod < len(expVals) and len(coefVals):
      part = coefVals[tod] * (x**expVals[tod])
      tod += 1
      derivValsa.append(part)
    while tom < len(seccoefVals) and len(otherVals):
      tam = seccoefVals[tom] * otherVals[tom]
      tom += 1
      derivValsb.append(tam)
  value = sum(derivValsa) + sum(derivValsb)
  print("f(",x,") = ", value)


#tangent line
if func == 4:
  numTerm = int(input("enter number of terms: "))
  x = float(input("enter desired point for derivative: "))
  tempy = 0
  tem = 0
  tod = 0
  tob = 0
  tom = 0
  top = 0
  tim = 0
  termVal = 1
  for tempy in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    tempy += 1
    termTypes.append(funcType)
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal) + " exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      newCoef = float(exp*coef)
      newExp = float(exp-1)
      termVal += 1
      tem += 1
      tim += 1
      expVals2.append(exp)
      coefVals2.append(coef)
      expVals.append(newExp)
      coefVals.append(newCoef)
    elif termTypes[tim] == 0:
      coef = float(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      if fun == "sin(x)":
        derivative = "cos(x)"
        fun2 = float(math.sin(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "cos(x)":
        derivative = "-sin(x)"
        fun2 = float(math.cos(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "e^x":
        derivative = "e^x"
        fun2 = float(math.exp(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "ln(x)":
        derivative = "x^-1"
        fun2 = float(1//x)
        if tim < len(termTypes):
          tim += 1
      seccoefVals.append(coef)
      seccoefVals2.append(coef)
      otherVals.append(derivative)
      otherVals2.append(fun2)
    if tem < len(termTypes):
      tem += 1
    if tim == len(termTypes):
      point = x
      while tod < len(expVals) and len(coefVals):
        part = coefVals[tod] * (x**expVals[tod])
        tod += 1
        derivVals.append(part)
      while tom < len(otherVals) and len(seccoefVals):
        specific = otherVals[tom]
        if specific == "cos(x)":
          secPart = seccoefVals[tom] * math.cos(x)
          derivVals.append(secPart)
        if specific == "-sin(x)":
          secPart = -1 * seccoefVals[tom] * math.sin(x)
          derivVals.append(secPart)
        if specific == "e^x":
          secPart = seccoefVals[tom] * math.exp(x)
          derivVals.append(secPart)
        if specific == "x^-1":
          secPart = seccoefVals[tom] * (1//x)
          derivVals.append(secPart)
        tom += 1
      while top < len(expVals2) and len(coefVals2):
        part = coefVals2[top] * (x**expVals2[top])
        top += 1
        derivValsa2.append(part)
      while tob < len(seccoefVals2) and len(otherVals2):
        tam = seccoefVals2[tob] * otherVals2[tob]
        tob += 1
        derivValsb2.append(tam)
    pointVal = sum(derivVals)
  value = sum(derivValsa2) + sum(derivValsb2)
  b = -1*(x * pointVal) + value
  print("equation of the line tangent to the curve at ", x,": y = ",pointVal,"*x + ", b)



#normal line
if func == 5:
  numTerm = int(input("enter number of terms: "))
  x = float(input("enter desired point for derivative: "))
  tempy = 0
  tem = 0
  tod = 0
  tob = 0
  tom = 0
  top = 0
  tim = 0
  termVal = 1
  for tempy in range(numTerm):
    funcType = int(input("Press 1 for power function term, press 0 for other: "))
    tempy += 1
    termTypes.append(funcType)
  for tem in range(0, len(termTypes)):
    if tim == len(termTypes):
      break
    elif termTypes[tim] == 1:
      exp = float(input("enter term " + str(termVal) + " exponent: "))
      coef = float(input("enter term " + str(termVal) + " coefficient: "))
      newCoef = float(exp*coef)
      newExp = float(exp-1)
      termVal += 1
      tem += 1
      tim += 1
      expVals2.append(exp)
      coefVals2.append(coef)
      expVals.append(newExp)
      coefVals.append(newCoef)
    elif termTypes[tim] == 0:
      coef = float(input("enter term  " + str(termVal) + " coefficient: "))
      fun = input("enter function: ")
      if fun == "sin(x)":
        derivative = "cos(x)"
        fun2 = float(math.sin(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "cos(x)":
        derivative = "-sin(x)"
        fun2 = float(math.cos(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "e^x":
        derivative = "e^x"
        fun2 = float(math.exp(x))
        if tim < len(termTypes):
          tim += 1
      if fun == "ln(x)":
        derivative = "x^-1"
        fun2 = float(1//x)
        if tim < len(termTypes):
          tim += 1
      seccoefVals.append(coef)
      seccoefVals2.append(coef)
      otherVals.append(derivative)
      otherVals2.append(fun2)
    if tem < len(termTypes):
      tem += 1
    if tim == len(termTypes):
      point = x
      while tod < len(expVals) and len(coefVals):
        part = coefVals[tod] * (x**expVals[tod])
        tod += 1
        derivVals.append(part)
      while tom < len(otherVals) and len(seccoefVals):
        specific = otherVals[tom]
        if specific == "cos(x)":
          secPart = seccoefVals[tom] * math.cos(x)
          derivVals.append(secPart)
        if specific == "-sin(x)":
          secPart = -1 * seccoefVals[tom] * math.sin(x)
          derivVals.append(secPart)
        if specific == "e^x":
          secPart = seccoefVals[tom] * math.exp(x)
          derivVals.append(secPart)
        if specific == "x^-1":
          secPart = seccoefVals[tom] * (1//x)
          derivVals.append(secPart)
        tom += 1
      while top < len(expVals2) and len(coefVals2):
        part = coefVals2[top] * (x**expVals2[top])
        top += 1
        derivValsa2.append(part)
      while tob < len(seccoefVals2) and len(otherVals2):
        tam = seccoefVals2[tob] * otherVals2[tob]
        tob += 1
        derivValsb2.append(tam)
    pointVal = sum(derivVals)
  finalSlope = -1* np.reciprocal(pointVal)
  value = sum(derivValsa2) + sum(derivValsb2)
  b = -1*(x * finalSlope) + value
  print("equation of the line normal to the curve at ", x,": y = ",finalSlope,"*x + ", b)