### Python Showcase Math Methods ###
print("Beginning of the Python Math Methods Showcase\n\n\n")

import math


Math_ArcCosine_def = "Math Arc Cosine: The math.acos() method returns the arc cosine value of a number. Note: The parameter passed in math.acos() must lie between -1 to 1. Tip: math.acos(-1) will return the value of PI."
print(f"\n{Math_ArcCosine_def}")
print("    # Return the arc cosine of numbers")
print(f"        print(math.acos(0.55)) = {math.acos(0.55)}")
print(f"        print(math.acos(-0.55)) = {math.acos(-0.55)}")
print(f"        print(math.acos(0)) = {math.acos(0)}")
print(f"        print(math.acos(1)) = {math.acos(1)}")
print(f"        print(math.acos(-1)) = {math.acos(-1)}")




Math_InverseCosine_def = "Math Inverse Cosine: The math.acosh() method returns the inverse hyperbolic cosine of a number. Note: The parameter passed in acosh() must be greater than or equal to 1."
print(f"\n{Math_InverseCosine_def}")
print("    # Return the inverse hyperbolic cosine of different numbers")
print(f"        print(math.acosh(7)) = {math.acosh(7)}")
print(f"        print(math.acosh(56)) = {math.acosh(56)}")
print(f"        print(math.acosh(2.45)) = {math.acosh(2.45)}")
print(f"        print(math.acosh(1)) = {math.acosh(1)}")





Math_ArcSine_def = "Math Arc Sine: The math.asin() method returns the arc sine of a number. Note: The parameter passed in math.asin() must lie between -1 to 1. Tip: math.asin(1) will return the value of PI/2, and math.asin(-1) will return the value of -PI/2."
print(f"\n{Math_ArcSine_def}")
print("    # Return the arc sine of numbers")
print(f"        print(math.asin(0.55)) = {math.asin(0.55)}")
print(f"        print(math.asin(-0.55)) = {math.asin(-0.55)}")
print(f"        print(math.asin(0)) = {math.asin(0)}")
print(f"        print(math.asin(1)) = {math.asin(1)}")
print(f"        print(math.asin(-1)) = {math.asin(-1)}")




Math_InverseArcSine_def = "Math Inverse Sine: The math.asinh() method returns the inverse hyperbolic sine of a number."
print(f"\n{Math_InverseArcSine_def}")
print("    # Return the hyperbolic arc sine value of numbers")
print(f"        print(math.asinh(7)) = {math.asinh(7)}")
print(f"        print(math.asinh(56)) = {math.asinh(56)}")
print(f"        print(math.asinh(2.45)) = {math.asinh(2.45)}")
print(f"        print(math.asinh(1)) = {math.asinh(1)}")
print(f"        print(math.asinh(0.5)) = {math.asinh(0.5)}")
print(f"        print(math.asinh(-10)) = {math.asinh(-10)}")





Math_ArcTangent_def = "Math Arc Tangent: The math.atan() method returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians. Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated."
print(f"\n{Math_ArcTangent_def}")
print("    #find the arctangent of some values")
print(f"        print(math.atan(0.39)) = {math.atan(0.39)}")
print(f"        print(math.atan(67)) = {math.atan(67)}")
print(f"        print(math.atan(-21)) = {math.atan(-21)}")





Math_ArcTangent_XY_def = "Math Arc Tangent XY: The math.atan2() method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y). The returned value is between PI and -PI."
print(f"\n{Math_ArcTangent_XY_def}")
print("    # Return the arc tangent of y/x in radians")
print(f"        print(math.atan2(8, 5)) = {math.atan2(8, 5)}")
print(f"        print(math.atan2(20, 10)) = {math.atan2(20, 10)}")
print(f"        print(math.atan2(34, -7)) = {math.atan2(34, -7)}")
print(f"        print(math.atan2(-340, -120)) = {math.atan2(-340, -120)}")





