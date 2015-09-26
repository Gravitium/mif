import math
import random


class Math:
    h = 6.62607004 * 10 ** -34
    c = 299792458
    G = 6.67384 * 10 ** -11
    hbar = 1.054571726 * 10 ** -34
    k = 1.3806488 * 10 ** - 23
    electron_mass = 9.10938291 * 10 ** -31
    golden = (1 + math.sqrt(5))/2

    # planck {natural} units
    planck_length = math.sqrt((G * hbar) / c ** 3)
    planck_mass = math.sqrt(hbar * c / G)
    planck_energy = planck_mass * c ** 2
    planck_time = math.sqrt(G * hbar / c ** 5)

    def frequency_to_momentum(self, f, to_string=False):
        if not to_string:
            return (self.h * f) / self.c
        else:
            p = (self.h * f) / self.c
            return 'The momentum is {} kg*m/s'.format(p)

    def wavelength_to_momentum(self, wavelength, to_string=False):
        if not to_string:
            return self.h / wavelength
        else:
            p = self.h / wavelength
            return "The momentum of the foton is {} kg*m/s".format(p)

    def energy_to_momentum(self, e, to_s=False):
        if not to_s:
            return e / self.c
        else:
            a = e / self.c
            return "The momentum is {} J".format(a)

    def wavelength_to_energy(self, wavelength, to_string=False):
        if not to_string:
            return self.h * (self.c / wavelength)
        else:
            e = self.h * (self.c / wavelength)
            print 'The energy is {} J'.format(e)

    def energy_to_mass(self, e):
        return e / self.c ** 2

    def mass_to_energy(self, mass, to_string=False):
        if not to_string:
            return mass * self.c ** 2
        else:
            e = mass * self.c ** 2
            return 'The energy is {} J'.format(e)

    def log_standart_model(self):
        print "---------------------------------"
        print "!  u  !  c  !  t   !  g  !  H  !"
        print "!  d  !  s  !  b   ! ph  !     !"
        print "!-----!-----!------!     !     !"
        print "! Ve  ! Vmu ! Vtau !  Z  !     !"
        print "! e-  ! mu- ! tau- !  W  !     !"
        print "--------------------------------"

    def quark_help(self, flavour):
        if flavour == 'u':
            print 'First generation.'
            print 'Q = +2/3'
            print 'B = +1/3'
            print 'SPIN = +1/2'
            print 'm = 2.3Mev/c^2'
        elif flavour == 'd':
            print 'First generation.'
            print 'Q = -1/3'
            print 'B = +1/3'
            print 'SPIN = +1/2'
            print 'm = 4.8Mev/c^2'
        elif flavour == 'c':
            print 'Second generation.'
            print 'Q = -1/3'
            print 'B = +1/3'
            print 'SPIN = +1/2'
            print 'm = 98Mev/c^2'
        elif flavour == 's':
            print 'Second generation.'
            print 'Q = -1/3'
            print 'B = +1/3'
            print 'SPIN = +1/2'
            print 'm = 1.275GeV/c**2'
        else:
            "WHY ON EARTH YOU NEED TO KNOW ANYTHING ABOUT TOP OR BOTTOM QUARK ?!?"

    def orbital_period(self, m1, m2, a):
        pi = math.pi
        T = 2 * pi * math.sqrt(a ** 3 / self.G * (m1))
        return T / 60 / 60 / 24 / 365

    def energy_to_wavelength(self, e):
        return self.h / e

    def mass_to_wavelength(self, mass):
        e = self.mass_to_energy(mass)
        return self.energy_to_wavelength(e)

    #UNIT CONVERSION

    def GeV_to_J(self, gev):
        x = long(gev)
        return 1.60217657 * 10 ** -10 * x

    def Mev_to_J(self, mev):
        return 1.60217657 * 10 ** -13 * mev

    def eV_to_J(self, ev):
        return 1.60217657 * 10 ** -19 * ev

    # revers
    def J_to_GeV(self, gev):

        x = long(gev)
        return 1.60217657 * 10 ** -10 / x

    def J_to_MeV(self, mev):
        return 1.60217657 * 10 ** -13 / mev

    def J_to_eV(self, ev):
        return 1.60217657 * 10 ** -19 / ev

    # end reverse#
    #END UNIT CONVERSION

    def print_planck_units(self):
        print """
        planck_length = math.sqrt((G * hbar) / c ** 3)
        planck_mass = math.sqrt(hbar * c / G)
        planck_energy = planck_mass * c ** 2
        planck_time = math.sqrt(G * hbar / c ** 5"""

    def magnification(self, fo, fe, to_string=False):
        #Telescope magnification
        M = fo / fe
        if not to_string:
            return M
        else:
            return "The magnification is {}x . ".format(M)

    def particle_wavelength(self, mass, kinetic, to_string=False):

        if not to_string:
            return self.h / math.sqrt(2 * mass * kinetic)
        else:
            wavelength = self.h / math.sqrt(2 * mass * kinetic)
            return "The wavelenght is {} meters".format(wavelength)

    def schwarzschild_radius(self, mass, solar=True, to_string=False, area=True):
        #polomer cerne diry
        if solar:
            mass *= 1.989 * 10 ** 30
            radius = (2 * mass * self.G) / self.c ** 2
        else:
            radius = (2 * mass * self.G) / self.c ** 2
        if not area:
            if not to_string:
                return radius
            else:
                return "The event horizont radius is {} meters, given by 2MG/c^2".format(radius)
        else:
            area = 4 * math.pi * radius ** 2
            if not to_string:
                print area
                return radius
            else:
                return "The event horizont radius is {} m, given by 2MG/c^2. The area of a sphere with this Schwarzchild radius is {} m^2,\
                 given by 4*pi*r^2.".format(radius, area)

    def BH_temperature(self, M, to_string=False, solar=True, to_celsius=False):
        # teplota na povrchu cerne diry
        if solar:
            M *= 2 * 10 ** 30
        T = (self.hbar * self.c ** 3) / 8 * math.pi * self.k * self.G * M

        if to_celsius:
            T += 273
            if not to_string:
                return T
            else:
                return "The temperature of the black hole (at event horizont) is {} Celsius".format(T)
        else:
            if not to_string:
                return T
            else:
                return "The temperature of the black hole (at event horizont) is {} Kelvin".format(T)

    # RELATIVISTIC, lorentz transformation

    def r_momentum(self, mass, velocity, to_string=False):
        x = mass*velocity/math.sqrt(1+velocity**2/self.c**2)
        if not to_string:
            return x
        else:
            return "The relativistic momentum is {}".format(x)

    def r_velocity(self, v1, v2, to_string=False):
        x = v1+v2/1+(v1*v2)/self.c**2
        if not to_string:
            return x
        else:
            return "The relativistic velocity is {}".format(x)

    def cat(self):
        print "at the moment, the cat is dead and alive"
        for i in range(0, 3):
            print "..."
        life = random.choice([True, False])
        if life:
            print "The cat is alive!"
        else:
            print "The cat is dead!"
            
