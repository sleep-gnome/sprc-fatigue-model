import math


def wakeode(t, z, theta):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    etas = etaw * Wc / (Wc - 24)
    (p, u, h, k) = z

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphaw * ((p - pf) - beta * u) + xi * k * (c + muw)

    dudt = -etaw * (zeta * xi * (p - pf) - u)

    dhdt = -nu * h

    dkdt = lam * k * (1 - k)

    # allp = (p - p0) + xi * h

    return [dpdt, dudt, dhdt, dkdt]


def sleepode(t, z, theta):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    etas = etaw * Wc / (24 - Wc)
    (p, u, h, k) = z

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphas * ((p - pf) - beta * (u - 1 / etas)) + xi * k * (c - mus)

    dudt = etas * (zeta * xi * (p - pf) - u) + 1

    dhdt = nu * (gam * (p - pf) - h)

    dkdt = -lam * k

    # allp = (p - p0) + xi * h

    return [dpdt, dudt, dhdt, dkdt]