Math_InverseHyperbolicTangent_def = "Math Inverse Hyperbolic Tangent: The math.atanh() method returns the inverse hyperbolic tangent of a number. Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99."
print(f"\n{Math_InverseHyperbolicTangent_def}")
print("    #print the hyperbolic arctangent of different numbers")
print(f"        print(math.atanh(0.59)) = {math.atanh(0.59)}")
print(f"        print(math.atanh(-0.12)) = {math.atanh(-0.12)}")
print(f"        print(math.atanh(0.99)) = {math.atanh(0.99)}")




Math_Ceiling_def = "Math Ceiling: The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result. Tip: To round a number DOWN to the nearest integer, look at the math.floor() method."
print(f"\n{Math_Ceiling_def}")
print("    # Round a number upward to its nearest integer")
print(f"        print(math.ceil(1.4)) = {math.ceil(1.4)}")
print(f"        print(math.ceil(5.3)) = {math.ceil(5.3)}")
print(f"        print(math.ceil(-5.3)) = {math.ceil(-5.3)}")
print(f"        print(math.ceil(22.6)) = {math.ceil(22.6)}")
print(f"        print(math.ceil(10.0)) = {math.ceil(10.0)}")



Math_CombinationsPossible_def = "Math Combinations Possible: The math.comb() method returns the number of ways picking k unordered outcomes from Math_Comb_n possibilities, without repetition, also known as combinations. Note: The parameters passed in this method must be positive integers."
print(f"\n{Math_CombinationsPossible_def}")
Math_Comb_n = 7
Math_Comb_k = 5
print("    # Initialize the number of items to choose from")
print("    Math_Comb_n = 7")
print("    # Initialize the number of possibilities to choose")
print("    Math_Comb_k = 5")
print("    # Print total number of possible combinations")
print(f"        print(math.comb(Math_Comb_n, Math_Comb_k)) = {math.comb(Math_Comb_n, Math_Comb_k)}")




Math_CopySign_def = "Math CopySign: The math.copysign() method returns a float consisting of the value of the first parameter and the sign(+/-) of the second parameter."
print(f"\n{Math_CopySign_def}")
print("    #Return the value of the first parameter and the sign of the second parameter")
print(f"        print(math.copysign(4, -1)) = {math.copysign(4, -1)}")
print(f"        print(math.copysign(-8, 97.21)) = {math.copysign(-8, 97.21)}")
print(f"        print(math.copysign(-43, -76)) = {math.copysign(-43, -76)}")




Math_Cosine_def = "Math Cosine: The math.cos() method returns the cosine of a number."
print(f"\n{Math_Cosine_def}")
print("    # Return the cosine of different numbers")
print(f"        print(math.cos(0.00)) = {math.cos(0.00)}")
print(f"        print(math.cos(-1.23)) = {math.cos(-1.23)}")
print(f"        print(math.cos(10)) = {math.cos(10)}")
print(f"        print(math.cos(3.14159265359)) = {math.cos(3.14159265359)}")





Math_CosineHyperbolic_def = "Math Cosine Hyperbolic: The math.cosh() method returns the hyperbolic cosine of a number (equivalent to (exp(number) + exp(-number)) / 2)."
print(f"\n{Math_CosineHyperbolic_def}")
print("    # Return the hyperbolic cosine of different numbers")
print(f"        print(math.cosh(1)) = {math.cosh(1)}")
print(f"        print(math.cosh(8.90)) = {math.cosh(8.90)}")
print(f"        print(math.cosh(0)) = {math.cosh(0)}")
print(f"        print(math.cosh(1.52)) = {math.cosh(1.52)}")




Math_Degrees_def = "Math_Degrees: The mmath.degrees() method converts an angle from radians to degrees. Tip: PI (3.14..) radians are equal to 180 degrees, which means that 1 radian is equal to 57.2957795 degrees. Tip: See also math.radians() to convert a degree value into radians."
print(f"\n{Math_Degrees_def}")
print("    # Convert from radians to degrees:")
print(f"        print(math.degrees(8.90)) = {math.degrees(8.90)}")
print(f"        print(math.degrees(-20)) = {math.degrees(-20)}")
print(f"        print(math.degrees(1)) = {math.degrees(1)}")
print(f"        print(math.degrees(90)) = {math.degrees(90)}")




