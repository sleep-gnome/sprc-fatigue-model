import math


def wakeode(t, z, theta, p0):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, nu, gam, zeta) = theta
    etas = etaw * Wc / (Wc - 24)
    (p, u, h, k) = z

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphaw * ((p - p0) - beta * u) + xi * k * (c + muw)

    dudt = -etaw * (zeta * xi * (p - p0) - u)

    dhdt = -nu * h

    dkdt = lam * k * (1 - k)

# allp = (p - p0) + xi * h

    return [dpdt, dudt, dhdt, dkdt]

def sleepode(t, z, theta, p0):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, nu, gam, zeta) = theta
    etas = etaw * Wc / (Wc - 24)
    (p, u, h, k) = z

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphas * ((p - p0) - beta * (u + 1/etas)) + xi * k * (c - mus)

    dudt = etas * (zeta * xi * (p - p0) - u) + 1

    dhdt = nu * (gam * (p - p0) - h)

    dkdt = -lam * k

# allp = (p - p0) + xi * h

    return [dpdt, dudt, dhdt, dkdt]
