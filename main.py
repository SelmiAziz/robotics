from scorbot import Scorbot




u = False; 

while(True): 

	print("\n")
	print("<------SCORBOT------>")
	print("1:Set settings")
	print("2:Direct cinematics")
	print("3:Inverse cinematics")
	print("4:Direct cinematics encoder")
	print("5:Inverse cinematics encoder")
	c = input()
	
	if(c == "1"):
		print("Settings") 
		u = True
		l1 = 17
		l2 = 23
		l3 = 23
		d1 = 22
		d5 = 15
		a = 0.0482 
		b = 0.0602
		g = 0.22
		
		d = 0.12

		scorby = Scorbot(l1, l2, l3, d1, d5)
		
	elif(c == "2"):
		if(u == False): 
			print("No settings!!!!") 
		else: 
			print("\nInserire angoli giunti rotoidali in gradi")
			theta1 = int(input("Inserisci giunto1: "))
			theta2 = int(input("Inserisci giunto2: "))
			theta3 = int(input("Inserisci giunto3: "))
			theta4 = int(input("Inserisci giunto4: "))
			theta5 = int(input("Inserisci giunto5: "))
			scorby.cinematicaDiretta(theta1, theta2, theta3, theta4, theta5)
			r = scorby.getPosizioni()
			print(r)
			
	elif(c == "3"):
		if(u == False):
			print("No settings!!!!")
		else:
			print("\nInserire angolo di rollio, beccheggio e posizione della pinza")
			angoloRollio = int(input("Inserisci angolo di rollio: "))
			angoloBeccheggio = int(input("Inserisci angolo di beccheggio: "))
			xp = int(input("Inserisci coordinata x: "))
			yp = int(input("Inserisci coordinata y: ")) 
			zp = int(input("Inserisci coordinata z: ")) 
			scorby.cinematicaInversa(angoloRollio, angoloBeccheggio, xp, yp, zp)
			r = scorby.getAngoli()
			print(r)
			
	elif(c == "4"): 
		if(u == False): 
			print("No settings!!!!") 
		else: 
			print("\nInserire passi encoder")
			p0 = int(input("Inserisci p0: "))
			p1 = int(input("Inserisci p1: "))
			p2 = int(input("Inserisci p2: "))
			p3 = int(input("Inserisci p3: "))
			p4 = int(input("Inserisci p4: "))
			theta1 = -a*p0
			theta2 = -b*p1
			theta3 = b*(p1+p2)
			theta4 = -b*p2+g*(p3-p4)
			theta5 = d*(p3+p4)
			scorby.cinematicaDiretta(theta1, theta2, theta3, theta4, theta5)
			r = scorby.getPosizioni()
			print(r)
	
	elif(c == "5"): 
		if(u == False): 
			print("No settings!!!!") 
		else: 
			print("\nInserire angoli giunti rotoidali in gradi")
			theta1 = int(input("Inserisci giunto1: "))
			theta2 = int(input("Inserisci giunto2: "))
			theta3 = int(input("Inserisci giunto3: "))
			theta4 = int(input("Inserisci giunto4: "))
			theta5 = int(input("Inserisci giunto5: "))
			scorby.cinematicaDiretta(theta1, theta2, theta3, theta4, theta5)
			r = scorby.getPosizioni()
			r = (-r[0]/a, -r[1]/b, (r[4]+r[2])/b, 0.5*[(r[1]+r[2]+r[3])/g+r[4]/d], 0.5*[r[4]/d -(r[1]+r[2]+r[3])/g])
			print(r)			
	else:
		print("Comando non riconosciuto")
		
		