Math_DistanceEuclidean_def = "Math Distance Euclidean: The math.dist() method returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point. Note: The two points (p and q) must be of the same dimensions."
print(f"\n{Math_DistanceEuclidean_def}")
print("    Math_DistEuc_p = [3]")
print("    Math_DistEuc_q = [1]")
Math_DistEuc_p = [3]
Math_DistEuc_q = [1]
print("    # Calculate Euclidean distance")
print(f"        print(math.dist(Math_DistEuc_p, Math_DistEuc_q)) = {math.dist(Math_DistEuc_p, Math_DistEuc_q)}")
print("    Math_DistEuc_p = [3, 3]")
print("    Math_DistEuc_q = [6, 12]")
Math_DistEuc_p = [3, 3]
Math_DistEuc_q = [6, 12]
print("    # Calculate Euclidean distance")
print(f"        print(math.dist(Math_DistEuc_p, Math_DistEuc_q)) = {math.dist(Math_DistEuc_p, Math_DistEuc_q)}")





Math_ErrorFunction_def = "Math Error Function: The math.erf() method returns the error function of a number. This method accepts a value between - inf and + inf, and returns a value between - 1 to + 1."
print(f"\n{Math_ErrorFunction_def}")
print("    #Print the error function of a number")
print(f"        print(math.erf(0.67)) = {math.erf(0.67)}")
print(f"        print(math.erf(1.34)) = {math.erf(1.34)}")
print(f"        print(math.erf(-6)) = {math.erf(-6)}")





Math_ErrorFunctionComplementary_def = "Math Error Function Complementary: The math.erfc() method returns the complementary error function of a number. This method accepts a value between - inf and + inf, and returns a value between 0 and 2."
print(f"\n{Math_ErrorFunctionComplementary_def}")
print("    #Print the complementary error function of a number")
print(f"        print(math.erfc(0.67)) = {math.erfc(0.67)}")
print(f"        print(math.erfc(1.34)) = {math.erfc(1.34)}")
print(f"        print(math.erfc(-6)) = {math.erfc(-6)}")





Math_Exponential_def = "Math Exponential: The math.exp() method returns E raised to the power of x (Ex). 'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it."
print(f"\n{Math_Exponential_def}")
print("    #find the exponential of the specified value")
print(f"        print(math.exp(65)) = {math.exp(65)}")
print(f"        print(math.exp(-6.89)) = {math.exp(-6.89)}")





Math_ExponentialMinus1_def = "Math Exponential Minus 1: The math.expm1() method returns Ex - 1. 'E' is the base of the natural system of logarithms (approximately 2.718282) and x is the number passed to it. This function is more accurate than calling math.exp() and subtracting 1."
print(f"\n{Math_ExponentialMinus1_def}")
print("    #Return the exponential ex-1 ")
print(f"        print(math.expm1(32)) = {math.expm1(32)}")
print(f"        print(math.expm1(-10.89)) = {math.expm1(-10.89)}")




Math_AbsoluteValueFloat_def = "Math Absolute Value Float: The math.fabs() method returns the absolute value of a number, as a float. Absolute denotes a non-negative number. This removes the negative sign of the value if it has any. Unlike Python abs(), this method always converts the value to a float value."
print(f"\n{Math_AbsoluteValueFloat_def}")
print("    #Remove - sign of given number")
print(f"        print(math.fabs(-66.43)) = {math.fabs(-66.43)}")
print(f"        print(math.fabs(-7)) = {math.fabs(-7)}")




Math_Factorial_def = "Math Factorial: The math.factorial() method returns the factorial of a number. Note: This method only accepts positive integers. The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number down to 1. For example, the factorial of 6 would be 6 x 5 x 4 x 3 x 2 x 1 = 720"
print(f"\n{Math_Factorial_def}")
print("    #Return factorial of a number")
print(f"        print(math.factorial(9)) = {math.factorial(9)}")
print(f"        print(math.factorial(6)) = {math.factorial(6)}")
print(f"        print(math.factorial(12)) = {math.factorial(12)}")




