import math


def wakeode(t, z, theta):
    (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi) = theta
    etas = etaw * Wc / (Wc - 24)
    (p, u, k) = z

    c = math.sin(2 * math.pi / 24 * (t - phi))

    dpdt = -alphaw * (p - beta * u) + xi * k * (c + muw)

    dudt = etaw * u

    dkdt = lam * k * (1 - k)

    return [dpdt, dudt, dkdt]