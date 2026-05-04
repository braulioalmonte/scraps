import flet as ft
import random
#TODO 1: Make a view that only includes the periodic table, using a grid and making the elements clickable to see their information with a dialog window
#TODO 2: Make the following gamemodes: Atomic Number -> Symbol, Symbol -> Name, Atomic Mass -> Symbol
#TODO 3: Normal mode: Write answer manually, Easy mode: Multiple Choice answer
#TODO 4: Pehaps make an "ElementCard" custom class and generate it programmatically using the periodicTable variable to then fill the grid in TODO 1

def main(page: ft.Page):
    #Variables
    periodicTable = {
    1: {"atomic_number": 1, "name": "Hydrogen", "symbol": "H", "atomic_mass": 1.008},
    2: {"atomic_number": 2, "name": "Helium", "symbol": "He", "atomic_mass": 4.0026},
    3: {"atomic_number": 3, "name": "Lithium", "symbol": "Li", "atomic_mass": 6.94},
    4: {"atomic_number": 4, "name": "Beryllium", "symbol": "Be", "atomic_mass": 9.0122},
    5: {"atomic_number": 5, "name": "Boron", "symbol": "B", "atomic_mass": 10.81},
    6: {"atomic_number": 6, "name": "Carbon", "symbol": "C", "atomic_mass": 12.011},
    7: {"atomic_number": 7, "name": "Nitrogen", "symbol": "N", "atomic_mass": 14.007},
    8: {"atomic_number": 8, "name": "Oxygen", "symbol": "O", "atomic_mass": 15.999},
    9: {"atomic_number": 9, "name": "Fluorine", "symbol": "F", "atomic_mass": 18.998},
    10: {"atomic_number": 10, "name": "Neon", "symbol": "Ne", "atomic_mass": 20.180},

    11: {"atomic_number": 11, "name": "Sodium", "symbol": "Na", "atomic_mass": 22.990},
    12: {"atomic_number": 12, "name": "Magnesium", "symbol": "Mg", "atomic_mass": 24.305},
    13: {"atomic_number": 13, "name": "Aluminum", "symbol": "Al", "atomic_mass": 26.982},
    14: {"atomic_number": 14, "name": "Silicon", "symbol": "Si", "atomic_mass": 28.085},
    15: {"atomic_number": 15, "name": "Phosphorus", "symbol": "P", "atomic_mass": 30.974},
    16: {"atomic_number": 16, "name": "Sulfur", "symbol": "S", "atomic_mass": 32.06},
    17: {"atomic_number": 17, "name": "Chlorine", "symbol": "Cl", "atomic_mass": 35.45},
    18: {"atomic_number": 18, "name": "Argon", "symbol": "Ar", "atomic_mass": 39.948},
    19: {"atomic_number": 19, "name": "Potassium", "symbol": "K", "atomic_mass": 39.098},
    20: {"atomic_number": 20, "name": "Calcium", "symbol": "Ca", "atomic_mass": 40.078},

    21: {"atomic_number": 21, "name": "Scandium", "symbol": "Sc", "atomic_mass": 44.956},
    22: {"atomic_number": 22, "name": "Titanium", "symbol": "Ti", "atomic_mass": 47.867},
    23: {"atomic_number": 23, "name": "Vanadium", "symbol": "V", "atomic_mass": 50.942},
    24: {"atomic_number": 24, "name": "Chromium", "symbol": "Cr", "atomic_mass": 51.996},
    25: {"atomic_number": 25, "name": "Manganese", "symbol": "Mn", "atomic_mass": 54.938},
    26: {"atomic_number": 26, "name": "Iron", "symbol": "Fe", "atomic_mass": 55.845},
    27: {"atomic_number": 27, "name": "Cobalt", "symbol": "Co", "atomic_mass": 58.933},
    28: {"atomic_number": 28, "name": "Nickel", "symbol": "Ni", "atomic_mass": 58.693},
    29: {"atomic_number": 29, "name": "Copper", "symbol": "Cu", "atomic_mass": 63.546},
    30: {"atomic_number": 30, "name": "Zinc", "symbol": "Zn", "atomic_mass": 65.38},

    31: {"atomic_number": 31, "name": "Gallium", "symbol": "Ga", "atomic_mass": 69.723},
    32: {"atomic_number": 32, "name": "Germanium", "symbol": "Ge", "atomic_mass": 72.630},
    33: {"atomic_number": 33, "name": "Arsenic", "symbol": "As", "atomic_mass": 74.922},
    34: {"atomic_number": 34, "name": "Selenium", "symbol": "Se", "atomic_mass": 78.971},
    35: {"atomic_number": 35, "name": "Bromine", "symbol": "Br", "atomic_mass": 79.904},
    36: {"atomic_number": 36, "name": "Krypton", "symbol": "Kr", "atomic_mass": 83.798},

    37: {"atomic_number": 37, "name": "Rubidium", "symbol": "Rb", "atomic_mass": 85.468},
    38: {"atomic_number": 38, "name": "Strontium", "symbol": "Sr", "atomic_mass": 87.62},
    39: {"atomic_number": 39, "name": "Yttrium", "symbol": "Y", "atomic_mass": 88.906},
    40: {"atomic_number": 40, "name": "Zirconium", "symbol": "Zr", "atomic_mass": 91.224},
    41: {"atomic_number": 41, "name": "Niobium", "symbol": "Nb", "atomic_mass": 92.906},
    42: {"atomic_number": 42, "name": "Molybdenum", "symbol": "Mo", "atomic_mass": 95.95},
    43: {"atomic_number": 43, "name": "Technetium", "symbol": "Tc", "atomic_mass": 98},
    44: {"atomic_number": 44, "name": "Ruthenium", "symbol": "Ru", "atomic_mass": 101.07},
    45: {"atomic_number": 45, "name": "Rhodium", "symbol": "Rh", "atomic_mass": 102.91},
    46: {"atomic_number": 46, "name": "Palladium", "symbol": "Pd", "atomic_mass": 106.42},
    47: {"atomic_number": 47, "name": "Silver", "symbol": "Ag", "atomic_mass": 107.87},
    48: {"atomic_number": 48, "name": "Cadmium", "symbol": "Cd", "atomic_mass": 112.41},

    49: {"atomic_number": 49, "name": "Indium", "symbol": "In", "atomic_mass": 114.82},
    50: {"atomic_number": 50, "name": "Tin", "symbol": "Sn", "atomic_mass": 118.71},
    51: {"atomic_number": 51, "name": "Antimony", "symbol": "Sb", "atomic_mass": 121.76},
    52: {"atomic_number": 52, "name": "Tellurium", "symbol": "Te", "atomic_mass": 127.60},
    53: {"atomic_number": 53, "name": "Iodine", "symbol": "I", "atomic_mass": 126.90},
    54: {"atomic_number": 54, "name": "Xenon", "symbol": "Xe", "atomic_mass": 131.29},

    55: {"atomic_number": 55, "name": "Cesium", "symbol": "Cs", "atomic_mass": 132.91},
    56: {"atomic_number": 56, "name": "Barium", "symbol": "Ba", "atomic_mass": 137.33},

    57: {"atomic_number": 57, "name": "Lanthanum", "symbol": "La", "atomic_mass": 138.91},
    58: {"atomic_number": 58, "name": "Cerium", "symbol": "Ce", "atomic_mass": 140.12},
    59: {"atomic_number": 59, "name": "Praseodymium", "symbol": "Pr", "atomic_mass": 140.91},
    60: {"atomic_number": 60, "name": "Neodymium", "symbol": "Nd", "atomic_mass": 144.24},
    61: {"atomic_number": 61, "name": "Promethium", "symbol": "Pm", "atomic_mass": 145},
    62: {"atomic_number": 62, "name": "Samarium", "symbol": "Sm", "atomic_mass": 150.36},
    63: {"atomic_number": 63, "name": "Europium", "symbol": "Eu", "atomic_mass": 151.96},
    64: {"atomic_number": 64, "name": "Gadolinium", "symbol": "Gd", "atomic_mass": 157.25},
    65: {"atomic_number": 65, "name": "Terbium", "symbol": "Tb", "atomic_mass": 158.93},
    66: {"atomic_number": 66, "name": "Dysprosium", "symbol": "Dy", "atomic_mass": 162.50},
    67: {"atomic_number": 67, "name": "Holmium", "symbol": "Ho", "atomic_mass": 164.93},
    68: {"atomic_number": 68, "name": "Erbium", "symbol": "Er", "atomic_mass": 167.26},
    69: {"atomic_number": 69, "name": "Thulium", "symbol": "Tm", "atomic_mass": 168.93},
    70: {"atomic_number": 70, "name": "Ytterbium", "symbol": "Yb", "atomic_mass": 173.05},
    71: {"atomic_number": 71, "name": "Lutetium", "symbol": "Lu", "atomic_mass": 174.97},

    72: {"atomic_number": 72, "name": "Hafnium", "symbol": "Hf", "atomic_mass": 178.49},
    73: {"atomic_number": 73, "name": "Tantalum", "symbol": "Ta", "atomic_mass": 180.95},
    74: {"atomic_number": 74, "name": "Tungsten", "symbol": "W", "atomic_mass": 183.84},
    75: {"atomic_number": 75, "name": "Rhenium", "symbol": "Re", "atomic_mass": 186.21},
    76: {"atomic_number": 76, "name": "Osmium", "symbol": "Os", "atomic_mass": 190.23},
    77: {"atomic_number": 77, "name": "Iridium", "symbol": "Ir", "atomic_mass": 192.22},
    78: {"atomic_number": 78, "name": "Platinum", "symbol": "Pt", "atomic_mass": 195.08},
    79: {"atomic_number": 79, "name": "Gold", "symbol": "Au", "atomic_mass": 196.97},
    80: {"atomic_number": 80, "name": "Mercury", "symbol": "Hg", "atomic_mass": 200.59},

    81: {"atomic_number": 81, "name": "Thallium", "symbol": "Tl", "atomic_mass": 204.38},
    82: {"atomic_number": 82, "name": "Lead", "symbol": "Pb", "atomic_mass": 207.2},
    83: {"atomic_number": 83, "name": "Bismuth", "symbol": "Bi", "atomic_mass": 208.98},
    84: {"atomic_number": 84, "name": "Polonium", "symbol": "Po", "atomic_mass": 209},
    85: {"atomic_number": 85, "name": "Astatine", "symbol": "At", "atomic_mass": 210},
    86: {"atomic_number": 86, "name": "Radon", "symbol": "Rn", "atomic_mass": 222},

    87: {"atomic_number": 87, "name": "Francium", "symbol": "Fr", "atomic_mass": 223},
    88: {"atomic_number": 88, "name": "Radium", "symbol": "Ra", "atomic_mass": 226},

    89: {"atomic_number": 89, "name": "Actinium", "symbol": "Ac", "atomic_mass": 227},
    90: {"atomic_number": 90, "name": "Thorium", "symbol": "Th", "atomic_mass": 232.04},
    91: {"atomic_number": 91, "name": "Protactinium", "symbol": "Pa", "atomic_mass": 231.04},
    92: {"atomic_number": 92, "name": "Uranium", "symbol": "U", "atomic_mass": 238.03},
    93: {"atomic_number": 93, "name": "Neptunium", "symbol": "Np", "atomic_mass": 237},
    94: {"atomic_number": 94, "name": "Plutonium", "symbol": "Pu", "atomic_mass": 244},
    95: {"atomic_number": 95, "name": "Americium", "symbol": "Am", "atomic_mass": 243},
    96: {"atomic_number": 96, "name": "Curium", "symbol": "Cm", "atomic_mass": 247},
    97: {"atomic_number": 97, "name": "Berkelium", "symbol": "Bk", "atomic_mass": 247},
    98: {"atomic_number": 98, "name": "Californium", "symbol": "Cf", "atomic_mass": 251},
    99: {"atomic_number": 99, "name": "Einsteinium", "symbol": "Es", "atomic_mass": 252},
    100: {"atomic_number": 100, "name": "Fermium", "symbol": "Fm", "atomic_mass": 257},
    101: {"atomic_number": 101, "name": "Mendelevium", "symbol": "Md", "atomic_mass": 258},
    102: {"atomic_number": 102, "name": "Nobelium", "symbol": "No", "atomic_mass": 259},
    103: {"atomic_number": 103, "name": "Lawrencium", "symbol": "Lr", "atomic_mass": 266},

    104: {"atomic_number": 104, "name": "Rutherfordium", "symbol": "Rf", "atomic_mass": 267},
    105: {"atomic_number": 105, "name": "Dubnium", "symbol": "Db", "atomic_mass": 268},
    106: {"atomic_number": 106, "name": "Seaborgium", "symbol": "Sg", "atomic_mass": 269},
    107: {"atomic_number": 107, "name": "Bohrium", "symbol": "Bh", "atomic_mass": 270},
    108: {"atomic_number": 108, "name": "Hassium", "symbol": "Hs", "atomic_mass": 277},
    109: {"atomic_number": 109, "name": "Meitnerium", "symbol": "Mt", "atomic_mass": 278},
    110: {"atomic_number": 110, "name": "Darmstadtium", "symbol": "Ds", "atomic_mass": 281},
    111: {"atomic_number": 111, "name": "Roentgenium", "symbol": "Rg", "atomic_mass": 282},
    112: {"atomic_number": 112, "name": "Copernicium", "symbol": "Cn", "atomic_mass": 285},
    113: {"atomic_number": 113, "name": "Nihonium", "symbol": "Nh", "atomic_mass": 286},
    114: {"atomic_number": 114, "name": "Flerovium", "symbol": "Fl", "atomic_mass": 289},
    115: {"atomic_number": 115, "name": "Moscovium", "symbol": "Mc", "atomic_mass": 290},
    116: {"atomic_number": 116, "name": "Livermorium", "symbol": "Lv", "atomic_mass": 293},
    117: {"atomic_number": 117, "name": "Tennessine", "symbol": "Ts", "atomic_mass": 294},
    118: {"atomic_number": 118, "name": "Oganesson", "symbol": "Og", "atomic_mass": 294},
}

    #Functions

    #Views

    #Page Setup

    #Controls

    pass

ft.run(main=main)