Math_Floor_def = "Math Floor: The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result. Tip: To round a number UP to the nearest integer, look at the math.ceil() method."
print(f"\n{Math_Floor_def}")
print("    # Round numbers down to the nearest integer")
print(f"        print(math.floor(0.6)) = {math.floor(0.6)}")
print(f"        print(math.floor(1.4)) = {math.floor(1.4)}")
print(f"        print(math.floor(5.3) = {math.floor(5.3)}")
print(f"        print(math.floor(-5.3)) = {math.floor(-5.3)}")
print(f"        print(math.floor(22.6)) = {math.floor(22.6)}")
print(f"        print(math.floor(10.0)) = {math.floor(10.0)}")




Math_Modulo_def = "Math Modulo: The math.fmod() method returns the remainder (modulo) of x/y."
print(f"\n{Math_Modulo_def}")
print("    # Return the remainder of x/y")
print(f"        print(math.fmod(20, 4)) = {math.fmod(20, 4)}")
print(f"        print(math.fmod(20, 3)) = {math.fmod(20, 3)}")
print(f"        print(math.fmod(20, 3)) = {math.fmod(15, 6)}")
print(f"        print(math.fmod(-10, 3)) = {math.fmod(-10, 3)}")
print(f"        print(math.fmod(0, 0)) = ValueError")





Math_ExponentMantissa_def = "Math Exponent Mantissa: The math.frexp() method returns the mantissa and the exponent of a specified number, as a pair (m,e). The mathematical formula for this method is: number = m * 2**e."
print(f"\n{Math_ExponentMantissa_def}")
print("    #Return mantissa and exponent of a given number")
print(f"        print(math.frexp(4)) = {math.frexp(4)}")
print(f"        print(math.frexp(-4)) = {math.frexp(-4)}")
print(f"        print(math.frexp(7)) = {math.frexp(7)}")





Math_FSum_def = "MAth FSum: The math.fsum() method returns the sum of all items in any iterable (tuples, arrays, lists, etc.)."
print(f"\n{Math_FSum_def}")
print("    # Print the sum of all items ")
print(f"        print(math.fsum([1, 2, 3, 4, 5])) = {math.fsum([1, 2, 3, 4, 5])}")
print(f"        print(math.fsum([100, 400, 340, 500])) = {math.fsum([100, 400, 340, 500])}")
print(f"        print(math.fsum([1.7, 0.3, 1.5, 4.5])) = {math.fsum([1.7, 0.3, 1.5, 4.5])}")





Math_Gamma_def = "Math Gamma: The math.gamma() method returns the gamma function at a number. Tip: To find the log gamma value of a number, use the math.lgamma() method."
print(f"\n{Math_Gamma_def}")
print("    # Return the gamma function for different numbers")
print(f"        print(math.gamma(-0.1)) = {math.gamma(-0.1)}")
print(f"        print(math.gamma(8)) = {math.gamma(8)}")
print(f"        print(math.gamma(1.2)) = {math.gamma(1.2)}")
print(f"        print(math.gamma(80)) = {math.gamma(80)}")
print(f"        print(math.gamma(-0.55)) = {math.gamma(-0.55)}")




Math_GreatestCommonDivisor_def = "Math Greatest Common Divisor: The math.gcd() method returns the greatest common divisor of the two integers int1 and int2. GCD is the largest common divisor that divides the numbers without a remainder. GCD is also known as the highest common factor (HCF). Tip: gcd(0,0) returns 0."
print(f"\n{Math_GreatestCommonDivisor_def}")
print("    #find the  the greatest common divisor of the two integers")
print(f"        print(math.gcd(3, 6)) = {math.gcd(3, 6)}")
print(f"        print(math.gcd(6, 12)) = {math.gcd(6, 12)}")
print(f"        print(math.gcd(12, 36)) = {math.gcd(12, 36)}")
print(f"        print(math.gcd(-12, -36)) = {math.gcd(-12, -36)}")
print(f"        print(math.gcd(5, 12)) = {math.gcd(5, 12)}")
print(f"        print(math.gcd(10, 0)) = {math.gcd(10, 0)}")
print(f"        print(math.gcd(0, 34)) = {math.gcd(0, 34)}")
print(f"        print(math.gcd(0, 0)) = {math.gcd(0, 0)}")




