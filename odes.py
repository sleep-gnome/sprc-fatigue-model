import math


def wakeode(t, z, theta):
    # (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    # etas = etaw * Wc / (Wc - 24)
    (p, u, h, k) = z

    oldp = (p - Params.pf) - Params.si_tog * Params.xi * h

    c = math.sin(2 * math.pi / 24 * (t - Params.phi))

    dpdt = (-Params.alpha_w * (oldp - Params.beta * u)
            - Params.si_tog * Params.xi * Params.nu * h
            + Params.xi * k * (c + Params.mu_w))

    dudt = -Params.eta_w * (Params.zeta * Params.xi * oldp - u)

    dhdt = -Params.nu * h

    dkdt = Params.lam * k * (1 - k)

    return [dpdt, dudt, dhdt, dkdt]


def sleepode(t, z, theta):
    # (alphaw, alphas, beta, etaw, Wc, muw, mus, lam, phi, xi, pf, nu, gam, zeta) = theta
    etas = Params.eta_w * Params.Wc / (24 - Params.Wc)
    (p, u, h, k) = z

    oldp = (p - Params.pf) - Params.si_tog * Params.xi * h

    c = math.sin(2 * math.pi / 24 * (t - Params.phi))

    dpdt = (-Params.alpha_s * (oldp - Params.beta * (u - 1 / etas))
            + Params.si_tog * Params.xi * Params.nu * (Params.gam * oldp - h)
            + Params.xi * k * (c - Params.mu_s))

    dudt = etas * (Params.zeta * Params.xi * oldp - u) + 1

    dhdt = Params.nu * (Params.gam * oldp - h)

    dkdt = -Params.lam * k

    return [dpdt, dudt, dhdt, dkdt]

class Params(object):
    alpha_w = 0.028
    alpha_s = 0.26
    beta = 0.26
    eta_w = 0.0126
    Wc = 20.22
    mu_w = 0.466
    mu_s = 1.5
    lam = 0.49
    phi = 21.2
    xi = 1.09
    pf = 0
    nu = 1.37
    gam = 0.71
    zeta = 1.31
    si_tog = 1


def pvt_toggle():
    Params.alpha_w = 0.028
    Params.alpha_s = 0.26
    Params.Wc = 20.2
    Params.mu_w = 0.466
    Params.xi = 1.09
    Params.pf = 0


def kss_toggle():
    Params.alpha_w = 0.22
    Params.alpha_s = 0.037
    Params.Wc = 22.02
    Params.mu_w = 0.82
    Params.xi = 0.51
    Params.pf = 1


def si_toggle(si_value):
    Params.si_tog = si_value