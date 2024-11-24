
def calculate_parameters(theta1, theta2, theta3, theta4, theta5, p0, p1, p2, p3, p4):
    # Calcolo di alpha
    alpha = -theta1 / p0 if p0 != 0 else None

    # Calcolo di beta
    beta1 = -theta2 / p1 if p1 != 0 else None
    beta2 = (theta2 + theta3) / p2 if p2 != 0 else None
    if beta1 is not None and beta2 is not None and abs(beta1 - beta2) > 1e-6:
        raise ValueError("Valori inconsistenti per beta.")
    beta = beta1 if beta1 is not None else beta2

    # Calcolo di gamma
    gamma = (theta2 + theta3 + theta4) / (p3 - p4) if (p3 - p4) != 0 else None

    # Calcolo di delta
    delta = theta5 / (p3 + p4) if (p3 + p4) != 0 else None

    return alpha, beta, gamma, delta


# Esempio di utilizzo
theta1 = 0; 
theta2 = 90;
theta3 = 90; 
theta4 = 90;
theta5 = 0; 

p0 = 0
p1 = -15
p2 = 1500
p3 = 350
p4 = -350

alpha, beta, gamma, delta = calculate_parameters(theta1, theta2, theta3, theta4, theta5, p0, p1, p2, p3, p4)

print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"gamma = {gamma}")
print(f"delta = {delta}")