Math_Hypotenuse_def = "Math Hypotenuse: The math.hypot() method returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given."
print(f"\n{Math_Hypotenuse_def}")
print("    #set perpendicular and base")
print("    Math_Hypot_parendicular = 10")
print("    Math_Hypot_base = 5")
Math_Hypot_parendicular = 10
Math_Hypot_base = 5
print("    #print the hypotenuse of a right-angled triangle")
print(f"        print(math.hypot(Math_Hypot_parendicular, Math_Hypot_base)) = {math.hypot(Math_Hypot_parendicular, Math_Hypot_base)}")




Math_IsClose_Def = "Math Is Close: The math.isclose() method checks whether two values are close to each other, or not. Returns True if the values are close, otherwise False. This method uses a relative or absolute tolerance, to see if the values are close. Tip: It uses the following formula to compare the values: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)"
print(f"\n{Math_IsClose_Def}")
print("    #compare the closeness of two values")
print(f"        print(math.isclose(1.233, 1.4566)) = {math.isclose(1.233, 1.4566)}")
print(f"        print(math.isclose(1.233, 1.233)) = {math.isclose(1.233, 1.233)}")
print(f"        print(math.isclose(1.233, 1.24)) = {math.isclose(1.233, 1.24)}")
print(f"        print(math.isclose(1.233, 1.233000001)) = {math.isclose(1.233, 1.233000001)}")




Math_IsFinite_def = "Math Is Finite: The math.isfinite() method checks whether a number is finite or not. This method returns True if the specified number is a finite number, otherwise it returns False."
print(f"\n{Math_IsFinite_def}")
print("    # Check whether the values are finite or not")
print(f"        print(math.isfinite(2000)) = {math.isfinite(2000)}")
print(f"        print(math.isfinite(-45.34)) = {math.isfinite(-45.34)}")
print(f"        print(math.isfinite(+45.34)) = {math.isfinite(+45.34)}")
print(f"        print(math.isfinite(math.inf)) = {math.isfinite(math.inf)}")
print(f"        print(math.isfinite(float('nan'))) = {math.isfinite(float('nan'))}")
print(f"        print(math.isfinite(float('inf'))) = {math.isfinite(float('inf'))}")
print(f"        print(math.isfinite(float('-inf'))) = {math.isfinite(float('-inf'))}")
print(f"        print(math.isfinite(-math.inf)) = {math.isfinite(-math.inf)}")
print(f"        print(math.isfinite(0.0)) = {math.isfinite(0.0)}")




Math_IsInf_def = "Math Is Inf: The math.isinf() method checks whether a number is infinite or not. This method returns True if the specified number is a positive or negative infinity, otherwise it returns False."
print(f"\n{Math_IsInf_def}")
print("    # Check whether some values are infinite")
print(f"        print(math.isinf (56)) = {math.isinf (56)}")
print(f"        print(math.isinf (-45.34)) = {math.isinf (-45.34)}")
print(f"        print(math.isinf (+45.34)) = {math.isinf (+45.34)}")
print(f"        print(math.isinf (math.inf)) = {math.isinf (math.inf)}")
print(f"        print(math.isinf (float('nan'))) = {math.isinf (float('nan'))}")
print(f"        print(math.isinf (float('-inf'))) = {math.isinf (float('-inf'))}")
print(f"        print(math.isinf (-math.inf)) = {math.isinf (-math.inf)}")