a = Math()

def understand():
    print """
 1  frequency_to_momentum
 2  wavelength_to_momentum
 3  energy_to_momentum
 4  wavelength_to_energy
 5  energy_to_mass
 6  mass_to_energy
 7  log_standart_model
 8  quark_help
 9  orbital_period
 10  energy_to_wavelength
 11  mass_to_wavelength
 12  GeV_to_J
 13  Mev_to_J
 14  eV_to_J
 15  J_to_GeV
 16  J_to_MeV
 17  J_to_eV
 18  print_planck_units
 19  magnification
 20  particle_wavelength
 21  schwarzschild_radius
 22  BH_temperature
 23  r_momentum
 24  r_velocity
 25  cat
    """
    for i in range(20):
        k = float(raw_input("Choose function >>> "))
        if k == 1:
           print a.frequency_to_momentum(float(raw_input("Frequency >>>")), bool(raw_input("To string >>>")))

        elif k == 2:
            print a.wavelength_to_momentum(float(raw_input("Wavelength >>>")), bool(raw_input("To string >>>")))

        elif k == 3:
            print a.energy_to_momentum(float(raw_input("Energy >>>")))

        elif k == 4:
            print a.wavelength_to_energy(float(raw_input("Wavelength >>>")), bool(raw_input("To string >>>")))

        elif k == 5:
            print a.energy_to_mass(float(raw_input("Energy >>>")))

        elif k == 6:
            print a.mass_to_energy(float(raw_input("Mass >>>")))

        elif k == 7:
            a.log_standart_model()

        elif k == 8:
            f = raw_input("Falvour >>> ")
            a.quark_help(f)

        elif k == 9:
            m1 = float(raw_input("Mass 1 >>> "))
            m2 = float(raw_input("mass 2 >>> "))
            s = float(raw_input("Semi majour axis >>>"))
            print(a.orbital_period(m1, m2, s))

        elif k == 10:
            print(a.energy_to_wavelength(float(raw_input("energy >>>"))))
            
        elif k == 11:
            print(a.mass_to_wavelength(float(raw_input("mass >>>"))))
        
        elif k == 12:
            print(a.GeV_to_J(float(raw_input("GeV >>> "))))
        
        elif k == 13:
            print(a.MeV_to_J(float(raw_input("MeV >>> "))))
            
        elif k == 14:
            print(a.eV_to_J(float(raw_input("eV >>> "))))
        
        elif k == 15:
            print(a.J_to_GeV(float(raw_input("J >>>"))))
        
        elif k == 16:
            print(a.J_to_MeV(float(raw_input("J >>>"))))
        
        elif k == 17:
            print(a.J_to_eV(float(raw_input("J >>>"))))
        
        elif k== 18:
            a.print_planck_units()
        
        elif k == 19:
            print(a.magnification(float(raw_input(">>> ")), float(raw_input(">>> ")), bool(raw_input(">>> "))))
            
        elif k == 20:
            print(a.particle_wavelength(float(raw_input("mass >>>"))), float(raw_input("kinetic >>>")), bool(raw_input("To string >>>")))

        elif k == 21:
            print a.schwarzschild_radius(float(raw_input("mass >>>")), bool(raw_input("solar >>>")), bool(raw_input("to string >>>")), bool(raw_input("area >>>")))


understand()







