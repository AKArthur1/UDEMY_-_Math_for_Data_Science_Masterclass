### Python Showcase CMath Methods ###
print("Beginning of the Python CMath Methods Showcase\n\n\n")

import cmath

print("Python has a built-in module that you can use for mathematical tasks for complex numbers.\n"
      "The methods in this module accepts int, float, and complex numbers. It even accepts Python objects that has a __complex__() or __float__() method.\n"
      "The methods in this module almost always return a complex number. If the return value can be expressed as a real number, the return value has an imaginary part of 0.\n"
      "The cmath module has a set of methods and constants.")




CMath_ArcCosine_def = "CMath Arc Cosine: The cmath.acos() method returns the arc cosine of a complex number. There are two branch cuts: Extends right from 1 along the real axis to ∞ Extends left from -1 along the real axis to -∞."
print(f"\n{CMath_ArcCosine_def}")
print("    #find the arc cosine of a complex number")
print(f"        print(cmath.acos(2+3j)) = {cmath.acos(2+3j)}")




CMath_ArcCosineHyperbolic_def = "CMath_ArcCosine Hyperbolic: The cmath.acosh() method returns the inverse hyperbolic cosine of a complex number. There is one branch cut: Extending left from 1 along the real axis to -∞, continuous from above"
print(f"\n{CMath_ArcCosineHyperbolic_def}")
print("    #find the hyperbolic arc cosine of a complex number")
print(f"        print(cmath.acos(2 + 3j)) = {cmath.acos(2 + 3j)}")




CMath_ArcSin_def = "CMath ArcSin: The cmath.asin() method returns the arc sine of a complex number. There are two branch cuts: Extends right from 1 along the real axis to ∞ Extends left from -1 along the real axis to -∞"
print(f"\n{CMath_ArcSin_def}")
print("    #find the arc sine of a complex number")
print(f"        print(cmath.asin(2 + 3j)) = {cmath.asin(2 + 3j)}")




CMath_ArcSineHyperbolic_def = "CMath Arc Sine Hyperbolic: The cmath.asinh() method returns the inverse hyperbolic sine of a number. There are mainly two branch cuts: Extending from 1j along the imaginary axis to ∞j towards the right Extending from -1j along the imaginary axis to -∞j towards left"
print(f"\n{CMath_ArcSineHyperbolic_def}")
print("    #find the hyperbolic arc sine of a complex number")
print(f"        print(cmath.asinh(2+3j)) = {cmath.asinh(2+3j)}")





CMath_ArcTangent_def = "CMath Arc tangent: The cmath.atan() method returns the arc tangent of a complex number. There are mainly two branch cuts: Extending from 1j along the imaginary axis to ∞j towards the right Extending from -1j along the imaginary axis to -∞j towards left"
print(f"\n{CMath_ArcTangent_def}")
print("    #find the arc tangent of a complex number")
print(f"        print(cmath.atan(2 + 3j)) = {cmath.atan(2 + 3j)}")





CMath_ArcTangentHyperbolic_def = "CMath Arc Tangent Hyperbolic: The cmath.atanh() method returns the inverse hyperbolic tangent of a complex number. There are two branch cuts: Extends from 1 along the real axis to ∞, continuous from below Extends from -1 along the real axis to -∞, continuous from above"
print(f"\n{CMath_ArcTangentHyperbolic_def}")
print("    #find the hyperbolic arctangent of a complex number")
print(f"        print(cmath.atanh(2+ 3j)) = {cmath.atanh(2+ 3j)}")




CMath_Cosine_def = "CMath Cosine: The cmath.cos() method returns the cosine of a complex number."
print(f"\n{CMath_Cosine_def}")
print("    #find the cosine of a complex number")
print(f"        print(cmath.cos(2 + 3j)) = {cmath.cos(2 + 3j)}")





CMath_CosineHyperbolic_def = "CMath Cosine Hyperbolic: The cmath.cosh() method returns the hyperbolic cosine of a complex number."
print(f"\n{CMath_CosineHyperbolic_def}")
print("    #find the hyperbolic cosine of a complex number")
print(f"        print(cmath.cosh(2 + 3j)) = {cmath.cosh(2 + 3j)}")




CMath_ExponentialValue_def = "CMath Exponential Value: The cmath.exp() method accepts a complex number and returns the exponential value. If the number is x, it returns e**x where e is the base of natural logarithms."
print(f"\n{CMath_ExponentialValue_def}")
print("    #find the exponential of a complex number")
print(f"        print(cmath.exp(2 + 3j)) = {cmath.exp(2 + 3j)}")




