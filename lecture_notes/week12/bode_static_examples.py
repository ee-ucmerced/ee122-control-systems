import numpy as np
import matplotlib.pyplot as plt
import control as ct

K = 1.0
TAU = 0.5
KP_P = 4.0
KP_PI = 2.0
KI_PI = 4.0
OMEGA = np.logspace(-2, 2, 800)


def freq_response(sys, omega):
    vals = np.array([complex(ct.evalfr(sys, 1j * w)) for w in omega])
    mag_db = 20.0 * np.log10(np.maximum(np.abs(vals), 1e-12))
    phase_deg = np.unwrap(np.angle(vals)) * 180.0 / np.pi
    return mag_db, phase_deg


def tf_poles(sys):
    den = np.asarray(sys.den[0][0], dtype=float)
    den = np.trim_zeros(den, trim="f")
    return np.roots(den)


def plot_pole_map(ax, poles, title):
    ax.axhline(0.0, linewidth=0.8)
    ax.axvline(0.0, linewidth=0.8)
    ax.scatter(np.real(poles), np.imag(poles), marker="x", s=80)
    ax.set_xlabel("Real")
    ax.set_ylabel("Imag")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

    real_vals = np.real(poles)
    imag_vals = np.imag(poles)
    span_r = max(0.5, np.max(real_vals) - np.min(real_vals), np.max(np.abs(real_vals)))
    span_i = max(0.5, np.max(np.abs(imag_vals)))
    center_r = 0.5 * (np.max(real_vals) + np.min(real_vals))

    ax.set_xlim(min(-0.2, center_r - 1.4 * span_r), 0.2)
    ax.set_ylim(-1.4 * span_i, 1.4 * span_i)


s = ct.TransferFunction.s
G = K / (TAU * s + 1)
C_p = KP_P
C_pi = KP_PI + KI_PI / s
T_p = ct.feedback(C_p * G, 1)
T_pi = ct.feedback(C_pi * G, 1)

systems = [
    (G, "Open-loop plant $G(s)$"),
    (T_p, "Closed loop with P"),
    (T_pi, "Closed loop with PI"),
]

fig, axes = plt.subplots(3, 3, figsize=(12, 8), constrained_layout=True)

for col, (sys, title) in enumerate(systems):
    mag_db, phase_deg = freq_response(sys, OMEGA)
    poles = tf_poles(sys)

    ax_mag = axes[0, col]
    ax_phase = axes[1, col]
    ax_pole = axes[2, col]

    ax_mag.semilogx(OMEGA, mag_db, linewidth=2)
    ax_mag.set_title(title)
    ax_mag.set_ylabel("Magnitude [dB]")
    ax_mag.grid(True, which="both", alpha=0.3)

    ax_phase.semilogx(OMEGA, phase_deg, linewidth=2)
    ax_phase.set_ylabel("Phase [deg]")
    ax_phase.set_xlabel("Frequency [rad/s]")
    ax_phase.grid(True, which="both", alpha=0.3)

    plot_pole_map(ax_pole, poles, "Pole locations")

fig.suptitle(
    f"Bode plots and pole maps for G(s), P closed loop, and PI closed loop\n"
    f"K={K}, tau={TAU}, kp(P)={KP_P}, kp(PI)={KP_PI}, ki(PI)={KI_PI}",
    fontsize=14,
)

plt.savefig("bode_side_by_side.png", dpi=200, bbox_inches="tight")
plt.show()
