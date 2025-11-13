#  Flam R&D Assignment — Parametric Curve Fitting

##  Problem Statement
The task is to determine the **unknown parameters (θ, M, X)** in the given **parametric curve equations**:

\[
\begin{aligned}
x(t) &= t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X \\[4pt]
y(t) &= 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\end{aligned}
\]
where  
\[
6 < t < 60
\]

and the provided CSV file `points.csv` contains the **x** and **y** coordinates of the curve points.

---

##  Objective
Estimate the parameters:
- \( 0° < \theta < 50° \)
- \( -0.05 < M < 0.05 \)
- \( 0 < X < 100 \)

so that the generated (x(t), y(t)) best fits the data points using nonlinear least squares optimization.

---

##  Methodology

1. **Data Loading** — Read the provided CSV containing (x, y) values.
2. **Parameterization** — Assume parameter `t` is linearly spaced between 6 and 60 for N data points.
3. **Curve Model** — Implement the given parametric equations in Python.
4. **Optimization** — Use `scipy.optimize.curve_fit` to estimate θ, M, and X.
5. **Visualization** — Plot both original data points and fitted curve for comparison.
6. **Verification** — Output parameter values and visual confirmation.

---

##  Final Results

| Parameter | Symbol | Value | Units |
|------------|---------|--------|--------|
| Angle | θ | **29.5826°** (0.51631754 rad) | degrees/radians |
| Exponent Coefficient | M | **-0.05** | — |
| Translation Constant | X | **55.0135339** | units |

---

##  Final Equation (in LaTeX)

\[
\begin{aligned}
x(t) &= t\cos(0.51631754) - e^{-0.05|t|}\sin(0.3t)\sin(0.51631754) + 55.0135339\\[6pt]
y(t) &= 42 + t\sin(0.51631754) + e^{-0.05|t|}\sin(0.3t)\cos(0.51631754)
\end{aligned}
\quad,\quad 6\le t\le 60
\]

---

##  Implementation Details

- **Language:** Python 3  
- **Libraries:** NumPy, SciPy, Matplotlib, Pandas  
- **Files Included:**
  - `main.py` — main code for optimization and visualization  
  - `points.csv` — dataset provided  
  - `fitted_params.txt` — final parameter values  
  - `fit_plot.png` — visualization comparing data and fitted curve  
  - `README.md` — documentation

---

##  Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Flam-Assignment-Repo.git
   cd Flam-Assignment-Repo
