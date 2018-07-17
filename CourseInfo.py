""" 
This file contains the information about the various classes in the Tutor Center.
If you wish to add to this list, type in the new value in the proper location (i.e. majors, class prefixes, etc.),
making sure that your entry is in double quotes and seperated from the other options by a comma.
Also make sure that you enter your new item between the [ ].
Some sections have additional steps that must be followed when adding a new value. See the individual section below
for those steps.
"""


class CourseInfo:
    # This list of available majors.
    majoroptions = [
                    "BIEN",
                    "CIEN",
                    "CMPE",
                    "COSC",
                    "ELEN",
                    "ENVE",
                    "GENG",
                    "MEEN/AERO",
                    "OTHER"
                    ]

    # This is a list of the class ranks.
    rankoptions = [
                   "Freshman",
                   "Sophmore",
                   "Junior",
                   "Senior",
                   "Graduate Student"
                   ]

    # This is a list of course prefixes.
    # THIS SECTION HAS ADDITIONAL STEPS WHEN ADDING A NEW ITEM!
    # When adding a new item to this list, you need to add another else statement to the populate_names method, below.
    # See that section for how to do that.
    prefixoptions = [
                     "BENG",
                     "BIOL",
                     "CEE",
                     "CHEM",
                     "CS",
                     "ECE",
                     "ENGR",
                     "GEOL",
                     "MAE",
                     "MATH",
                     "MGT",
                     "PHYS",
                     "PSC",
                     "STAT"
                     ]

    # This populates the prefix menu based on the prefix selection.
    # ADDING A NEW ITEM:
    # Copy the following two lines into the list, above the "else" line: (delete the # in the new lines after copying)
        #elif prefix_selection == "NewPrefixHere":
            #prefix = CourseInfo.PREoptions
    # Change the "NewPrefixHere" and "PREoptions" to match the new prefix that you added above and below.
    @staticmethod
    def populate_names(prefix_selection):
        if prefix_selection == "ENGR":
            prefix = CourseInfo.ENGRoptions
        elif prefix_selection == "MAE":
            prefix = CourseInfo.MAEoptions
        elif prefix_selection == "CHEM":
            prefix = CourseInfo.CHEMoptions
        elif prefix_selection == "MATH":
            prefix = CourseInfo.MATHoptions
        elif prefix_selection == "PHYS":
            prefix = CourseInfo.PHYSoptions
        elif prefix_selection == "CS":
            prefix = CourseInfo.CSoptions
        elif prefix_selection == "BENG":
            prefix = CourseInfo.BENGoptions
        elif prefix_selection == "BIOL":
            prefix = CourseInfo.BIOLoptions
        elif prefix_selection == "STAT":
            prefix = CourseInfo.STAToptions
        elif prefix_selection == "CEE":
            prefix = CourseInfo.CEEoptions
        elif prefix_selection == "GEOL":
            prefix = CourseInfo.GEOLoptions
        elif prefix_selection == "ECE":
            prefix = CourseInfo.ECEoptions
        elif prefix_selection == "PSC":
            prefix = CourseInfo.PSCoptions
        elif prefix_selection == "MGT":
            prefix = CourseInfo.MGToptions
        else: # This should only be reachable if the course prefixes are updated without changing this function.
            prefix = CourseInfo.ENGRoptions # defaults the prefix to ENGR
            print("You need to update the populate_names function!") # Prints out a message warning about the problem.
        return prefix

    # This contains all of the ENGR-prefixed courses.
    ENGRoptions = [
                   "ENGR 2010: Statics",
                   "ENGR 2210: Fundamental Electronics",
                   "ENGR 2030: Dynamics",
                   "ENGR 2140: Mechanics of Materials",
                   "ENGR 2270: Computer Engr. Drafting",
                   "ENGR 2450: Numerical Methods",
                   "ENGR 3080: Technical Communication"
                   ]
    ENGRoptions = sorted(ENGRoptions) # Sorts by course number.
    
    # This contains all of the MAE-prefixed courses.
    MAEoptions = [
                  "MAE 1010: Intro to Mechanical Engineering",
                  "MAE 1200: Engineering Graphics",
                  "MAE 2160: Material Science",
                  "MAE 2300: Thermodynamics 1",
                  "MAE 3210: Numerical Methods",
                  "MAE 3340: Instrumentation and Measurements",
                  "MAE 3600: Engr. Professionalism and Ethics",
                  "MAE 3040: Mechanics of Solids",
                  "MAE 3320: Advanced Dynamics",
                  "MAE 5300: Vibrations",
                  "MAE 3440: Heat Transfer",
                  "MAE 4300: Machine Design",
                  "MAE 3420: Fluid Dynamics",
                  "MAE 4400: Fluids/Thermal Lab",
                  "MAE 4800: Capstone Design 1",
                  "MAE 4810: Capstone Design 2",
                  "MAE 5020: Finite Element Methods 1",
                  "MAE 5040: Experimental Solid Mechanics",
                  "MAE 5060: Mechanics of Composite Materials 1",
                  "MAE 5310: Dynamics Systems and Controls",
                  "MAE 5320: Mechatronics",
                  "MAE 5350: Kinematics",
                  "MAE 5410: Design and Optimization of Thermal Systems",
                  "MAE 5420: Compressible Fluid Flow",
                  "MAE 5440: Computational Fluid Dynamics",
                  "MAE 5450: Renewable Energy",
                  "MAE 5500: Aerodynamics",
                  "MAE 5510: Dynamics of Atmospheric Flight",
                  "MAE 5530: Space System Design",
                  "MAE 5540: Propulsion Systems",
                  "MAE 5560: Dynamics of Space Flight",
                  "MAE 5580: Aircraft Design",
                  "MAE 5670: Fracture Mechanics"
                  ]
    MAEoptions = sorted(MAEoptions) # Sorts by course number.

    # This contains all of the CHEM-prefixed courses.
    CHEMoptions = [
                   "CHEM 1210: Principles of Chemistry 1",
                   "CHEM 2300: Organic Chemistry 1",
                   "CHEM 3700: Introductory Biochemistry",
                   "CHEM 1220: Principles of Chemistry 2",
                   "CHEM 2320: Organic Chemistry 2",
                   "CHEM 3070: Physical Chemistry",
                   "CHEM 3650: Environmental Chemistry"
                   ]
    CHEMoptions = sorted(CHEMoptions) # Sorts by course number.

    # This contains all of the MATH-prefixed courses.
    MATHoptions = [
                   "MATH 1050: College Algebra",
                   "MATH 1060: Trigonometry",
                   "MATH 1210: Calculus 1",
                   "MATH 1220: Calculus 2",
                   "MATH 2210: Multivariable Calculus",
                   "MATH 2250: Linear Algebra and Differential Equations",
                   "MATH 3310: Discrete Mathematics",
                   "MATH 2270: Linear Algebra",
                   "MATH 2280: Differential Equations"
                   ]
    MATHoptions = sorted(MATHoptions) # Sorts by course number.

    # This contains all of the PHYS-prefixed courses.
    PHYSoptions = [
        "PHYS 2210: Physics 1",
        "PHYS 2220: Physics 2",
        "PHYS 2710: Introductory Modern Physics"
    ]
    PHYSoptions = sorted(PHYSoptions) # Sorts by course number.

    # This contains all of the CS-prefixed courses.
    CSoptions = [
        "CS 1400: Computer Science 1",
        "CS 1410: Computer Science 2",
        "CS 2420: Computer Science 3",
        "CS 3100: Operating Systems",
        "CS 1440: Methods in Comp. Sci.",
        "CS 2420: Algorithms & Data Structures",
        "CS 2410: Intro to Event Prog. & GUIs",
        "CS 2610: Developing Web App",
        "CS 2810: Comp. Sys. Organization",
        "CS 3450: Intro to Software Engineering",
        "CS 4700: Programming Languages"
    ]
    CSoptions = sorted(CSoptions) # Sorts by course number.

    # This contains all of the BENG-prefixed courses.
    BENGoptions = [
        "BENG 1000: Intro to Undergraduate Research",
        "BENG 1880: Quantitative Biological Systems",
        "BENG 2300: Properties of Biomaterials",
        "BENG 2400: Thermodynamics",
        "BENG 3200: Intro to Unit Operations",
        "BENG 3500: Fluid Mechanics",
        "BENG 3870: Biol. Engr. Design 1",
        "BENG 3000: Instrumentation for Biol. Sys.",
        "BENG 3670: Transport Phenomena",
        "BENG 4880: Biol. Engr. Design 2",
        "BENG 4890: Biol. Engr. Design 3",
        "BENG 4250: Cooperative Practice"
    ]
    BENGoptions = sorted(BENGoptions) # Sorts by course number.

    # This contains all of the BIOL-prefixed courses.
    BIOLoptions = [
        "BIOL 1610: Biology 1",
        "BIOL 3300: General Microbiology",
        "BIOL 3060: Principles of Genetics",
        "BIOL 1620: Biology 2",
        "BIOL 2320: Human Anatomy",
        "BIOL 2420: Human Physiology",
        "BIOL 3060: Principles of Genetics"
        "BIOL 3100: Bioethics"
    ]
    BIOLoptions = sorted(BIOLoptions) # Sorts by course number.

    # This contains all of the STAT-prefixed courses.
    STAToptions = [
        "STAT 3000: Statistics for Scientists",
        "STAT 5200: Design of Experiments"
    ]
    STAToptions = sorted(STAToptions) # Sorts by course number.

    # This contains all of the CEE-prefixed courses.
    CEEoptions = [
        "CEE 1880: CEE Orientation",
        "CEE 2240: Engineering Surveying",
        "CEE 3160: Civil Engineering Materials",
        "CEE 3500: Fluid Mechanics",
        "CEE 3610: Environmental Management",
        "CEE 4200: Engineering Economics",
        "CEE 3020: Structural Analysis"
        "CEE 3510: Engineering Hydraulics",
        "CEE 3880: Civil and Env. Engr. Design 1",
        "CEE 4870: Civil and Env. Engr. Design 2",
        "CEE 4880: Civil and Env. Engr. Design 3",
        "CEE 3020: Structural Analysis",
        "CEE 5060: Mechanics of Composite Materials 1",
        "CEE 2620: Microbiology",
        "CEE 3780: Hazardous Waste Management",
        "CEE 3420: Engineering Hydrology",
        "CEE 3640: Drinking Water Engineering",
        "CEE 3650: Wastewater Engineering",
        "CEE 3670: Transport Phenomena in Bio-Environmental Systems"
    ]
    CEEoptions = sorted(CEEoptions) # Sorts by course number.

    # This contains all of the GEOL-prefixed courses.
    GEOLoptions = [
        "GEOL 1110: Physical Geology"
    ]
    GEOLoptions = sorted(GEOLoptions) # Sorts by course number.

    # This contains all of the ECE-prefixed courses.
    ECEoptions = [
        "ECE 2700: Digital Circuits",
        "ECE 2250: Electrical Circuits 1",
        "ECE 2290: Electrical Circuits 2",
        "ECE 3620: Continuous Time Systems",
        "ECE 3710: Microcontrollers",
        "ECE 3410: Microelectronics 1"
        "ECE 3810: Engineering Professionalism",
        "ECE 4820: Computer Engr. Design 1",
        "ECE 4830: Engineering Comm. 1",
        "ECE 4840: Computer Engr. Design 2",
        "ECE 4700: Engineering Comm. 2",
        "ECE 3620: Continuous-Time Sys. & Sig.",
        "ECE 3640: Discrete-Time Sys. & Sig.",
        "ECE 3870: Electromagnetics 1"
    ]
    ECEoptions = sorted(ECEoptions) # Sorts by course number.

    # This contains all of the PSC-prefixed courses.
    PSCoptions = [
        "PSC 3000: Fundamentals of Soil Science"
    ]
    PSCoptions = sorted(PSCoptions) # Sorts by course number.

    # This contains all of the MGT-prefixed courses.
    MGToptions = [
        "MGT 3110: Managing Organizations"
    ]
    MGToptions = sorted(MGToptions) # Sorts by course number.
