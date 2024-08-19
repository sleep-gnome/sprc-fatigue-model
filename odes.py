import math


def wakeode(t, z, theta):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    # etas = etaw * Wc / (Wc - 24)
    (p, u, h, k) = z

    oldp = (p - pf) - xi * h

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphaw * (oldp - beta * u) - xi * nu * h + xi * k * (c + muw)

    dudt = -etaw * (zeta * xi * oldp - u)

    dhdt = -nu * h

    dkdt = lam * k * (1 - k)

    return [dpdt, dudt, dhdt, dkdt]


def sleepode(t, z, theta):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    etas = etaw * Wc / (24 - Wc)
    (p, u, h, k) = z

    oldp = (p - pf) - xi * h

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphas * (oldp - beta * (u - 1 / etas)) + xi * nu * (gam * oldp - h) + xi * k * (c - mus)

    dudt = etas * (zeta * xi * oldp - u) + 1

    dhdt = nu * (gam * oldp - h)

    dkdt = -lam * k

    return [dpdt, dudt, dhdt, dkdt]
