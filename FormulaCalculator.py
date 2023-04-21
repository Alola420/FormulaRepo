import math
while True:
    #choosing the subject
    p = str(input("Choose your subject: 1)Math  2)Chemistry  3)Physics  4)Exit ")) 
    if p == "1":
        #Math formulae
        q = str(input("Choose your topic: 1)Circles  2)Straight Lines  3)Trigonometry  4)Permutation and Combination  5)Quadratic "))
        if q == "1":
            #choosing the problem within the selected topic
            r = str(input("Choose the formula 1)Finding equation of circle  2)Finding center and radius of circle "))
            if r == "1":
                # finding equation of a circle
                g = float(input("X co-ordinate of circle's centre"))
                f = float(input("Y co-ordinate of circle's centre"))
                rad = float(input("Enter radius of the circle"))
                c = (g**2 + f**2 - rad**2)
                print ('The equation of the circle is x^2 + y^2 + '+ str(-2*g) + 'x + ' + str(-2*f) + 'y + ' + str(c) + ' = 0')
            elif r == "2":
                # Finding center and radius of a circle given its equation
                print ("Let the equation of a circle be x^2 + y^2 + 2gx + 2fy + c = 0")
                g = float(input("Enter g "))
                f = float(input("Enter f "))
                c = float(input("enter c "))
                print ("The center is " + str(-g) + "-" + str(-f))
                print ("The radius is " + str((g**2 + f**2 - c)**0.5))
            else:
                #scouting for invalid input
                print ("Invalid option")
        elif q == "2":
            r = str(input("Choose the formula 1)Equation of a straight line  2)Distance of a point from a line "))
            if r == "1":
                # equation of line given 2 pts.
                x1 = float(input("X co-ordinate of first pt."))
                y1 = float(input("Y co-ordinate of first pt."))
                x2 = float(input("X co-ordinate of second pt."))
                y2 = float(input("Y co-ordinate of second pt."))
                print ("The pts. are " + str(x1) + "," + str(y1) + " and " + str(x2) + "," + str(y2))
                m = (y2 - y1)/(x2 - x1)
                c = -m*x1 + y1
                print ("The line connecting the above 2 pts. is y = " + str(m) + "x + " + str(c))

            if r == "2":
                # distance of a pt from a line
                x = float(input("X co-ordinate of pt."))
                y = float(input("Y co-ordinate of pt."))
                print ("Let the line be of for ax + by + c = 0")
                a = float(input("Enter a "))
                b = float(input("Enter b "))
                c = float(input("Enter c "))
                d = abs(a*x + b*y + c)/(a**2 + b**2)**0.5
                print ("The distance of the pt " + str(x) + " , " + str(y) + " from the line " + str(a) + "x + " + str(b) + "y + " + str(c) + " = 0 is " + str(d))

            else:
                print ("Invalid option")
        elif q == "3":
            r = str(input("Choose the formula 1)Degrees to radians  2)List of trig ratios "))
            if r == "1":
                # degrees to radians                
                d = float(input("Enter an angle in degrees "))
                print (str(d) + " degrees is equal to " + str(d/180) + "pi radians")
                print (str(d) + " degrees is equal to " + str(d * math.pi /180) + " radians")

            elif r == "2":                
                d = float(input("Enter an angle in degrees "))
                r = math.radians(d)
                print ("sin " + str(d) + " = " + str(math.sin(r)))
                print ("cos " + str(d) + " = " + str(math.cos(r)))
                print ("tan " + str(d) + " = " + str(math.tan(r)))
                print ("cot " + str(d) + " = " + str(1/math.tan(r)))
                print ("sec " + str(d) + " = " + str(1/math.cos(r)))
                print ("cosec " + str(d) + " = " + str(1/math.sin(r)))
            else:
                print ("Invalid option")
        elif q == "4":
            r = str(input("Choose the formula 1)n!  2)nCr "))
            if r == "1":
                # factorial of a number
                n = int(input("enter n for n!"))
                x = 1
                for a in range (1, n):
                   x = x*(a+1)
                print (x)
            if r == "2":
                # calculating ncr
                n = int(input("Enter total no. of objects "))
                r = int(input("Enter no. of ojects to be picked"))
                x = 1
                for a in range (1, n):
                    x = x*(a+1)
                y = 1
                for b in range (1, r):
                    y = y*(b+1)
                z = 1
                for c in range (1, n-r):
                    z = z*(c+1)
                ncr = x/(y * z)
                print ("There are " + str(ncr) + " ways of picking " + str(r) + " objects out of " + str(n) + " objects")
            else:
                print ("Invalid option")
        elif q == "5":
            r = str(input("Choose the formula 1)Solving a quadratic  2)Sum and product of roots "))
            if r == "1":
                # Quadratic
                a = float(input("Enter a for ax^2+bx+c=0 : "))
                b = float(input("Enter b for ax^2+bx+c=0 : "))
                c = float(input("Enter c for ax^2+bx+c=0 : "))
                d1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
                d2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
                print ("The first root is " + str(d1))
                print ("The second root is " + str(d2))
            elif r == "2":
                # sum and product of roots
                a = float(input("Enter a for ax^2+bx+c=0 : "))
                b = float(input("Enter b for ax^2+bx+c=0 : "))
                c = float(input("Enter c for ax^2+bx+c=0 : "))
                print ("Sum of roots is " + str(-b/a))
                print ("Product of roots is " + str(c/a))
            else:
                print ("Invalid option")
        else:
            print ("invalid option")
    elif p == "2":
        #Chemistry Formulae
        q = str(input("Choose your topic: 1)Atomic Structure  2)Gaseous State  3)Stoichiometry"))
        if q == "1":
            r = str(input("Choose the formula 1)Bohr's Orbit Radius  2)Bohr's orbit Energy  3)Bohr's Orbit Velocity  4)Quantized Angular Momentum"))
            if r == "1":
                # Bohr's Radius
                protons = int(input("enter number of protons in the element: " ))
                orbit = int(input("enter the orbit's radius you want calculate(n): "))
                radius = (0.529*(orbit**2))/protons
                print("the radius of the orbit is : " + str(radius) + " armstrong")
            elif r == "2":
                # Bohr's Energy
                protons = int(input("enter number of protons in the element: " ))
                orbit = int(input("enter the orbit's you want calculate(n): "))
                energy = (-13.6)*((protons**2)/(orbit**2))
                print("the energy of the orbit is : " + str(energy) + " eV")
            elif r == "3":
                # Bohr's Velocity
                protons = int(input("enter number of protons in the element: " ))
                orbit = int(input("enter the orbit's you want calculate(n): "))
                velocity = ((2.18*(10**6))*(protons))/(orbit)
                print("the velocity of the orbit is : " + str(velocity) + " m/s")
            elif r == "4":
                # Quantized Angular Momentum
                h = 6.62607004 * (10**(-34))
                orbit = int(input("enter the orbit's you want calculate(n): "))
                angular_momentum = orbit*(h/(2*math.pi))
                print("the angular momentum of the orbit is : ",angular_momentum,"kgm/s")
            else:
                print ("invalid option")
        elif q == "2":
            r = str(input("Choose the formula 1)Pressure of Ideal Gas  2)Temperature of Ideal Gas  3) Volume of Ideal Gas  4) Moles of Ideal Gas"))
            if r == "1":
                # Pressure
                n = float(input("enter the number of moles of ideal gas present(n): "))
                R = 0.0821
                t = float(input("enter temperature in degrees(celcius): "))
                T = t + 273
                V = float(input("enter the volume of the container(liters): "))
                P = (n*R*T)/V
                print("the pressure in the container is: " + str(P) + " atm")
            elif r == "2":
                # Temperature
                n = float(input("enter the number of moles of ideal gas present(n): "))
                R = 0.0821
                P = float(input("enter pressure in atm: "))
                V = float(input("enter the volume of the container(liters): "))
                t = (P*V)/(n*R)
                T = t-273
                print("the temperature in the container is: " + str(T) + " degrees")
            elif r == "3":
                # Volume
                n = float(input("enter the number of moles of ideal gas present(n): "))
                R = 0.0821
                P = float(input("enter pressure in atm: "))
                t = float(input("enter the temperature of the container(degrees): "))
                T = t + 273
                V = (n*R*T)/P
                print("the volume in the container is: " + str(V) + "liters")
            elif r == "4":
                # Moles
                V = float(input("enter the volume of the container(liters): "))
                R = 0.0821
                P = float(input("enter pressure in atm: "))
                t = float(input("enter the temperature of the container(degrees): "))
                T = t + 273
                n = (P*V)/(R*T)
                print("the moles of ideal gas in container is: " + str(n) + " moles")
            else:
                print ("invalid option")
        elif q == "3":
            r = str(input("Choose the formula 1) Molarity  2) %weight/weight"))
            if r == "1":
                # Molarity
                n = float(input("enter number of mole dissolved of the solute: "))
                v = float(input("enter the volume of solution in liters: "))
                M = n/v
                print("the molarity of the solution is: " + str(M) + " M")
            elif r == "2":
                # % weight by weight
                solute = float(input("mass of solute dissolved(g): "))
                v = float(input("volume of solution(ml): "))
                d = float(input("density of solution in (g/ml): "))
                solution = v*d
                wbyw = solute/solution
                print("the %(w/w) of the solute and solution is: " + str(wbyw) + "%")
            else:
                print ("invalid option")
        else:
            print ("invalid option")                            
    elif p == "3":
        #physics formulae
        q = str(input("Choose your topic: 1)Gravitation  2)Energy  3)Work power  4)Projectile"))
        if q == "1":
            r = str(input("Choose the formula 1)Black Hole Radius  2)Escape Velocity"))
            if r == "1":
                # Black Hole radius
                mass_b = float(input("Mass of the body(kgs): "))
                s_radius = (2 *(6.674 * 10**(-11)) * mass_b / (9*(10**16)))
                print("the radius required to convert it into a black hole in (nm): " + str(s_radius))
            elif r == "2":
                # Escape velocity
                print("give realistic mass and radius values.")
                radius = float( input(("enter radius (in meters): ")))
                mass = float(input(("enter mass (in kgs): ")))
                g_acc = float(((6.67408 * 10**(-11))*mass)/radius**2)
                e_vel = math.sqrt(2*g_acc*radius)
                print("the escape velocity of your planet is(m/s): " + str(e_vel))
            else:
                print ("invalid option")
        elif q == "2":
            r = str(input("Choose the formula 1)Potential Energy  2)Kinetic Energy"))
            if r == "1":
                # Potential Energy
                mass = float(input("enter mass of the object(in kgs): "))
                height = float(input("enter the height at which it is placed (in meters): "))
                p_energy = 10*mass*height
                print("the potential energy of the object is: " + str(p_energy) + "joules")
            elif r == "2":
                # Kinetic Energy
                mass = float(input("enter the mass of the object(in kgs):" ))
                velocity = float(input("enter velocity (in m/s): "))
                k_energy = 0.5*mass*(velocity**2)
                print (mass)
                print (velocity)
                print("the kinetic energy of the object is: " + str(k_energy) + "joules" )
            else:
                print ("invalid option")
        elif q == "3":
            r = str(input("Choose the formula 1)Work  2)Power"))
            if r == "1":
                # Work
                acc = float(input("enter the acceleration(in m/s^2):" ))
                mass = float(input("enter the mass of the object: "))
                force = mass*acc
                disp = float(input("enter displacment of the object(meters): "))
                work = force*disp
                print("the work done by the object is: " + str(work) + "joules")
            elif r == "2":
                # Power
                acc = float(input("enter the acceleration(in m/s^2):" ))
                mass = float(input("enter the mass of the object: "))
                force = mass*acc
                disp = float(input("enter displacment of the object(meters): "))
                work = force*disp
                time = float(input("enter time taken to do the work(in seconds): "))
                power = work/time
                print("the power of the object is: " + str(power) + "joules/second")
            else:
                print ("invalid option")
        elif q == "4":
            r = str(input("Choose the formula 1)Time  2)Displacement  3)Height  4)Range"))
            if r == "1":
                # Time
                i_vel = float(input("enter intial velocity of projection(m/s): " ))
                g = 10
                angl_proj = float(input("enter angle of projection(in degrees): "))
                rad = angl_proj*(math.pi/180)
                sine = math.sin(rad)
                time = (2*i_vel*sine)/g
                print("the time of projection is : " + str(time) + "seconds")
            elif r == "2":
                # Displacement
                i_vel = float(input("enter intial velocity of projection(m/s): "))
                g = 10
                angl_proj = float(input("enter angle of projection(in degrees): "))
                rad = angl_proj*(math.pi/180)
                sine = math.sin(rad)
                time = (2*i_vel*sine)/g
                print("the time of projection is : " + str(time) + "seconds")
                time_2 = float(input("the time at witch you wanna know displacement(seconds): "))
                cosine = math.cos(rad)
                x = i_vel *time_2*cosine
                y = (i_vel*time_2*sine)-(0.5*g*(time_2**2))
                print("displacement in the x axis (meters): " + str(x) + "m")
                print("displacement in the y axis (meters): " + str(y) + "m")
            elif r == "3":
                # Height
                i_vel = float(input("enter intial velocity of projection(m/s): " ))
                g = 10
                angl_proj = float(input("enter angle of projection(in degrees): "))
                rad = angl_proj*(math.pi/180)
                sine = math.sin(rad)
                max_h = ((i_vel**2)*(sine**2))/(2*g)
                print("the maximum height of projection is : " + str(max_h) + "meters")
            elif r == "4":
                # Range
                i_vel = float(input("enter intial velocity of projection(m/s): " ))
                g = 10
                angl_proj = float(input("enter angle of projection(in degrees): "))
                rad = angl_proj*(math.pi/180)
                sine = math.sin(2*rad)
                Range = ((i_vel**2)*(sine))/g
                print("the maximum range of projection is : " + str(Range) + "meters")
            else:
                print ("invalid option")
        else:
                print ("invalid option")
    elif p == "4":
        print ("Exiting Program")
        break
    else: 
        print ("Invalid option")