Math_IsNotANumber_def = "Math Is NaN(Not A Number): The math.isnan() method checks whether a value is NaN (Not a Number), or not. This method returns True if the specified value is a NaN, otherwise it returns False."
print(f"\n{Math_IsNotANumber_def}")
print("    # Check whether some values are NaN")
print(f"        print(math.isnan (56)) = {math.isnan (56)}")
print(f"        print(math.isnan (-45.34)) = {math.isnan (-45.34)}")
print(f"        print(math.isnan (+45.34)) = {math.isnan (+45.34)}")
print(f"        print(math.isnan (math.inf)) = {math.isnan (math.inf)}")
print(f"        print(math.isnan (float('nan'))) = {math.isnan (float('nan'))}")
print(f"        print(math.isnan (float('inf'))) = {math.isnan (float('inf'))}")
print(f"        print(math.isnan (float('-inf'))) = {math.isnan (float('-inf'))}")
print(f"        print(math.isnan (math.nan)) = {math.isnan (math.nan)}")





Math_SquareRoot_Round_Down_def = "Math Square Root Round Down: The math.isqrt() method rounds a square root number downwards to the nearest integer. Note: The number must be greater than or equal to 0."
print(f"\n{Math_SquareRoot_Round_Down_def}")
print("    # Round square root numbers downward to the nearest integer")
print(f"        print(math.isqrt(10)) = {math.isqrt(10)}")
print(f"        print(math.isqrt (12)) = {math.isqrt (12)}")
print(f"        print(math.isqrt (68)) = {math.isqrt (68)}")
print(f"        print(math.isqrt (100)) = {math.isqrt (100)}")




Math_LDexp_def = "Math LDexp: The math.ldexp() method returns  x * (2**i) of the given numbers x and i, which is the inverse of math.frexp()."
print(f"\n{Math_LDexp_def}")
print("    #Return value of x * (2**i)")
print(f"        print(math.ldexp(9, 3)) = {math.ldexp(9, 3)}")
print(f"        print(math.ldexp(-5, 2)) = {math.ldexp(-5, 2)}")
print(f"        print(math.ldexp(15, 2)) = {math.ldexp(15, 2)}")




Math_LogarithmGamma_def = "Math Logarithm Gamma: The math.lgamma() method returns the natural logarithm gamma value of a number. Tip: We can find also find the log gamma value by using the math.gamma() method to find the gamma value, and then use the math.log() method to calculate the log of that value. Tip: The gamma value is equal to factorial(x-1)."
print(f"\n{Math_LogarithmGamma_def}")
print("    # Return the log gamma value of different numbers")
print(f"        print(math.lgamma(7)) = {math.lgamma(7)}")
print(f"        print(math.lgamma(-4.2)) = {math.lgamma(-4.2)}")




Math_Logarithm_def = "Math Logarithm: The math.log() method returns the natural logarithm of a number, or the logarithm of number to base."
print(f"\n{Math_Logarithm_def}")
print("    # Return the natural logarithm of different numbers")
print(f"        print(math.log(2.7183)) = {math.log(2.7183)}")
print(f"        print(math.log(2)) = {math.log(2)}")
print(f"        print(math.log(1)) = {math.log(1)}")




Math_LogarithmBase10_def = "Math Logarithm Base 10: The math.log10() method returns the base-10 logarithm of a number."
print(f"\n{Math_LogarithmBase10_def}")
print("    # Return the base-10 logarithm of different numbers")
print(f"        print(math.log10(2.7183)) = {math.log10(2.7183)}")
print(f"        print(math.log10(2)) = {math.log10(2)}")
print(f"        print(math.log10(1)) = {math.log10(1)}")




Math_Log1PlusNumber_def = "Math Log 1+Number: The math.log1p() method returns log(1+number), computed in a way that is accurate even when the value of number is close to zero."
print(f"\n{Math_Log1PlusNumber_def}")
print("    # Return the log(1+number) for different numbers")
print(f"        print(math.log1p(2.7183)) = {math.log1p(2.7183)}")
print(f"        print(math.log1p(2)) = {math.log1p(2)}")
print(f"        print(math.log1p(1)) = {math.log1p(1)}")




