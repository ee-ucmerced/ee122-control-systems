import numpy as np
import matplotlib.pyplot as plt
import control as ct
import streamlit as st


st.set_page_config(page_title="Bode Plot Control Design Demo", layout="wide")


# ----------------------------
# Helpers
# ----------------------------
def bode_data(sys, omega):
    resp = np.array([ct.evalfr(sys, 1j * w) for w in omega], dtype=complex)
    mag_db = 20 * np.log10(np.maximum(np.abs(resp), 1e-12))
    phase_deg = np.degrees(np.unwrap(np.angle(resp)))
    return mag_db, phase_deg


def plot_mag(omega, mag_db, title):
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.semilogx(omega, mag_db, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(r"Frequency $\omega$ [rad/s]")
    ax.set_ylabel("Magnitude [dB]")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def plot_phase(omega, phase_deg, title):
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.semilogx(omega, phase_deg, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(r"Frequency $\omega$ [rad/s]")
    ax.set_ylabel("Phase [deg]")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def plot_pole_map(poles, title):
    fig, ax = plt.subplots(figsize=(5.5, 3.2))

    if len(poles) > 0:
        ax.scatter(np.real(poles), np.imag(poles), marker="x", s=100, linewidths=2)

        re = np.real(poles)
        im = np.imag(poles)

        x_min = min(np.min(re) - 1.0, -0.5)
        x_max = max(np.max(re) + 1.0, 0.5)

        if np.allclose(im, 0):
            y_min, y_max = -1.0, 1.0
        else:
            y_pad = max(0.5, 0.25 * (np.max(im) - np.min(im) + 1e-9))
            y_min = np.min(im) - y_pad
            y_max = np.max(im) + y_pad

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
    else:
        ax.set_xlim(-2, 1)
        ax.set_ylim(-1, 1)

    ax.axhline(0, color="k", linewidth=1)
    ax.axvline(0, color="k", linewidth=1)
    ax.set_title(title)
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


# ----------------------------
# Title / notes
# ----------------------------
st.title("Bode Plots for Plant, P Closed Loop, and PI Closed Loop")
st.markdown(
    r"""
This app uses the plant
\[
G(s)=\frac{K}{\tau s+1}
\]
and compares:

- the open-loop plant \(G(s)\),
- the P closed-loop transfer function
  \[
  T_P(s)=\frac{k_p G(s)}{1+k_p G(s)},
  \]
- the PI closed-loop transfer function
  \[
  T_{PI}(s)=\frac{\left(k_p+\frac{k_i}{s}\right)G(s)}{1+\left(k_p+\frac{k_i}{s}\right)G(s)}.
  \]
"""
)

omega = np.logspace(-2, 2, 600)

# ----------------------------
# Controls row
# ----------------------------
ctrl1, ctrl2, ctrl3 = st.columns(3)

with ctrl1:
    st.subheader("Plant")
    K = st.slider("K", min_value=0.1, max_value=10.0, value=1.0, step=0.1, key="K_slider")
    tau = st.slider("tau", min_value=0.1, max_value=10.0, value=1.0, step=0.1, key="tau_slider")

with ctrl2:
    st.subheader("P Controller")
    kp_p = st.slider("kp (P)", min_value=0.0, max_value=20.0, value=2.0, step=0.1, key="kp_p_slider")

with ctrl3:
    st.subheader("PI Controller")
    kp_pi = st.slider("kp (PI)", min_value=0.0, max_value=20.0, value=2.0, step=0.1, key="kp_pi_slider")
    ki_pi = st.slider("ki (PI)", min_value=0.0, max_value=20.0, value=1.0, step=0.1, key="ki_pi_slider")


# ----------------------------
# Systems
# ----------------------------
G = ct.tf([K], [tau, 1])

Cp = ct.tf([kp_p], [1])
Tp = ct.feedback(Cp * G, 1)

Cpi = ct.tf([kp_pi, ki_pi], [1, 0])
Tpi = ct.feedback(Cpi * G, 1)

# ----------------------------
# Data
# ----------------------------
mag_g, phase_g = bode_data(G, omega)
mag_tp, phase_tp = bode_data(Tp, omega)
mag_tpi, phase_tpi = bode_data(Tpi, omega)

poles_g = ct.poles(G)
poles_tp = ct.poles(Tp)
poles_tpi = ct.poles(Tpi)

# ----------------------------
# Optional numeric summaries
# ----------------------------
sum1, sum2, sum3 = st.columns(3)

with sum1:
    st.caption("Plant pole")
    st.write(poles_g)

with sum2:
    st.caption("P closed-loop pole(s)")
    st.write(poles_tp)

with sum3:
    st.caption("PI closed-loop pole(s)")
    st.write(poles_tpi)

# ----------------------------
# Aligned plot rows
# ----------------------------
mag_col1, mag_col2, mag_col3 = st.columns(3)
with mag_col1:
    st.pyplot(plot_mag(omega, mag_g, "Bode magnitude: plant"), use_container_width=True)
with mag_col2:
    st.pyplot(plot_mag(omega, mag_tp, "Bode magnitude: P closed loop"), use_container_width=True)
with mag_col3:
    st.pyplot(plot_mag(omega, mag_tpi, "Bode magnitude: PI closed loop"), use_container_width=True)

ph_col1, ph_col2, ph_col3 = st.columns(3)
with ph_col1:
    st.pyplot(plot_phase(omega, phase_g, "Bode phase: plant"), use_container_width=True)
with ph_col2:
    st.pyplot(plot_phase(omega, phase_tp, "Bode phase: P closed loop"), use_container_width=True)
with ph_col3:
    st.pyplot(plot_phase(omega, phase_tpi, "Bode phase: PI closed loop"), use_container_width=True)

pole_col1, pole_col2, pole_col3 = st.columns(3)
with pole_col1:
    st.pyplot(plot_pole_map(poles_g, "Pole map: plant"), use_container_width=True)
with pole_col2:
    st.pyplot(plot_pole_map(poles_tp, "Pole map: P closed loop"), use_container_width=True)
with pole_col3:
    st.pyplot(plot_pole_map(poles_tpi, "Pole map: PI closed loop"), use_container_width=True)

# ----------------------------
# Small interpretation block
# ----------------------------
st.markdown(
    r"""
### What to look for

- Increasing \(k_p\) in the P controller moves the closed-loop pole left and changes the closed-loop frequency response.
- Adding integral action through \(k_i\) changes the low-frequency behavior strongly, which is tied to improved step tracking.
- The plots here are for the plant \(G(s)\) and the closed-loop transfer functions \(T_P(s)\), \(T_{PI}(s)\).
"""
)