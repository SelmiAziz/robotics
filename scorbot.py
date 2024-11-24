import math

class Scorbot:
    def __init__(self, l1, l2, l3, d1, d5):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.d1 = d1
        self.d5 = d5
        self.theta1 = 0
        self.theta2 = 0
        self.theta3 = 0
        self.theta4 = 0
        self.theta5 = 0
        self.xd = 0
        self.yd = 0
        self.zd = 0

    def getPosizioni(self):
        return (self.xd, self.yd, self.zd)

    def getAngoli(self):
        return (self.theta1, self.theta2, self.theta3, self.theta4, self.theta5)

    def coseno(self, angolo):
        c = math.cos(math.radians(angolo))
        return 0 if abs(c) < 1e-10 else c

    def seno(self, angolo):
        s = math.sin(math.radians(angolo))
        return 0 if abs(s) < 1e-10 else s

    def angoloAtan2(self, y, x):
        """Calcola atan2 e restituisce l'angolo in gradi."""
        result = math.atan2(y, x)
        result_degrees = math.degrees(result)
        return 0 if abs(result_degrees) < 1e-10 else result_degrees

    def angoloAcos(self, value):
        """Calcola acos e restituisce l'angolo in gradi."""
        if value < -1:
            value = -1
        elif value > 1:
            value = 1
        result = math.acos(value)
        result_degrees = math.degrees(result)
        return 0 if abs(result_degrees) < 1e-10 else result_degrees

    def calcolaPosizione(self):
        self.xd = self.coseno(self.theta1) * (
            self.l1 + self.l2 * self.coseno(self.theta2) +
            self.l3 * self.coseno(self.theta2 + self.theta3) -
            self.d5 * self.seno(self.theta2 + self.theta3 + self.theta4)
        )
        self.yd = self.seno(self.theta1) * (
            self.l1 + self.l2 * self.coseno(self.theta2) +
            self.l3 * self.coseno(self.theta2 + self.theta3) -
            self.d5 * self.seno(self.theta2 + self.theta3 + self.theta4)
        )
        self.zd = (
            self.d1 - self.l2 * self.seno(self.theta2) -
            self.l3 * self.seno(self.theta2 + self.theta3) -
            self.d5 * self.coseno(self.theta2 + self.theta3 + self.theta4)
        )

    def cinematicaDiretta(self, theta1, theta2, theta3, theta4, theta5):
        self.theta1 = theta1
        self.theta2 = theta2
        self.theta3 = theta3
        self.theta4 = theta4
        self.theta5 = theta5
        self.calcolaPosizione()

    def calcolaAngoli(self, angoloRollio, angoloBeccheggio):
        self.theta5 = angoloRollio
        self.theta1 = self.angoloAtan2(self.yd, self.xd)
        A1 = (self.xd * self.coseno(self.theta1) +
              self.yd * self.seno(self.theta1) -
              self.d5 * self.coseno(angoloBeccheggio) - self.l1)
        A2 = self.d1 - self.zd - self.d5 * self.seno(angoloBeccheggio)
        self.theta3 = self.angoloAcos((A1**2 + A2**2 - self.l2**2 - self.l3**2) / (2 * self.l2 * self.l3))
        self.theta2 = self.angoloAtan2(
            (self.l2 + self.l3 * self.coseno(self.theta3)) * A2 - self.l3 * self.seno(self.theta3) * A1,
            (self.l2 + self.l3 * self.coseno(self.theta3)) * A1 + self.l3 * self.seno(self.theta3) * A2
        )
        self.theta4 = angoloBeccheggio - self.theta2 - self.theta3 - 90

    def cinematicaInversa(self, angoloRollio, angoloBeccheggio, xf, yf, zf):
        self.xd = xf
        self.yd = yf
        self.zd = zf
        self.calcolaAngoli(angoloRollio, angoloBeccheggio)