Math_LogarithmBase2_Def = "Math Logarithm Base 2: The math.log2() method returns the base-2 logarithm of a number."
print(f"\n{Math_LogarithmBase2_Def}")
print("    # Return the base-2 logarithm of different numbers")
print(f"        print(math.log2(2.7183)) = {math.log2(2.7183)}")
print(f"        print(math.log2(2)) = {math.log2(2)}")
print(f"        print(math.log2(1)) = {math.log2(1)}")




Math_Perm_def = "Math Perm: The math.perm() method returns the number of ways to choose k items from n items with order and without repetition. Note: The k parameter is optional. If we do not provide one, this method will return n! (for example, math.perm(7) will return 5040)."


print(f"\n{Math_Perm_def}")
print("    # Initialize the number of items to choose from")
print("    Math_Perm_n = 7")
Math_Perm_n = 7
print("    # Initialize the number of items to choose")
print("    Math_Perm_k = 5")
Math_Perm_k = 5
print("    # Print the number of ways to choose k items from n items")
print(f"        print(math.perm(Math_Perm_n, Math_Perm_k)) = {math.perm(Math_Perm_n, Math_Perm_k)}")





Math_Power_def = "Math Power: The math.pow() method returns the value of x raised to power y. If x is negative and y is not an integer, it returns a ValueError. This method converts both arguments into a float. Tip: If we use math.pow(1.0,x) or math.pow(x,0.0), it will always returns 1.0."
print(f"\n{Math_Power_def}")
print("    #Return the value of 9 raised to the power of 3")
print(f"        print(math.pow(9, 3)) = {math.pow(9, 3)}")




Math_Product_def = "Math Product: The math.prod() method returns the product of the elements from the given iterable."
print(f"\n{Math_Product_def}")
print("    Math_Product_sequence = (2, 2, 2)")
Math_Product_sequence = (2, 2, 2)
print("    #Return the product of the elements")
print(f"        print(math.prod(Math_Product_sequence)) = {math.prod(Math_Product_sequence)}")





Math_Radian_convert_def = "Math Radian convert: The math.radians() method converts a degree value into radians. Tip: See also math.degrees() to convert an angle from radians to degrees."




print(f"\n{Math_Radian_convert_def}")
print("    BLANK")
print(f"        print(math.radians(180)) = {math.radians(180)}")
print(f"        print(math.radians(100.03)) = {math.radians(100.03)}")
print(f"        print(math.radians(-20)) = {math.radians(-20)}")




Math_Remainder_def = "Math Remainder: The math.remainder() method returns the remainder of x with respect to y."
print(f"\n{Math_Remainder_def}")
print("    # Return the remainder of x/y")
print(f"        print(math.remainder(9, 2)) = {math.remainder(9, 2)}")
print(f"        print(math.remainder(9, 3)) = {math.remainder(9, 3)}")
print(f"        print(math.remainder(18, 4)) = {math.remainder(18, 4)}")




Math_Sin_def = "Math Sin: The math.sin() method returns the sine of a number. Note: To find the sine of degrees, it must first be converted into radians with the math.radians() method (see example below)."
print(f"\n{Math_Sin_def}")
print("    # Return the sine of different numbers")
print(f"        print(math.sin(0.00)) = {math.sin(0.00)}")
print(f"        print(math.sin(-1.23)) = {math.sin(-1.23)}")
print(f"        print(math.sin(10)) = {math.sin(10)}")
print(f"        print(math.sin(math.pi)) = {math.sin(math.pi)}")
print(f"        print(math.sin(math.pi/2)) = {math.sin(math.pi/2)}")




