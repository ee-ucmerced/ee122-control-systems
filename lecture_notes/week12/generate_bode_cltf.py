import numpy as np
import matplotlib.pyplot as plt

# Plant: G(s) = 5 / (s + 2)
# Provided-controller example: C(s) = 8 / (0.2 s + 1)
# Closed-loop transfer function:
# T(s) = C(s)G(s) / (1 + C(s)G(s))
#      = 40 / ((0.2s + 1)(s + 2) + 40)
#      = 40 / (0.2 s^2 + 1.4 s + 42)

num = np.array([40.0])
den = np.array([0.2, 1.4, 42.0])

omega = np.logspace(-2, 2, 800)
s = 1j * omega
resp = np.polyval(num, s) / np.polyval(den, s)
mag_db = 20 * np.log10(np.maximum(np.abs(resp), 1e-12))

fig, ax = plt.subplots(figsize=(6.8, 4.0), dpi=200)
ax.semilogx(omega, mag_db, linewidth=2)
ax.set_xlabel(r"Frequency $\omega$ [rad/s]")
ax.set_ylabel(r"$20\log_{10}(|T(j\omega)|)$ [dB]")
ax.grid(True, which="both", linestyle="--", alpha=0.5)
fig.tight_layout()
fig.savefig("bode_cltf.png", bbox_inches="tight")