CMath_IsCLose_def = "CMath Is Close: The cmath.isclose() method checks whether two complex values are close, or not. This method returns a Boolean value: True if the values are close, otherwise False. This method uses a relative tolerance, or an absolute tolerance, to see if the values are close. Tip: It uses the following formula to compare the values: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)"
print(f"\n{CMath_IsCLose_def}")
print("    #compare the closeness of two complex values using relative tolerance")
print(f"        print(cmath.isclose(10+5j, 10+5j)) = {cmath.isclose(10+5j, 10+5j)}")
print(f"        print(cmath.isclose(10+5j, 10.01+5j)) = {cmath.isclose(10+5j, 10.01+5j)}")





CMath_IsFinite_def = "CMath Is Finite: The cmath.isfinite() method checks whether a complex value is finite, or not. This method returns a Boolean value: True if the value is finite, otherwise False."
print(f"\n{CMath_IsFinite_def}")
print("    #find whether a complex number is finite or not")
print(f"        print(cmath.isfinite(2 + 3j)) = {cmath.isfinite(2 + 3j)}")
print(f"        print(cmath.isfinite(complex(5.0,float('inf')))) = {cmath.isfinite(complex(5.0,float('inf')))}")
print(f"        print(cmath.isfinite(float('inf')+ 5j)) = {cmath.isfinite(float('inf')+ 5j)}")




CMath_IsInfinity_def = "CMath Is Infinity: The cmath.isinf() method checks whether a value is positive or negative infinity, or not. This method returns a Boolean value: True if the value is infinity, otherwise False."
print(f"\n{CMath_IsInfinity_def}")
print("    #find whether a complex number is infinite or not")
print(f"        print(cmath.isinf(complex(10 + float('inf')))) = {cmath.isinf(complex(10 + float('inf')))}")
print(f"        print(cmath.isinf(11 + 4j)) = {cmath.isinf(11 + 4j)}")





CMath_IsNotANumber_def = "CMath Is Not A Number: The cmath.isnan() method checks whether a value is nan (Not a Number), or not. This method returns a Boolean value: True if the value is nan, otherwise False"
print(f"\n{CMath_IsNotANumber_def}")
print("    #find whether a complex number is NaN or not")
print(f"        print(cmath.isnan(12 + float('nan'))) = {cmath.isnan(12 + float('nan'))}")
print(f"        print(cmath.isnan(2 + 3j)) = {cmath.isnan(2 + 3j)}")




CMath_Logarithm_def = "CMath Logarithm: The cmath.log() method returns the logarithm of a complex value. With a single argument, this method returns the natural logarithm of that argument with base e. With two arguments, this method returns the logarithm of the first argument (x) with the base of the second argument (base)."
print(f"\n{CMath_Logarithm_def}")
print("    #print log value of some given parameters")
print(f"        print(cmath.log(1+ 1j)) = {cmath.log(1+ 1j)}")
print(f"        print(cmath.log(1, 2.5)) = {cmath.log(1, 2.5)}")




CMath_LogarithmBase10_def = "The cmath.log10() method returns the base-10 logarithm of a complex number. There is one branch cut, from 0 along the negative real axis to -∞, continuous from above."
print(f"\n{CMath_LogarithmBase10_def}")
print("    #print base-10 log value of complex numbers")
print(f"        print(cmath.log10(2+ 3j)) = {cmath.log10(2+ 3j)}")
print(f"        print(cmath.log10(1+ 2j)) = {cmath.log10(1+ 2j)}")




CMath_Phase_def = "CMath Phase: The cmath.phase() method returns the phase of a complex number. A complx number can be expressed in terms of its magnitude and angle. This angle is between vector (representing complex number) and positive x-axis is called Phase. Note: Output is always between -π and π."
print(f"\n{CMath_Phase_def}")
print("    #print phase of some given parameters")
print(f"        print(cmath.phase(2 + 3j)) = {cmath.phase(2 + 3j)}")




CMath_PolarConvert_def = "CMath Polar Convert: The cmath.polar() method converts a complex number to polar coordinates. It returns a tuple of modulus and phase. In polar coordinates, a complex number is defined by modulus r and phase angle phi."
print(f"\n{CMath_PolarConvert_def}")
print("    #find the polar coordinates of complex number")
print(f"        print(cmath.polar(2 + 3j)) = {cmath.polar(2 + 3j)}")
print(f"        print(cmath.polar(1 + 5j)) = {cmath.polar(1 + 5j)}")




CMath_RectangularConvert_def = "CMath Rectangular Convert: The cmath.rect() method converts polar coordinates to rectangular form of the complex number. It creates a complex number with phase and modulus. This method is equivalent to r * (math.cos(phi) + math.sin(phi)*1j). Note: The radius r is the length of the vector, and phi (phase angle) is the angle made with the real axis."
print(f"\n{CMath_RectangularConvert_def}")
print("    #convert a polar coordinate to rectangular form")
print(f"        print(cmath.rect(3.1622776601683795, 1.2490457723982544)) = {cmath.rect(3.1622776601683795, 1.2490457723982544)}")