Math_SinHyperbolic_def = "Math Sin Hyperbolic: "
print(f"\n{Math_SinHyperbolic_def}")
print("    # Return the hyperbolic sine of different values")
print(f"        print(math.sinh(0.00)) = {math.sinh(0.00)}")
print(f"        print(math.sinh(-23.45)) = {math.sinh(-23.45)}")
print(f"        print(math.sinh(23)) = {math.sinh(23)}")
print(f"        print(math.sinh(1.00)) = {math.sinh(1.00)}")
print(f"        print(math.sinh(math.pi)) = {math.sinh(math.pi)}")




Math_SquareRoot_def = "Math Square Root: The math.sqrt() method returns the square root of a number. Note: The number must be greater than or equal to 0."
print(f"\n{Math_SquareRoot_def}")
print("    # Return the square root of different numbers")
print(f"        print(math.sqrt(9)) = {math.sqrt(9)}")
print(f"        print(math.sqrt(25)) = {math.sqrt(25)}")
print(f"        print(math.sqrt(16)) = {math.sqrt(16)}")




Math_Tangent_def = "Math Tangent: The math.tan() method returns the tangent of a number."
print(f"\n{Math_Tangent_def}")
print("    # Return the tangent of different numbers")
print(f"        print(math.tan(90)) = {math.tan(90)}")
print(f"        print(math.tan(-90)) = {math.tan(-90)}")
print(f"        print(math.tan(45)) = {math.tan(45)}")
print(f"        print(math.tan(60)) = {math.tan(60)}")




Math_TangentHyperbolic_def = "Math Tangent Hyperbolic: The math.tanh() method returns the hyperbolic tangent of a number."
print(f"\n{Math_TangentHyperbolic_def}")
print("    # Return the hyperbolic tangent of different numbers")
print(f"        print(math.tanh(8)) = {math.tanh(8)}")
print(f"        print(math.tanh(1)) = {math.tanh(1)}")
print(f"        print(math.tanh(-6.2)) = {math.tanh(-6.2)}")





Math_Truncate_def = "Math Truncate: The math.trunc() method returns the truncated integer part of a number. Note: This method will NOT round the number up/down to the nearest integer, but simply remove the decimals."
print(f"\n{Math_Truncate_def}")
print("    # Return the truncated integer parts of different numbers")
print(f"        print(math.trunc(2.77)) = {math.trunc(2.77)}")
print(f"        print(math.trunc(8.32)) = {math.trunc(8.32)}")
print(f"        print(math.trunc(-99.29)) = {math.trunc(-99.29)}")




Math_Eular_def = "Math Eular: The math.e constant returns the Eular's number: 2.718281828459045."
print(f"\n{Math_Eular_def}")
print("    # Print the value of E")
print(f"        print(math.e) = {math.e}")




Math_Infinity_def = "Math Infinity: The math.inf constant returns a floating-point positive infinity. For negative infinity, use -math.inf. The inf constant is equivalent to float('inf')."
print(f"\n{Math_Infinity_def}")
print("    # Print the positive infinity")
print(f"        print(math.inf) = {math.inf}")
print("    # Print the negative infinity")
print(f"        print(-math.inf) = {-math.inf}")




Math_NotANumber_def = "Math Not A Number: The math.nan constant returns a floating-point nan (Not a Number) value. This value is not a legal number. The nan constant is equivalent to float('nan')."
print(f"\n{Math_NotANumber_def}")
print("    # Print the value of nan")
print(f"        print(math.nan) = {math.nan}")





Math_Pi_def = "Math Pi: The math.pi constant returns the value of PI: 3.141592653589793. Note: Mathematically PI is represented by π."
print(f"\n{Math_Pi_def}")
print("    # Print the value of pi")
print(f"        print(math.pi) = {math.pi}")




Math_Tau_def = "Math Tau: The math.tau constant returns the value of tau, which is 6.283185307179586. It is defined as the ratio of the circumference to the radius of a circle. Tau is a circle constant and the value is equivalent to 2π. Note: Mathematically tau is represented by τ."
print(f"\n{Math_Tau_def}")
print("    # Print the value of tau")
print(f"        print(math.tau) = {math.tau}")





print("\n\n\nEnd of the Python Math Methods Showcase")