CMath_Sine_def = "CMath Sine: The cmath.sin() method returns the sine of a number. Sine is a trigonometric function representing the ratio between opposite side of a right triangle and hypotenuse."
print(f"\n{CMath_Sine_def}")
print("    #find the sine of complex number")
print(f"        print(cmath.sin(2 + 3j)) = {cmath.sin(2 + 3j)}")




CMath_SineHyperbolic_def = "CMath Sine Hyperbolic: The cmath.sinh() method returns the hyperbolic sine of a complex number."
print(f"\n{CMath_SineHyperbolic_def}")
print("    #find the hyperbolic sine of a complex number")
print(f"        print(cmath.sinh(2 + 3j)) = {cmath.sinh(2 + 3j)}")





CMath_SquareRoot_def = "CMath Square Root: The cmath.sqrt() method returns the square root of a complex number. Note: The number must be greater than or equal to 0."
print(f"\n{CMath_SquareRoot_def}")
print("    #Return the square root of a complex number")
print(f"        print(cmath.sqrt(2 + 3j)) = {cmath.sqrt(2 + 3j)}")
print(f"        print(cmath.sqrt(15)) = {cmath.sqrt(15)}")




CMath_Tangent_def = "CMath Tangent: The cmath.tan() method returns the tangent of a complex number."
print(f"\n{CMath_Tangent_def}")
print("    #Return the tangent of a complex number")
print(f"        print(cmath.tan(2 + 3j)) = {cmath.tan(2 + 3j)}")




CMath_TangentHyperbolic_def = "CMath TangentHyperbolic: The cmath.tanh() method returns the hyperbolic tangent of a complex number."
print(f"\n{CMath_TangentHyperbolic_def}")
print("    #Return the hyperbolic tangent of a complex number")
print(f"        print(cmath.tanh(2 + 3j)) = {cmath.tanh(2 + 3j)}")




CMath_Eular_def = "CMath Eular: The cmath.e constant returns the Euler's number: 2.718281828459045."
print(f"\n{CMath_Eular_def}")
print("    # Print the value of Euler e")
print(f"        print(cmath.e) = {cmath.e}")





CMath_Infinity_def = "CMath infinity: The cmath.inf constant returns a floating-point positive infinity. For negative infinity, use -cmath.inf. The cmath.inf constant is equivalent to float('inf')."
print(f"\n{CMath_Infinity_def}")
print("    # Print the positive infinity")
print(f"        print(cmath.inf) = {cmath.inf}")
print("    # Print the negative infinity")
print(f"        print(-cmath.inf) = {-cmath.inf}")




CMath_InfinityComplex_def = "CMath Infinity Complex: The cmath.infj constant returns a complex positive infinity. The return has a 0 real part, and positive infinity as the imaginary part. The cmath.infj constant is equivalent to complex(0.0, float('inf'))."
print(f"\n{CMath_InfinityComplex_def}")
print("    # Print complex infinity")
print(f"        print(cmath.infj) = {cmath.infj}")






CMath_NotANumber_def = "CMath Not A Number:The cmath.nan constant returns a floating-point nan (Not a Number) value. This value is not a legal number. The nan constant is equivalent to float('nan') or math.nan."
print(f"\n{CMath_NotANumber_def}")
print("    # Print the value of nan")
print(f"        print(cmath.nan) = {cmath.nan}")




CMath_NotANumberComplex_def = "CMath Not A Number: The cmath.nanj constant returns a complex nan (Not a Number) value. This value has a 0 real part, and nan as the imaginarly part. The nanj constant is equivalent to complex(0.0,float('nan')."
print(f"\n{CMath_NotANumberComplex_def}")
print("    # Print the value of nan")
print(f"        print(cmath.nanj) = {cmath.nanj}")
print(f"        print(type(cmath.nanj)) = {type(cmath.nanj)}")




CMath_Pi_def = "CMath Pi: The cmath.pi constant returns the value pi: 3.141592653589793. It is defined as the ratio of the circumference to the diameter of a circle. Note: Mathematically pi is represented by π."
print(f"\n{CMath_Pi_def}")
print("    # Print the value of pi")
print(f"        print(cmath.pi) = {cmath.pi}")




CMath_tau_def = "CMath Tau: The cmath.tau constant returns tau, which is 6.283185307179586. It is defined as the ratio of the circumference to the radius of a circle. Tau is a circle constant and the value is equivalent to 2π. Note: Mathematically tau is represented by τ."
print(f"\n{CMath_tau_def}")
print("    #Print the value of tau")
print(f"        print(cmath.tau) = {cmath.tau}")



print("\n\n\nEnd of the Python CMath Methods Showcase")