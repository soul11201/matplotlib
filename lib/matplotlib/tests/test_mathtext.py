import numpy as np
import matplotlib
from matplotlib.testing.decorators import image_comparison, knownfailureif
import matplotlib.pyplot as plt

math_tests = [
    r'$a+b+\dots+\dot{s}+\ldots$',
    r'$x \doteq y$',
    r'\$100.00 $\alpha \_$',
    r'$\frac{\$100.00}{y}$',
    r'$x   y$',
    r'$x+y\ x=y\ x<y\ x:y\ x,y\ x@y$',
    r'$100\%y\ x*y\ x/y x\$y$',
    r'$x\leftarrow y\ x\forall y\ x-y$',
    r'$x \sf x \bf x {\cal X} \rm x$',
    r'$x\ x\,x\;x\quad x\qquad x\!x\hspace{ 0.5 }y$',
    r'$\{ \rm braces \}$',
    r'$\left[\left\lfloor\frac{5}{\frac{\left(3\right)}{4}} y\right)\right]$',
    r'$\left(x\right)$',
    r'$\sin(x)$',
    r'$x_2$',
    r'$x^2$',
    r'$x^2_y$',
    r'$x_y^2$',
    r'$\prod_{i=\alpha_{i+1}}^\infty$',
    r'$x = \frac{x+\frac{5}{2}}{\frac{y+3}{8}}$',
    r'$dz/dt = \gamma x^2 + {\rm sin}(2\pi y+\phi)$',
    r'Foo: $\alpha_{i+1}^j = {\rm sin}(2\pi f_j t_i) e^{-5 t_i/\tau}$',
    r'$\mathcal{R}\prod_{i=\alpha_{i+1}}^\infty a_i \sin(2 \pi f x_i)$',
    r'Variable $i$ is good',
    r'$\Delta_i^j$',
    r'$\Delta^j_{i+1}$',
    r'$\ddot{o}\acute{e}\grave{e}\hat{O}\breve{\imath}\tilde{n}\vec{q}$',
    r"$\arccos((x^i))$",
    r"$\gamma = \frac{x=\frac{6}{8}}{y} \delta$",
    r'$\limsup_{x\to\infty}$',
    r'$\oint^\infty_0$',
    r"$f^'$",
    r'$\frac{x_2888}{y}$',
    r"$\sqrt[3]{\frac{X_2}{Y}}=5$",
    r"$\sqrt[5]{\prod^\frac{x}{2\pi^2}_\infty}$",
    r"$\sqrt[3]{x}=5$",
    r'$\frac{X}{\frac{X}{Y}}$',
    r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$",
    r'$\mathcal{H} = \int d \tau \left(\epsilon E^2 + \mu H^2\right)$',
    r'$\widehat{abc}\widetilde{def}$',
    r'$\Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma \Upsilon \Phi \Psi \Omega$',
    r'$\alpha \beta \gamma \delta \epsilon \zeta \eta \theta \iota \lambda \mu \nu \xi \pi \kappa \rho \sigma \tau \upsilon \phi \chi \psi$',
    # r'$\operatorname{cos} x$',

    # The examples prefixed by 'mmltt' are from the MathML torture test here:
        # http://www.mozilla.org/projects/mathml/demo/texvsmml.xhtml
    r'${x}^{2}{y}^{2}$',
    r'${}_{2}F_{3}$',
    r'$\frac{x+{y}^{2}}{k+1}$',
    r'$x+{y}^{\frac{2}{k+1}}$',
    r'$\frac{a}{b/2}$',
    r'${a}_{0}+\frac{1}{{a}_{1}+\frac{1}{{a}_{2}+\frac{1}{{a}_{3}+\frac{1}{{a}_{4}}}}}$',
    r'${a}_{0}+\frac{1}{{a}_{1}+\frac{1}{{a}_{2}+\frac{1}{{a}_{3}+\frac{1}{{a}_{4}}}}}$',
    r'$\binom{n}{k/2}$',
    r'$\binom{p}{2}{x}^{2}{y}^{p-2}-\frac{1}{1-x}\frac{1}{1-{x}^{2}}$',
    # 'mmltt10'    : r'$\sum _{\genfrac{}{}{0}{}{0\leq i\leq m}{0<j<n}}P\left(i,j\right)$',
    r'${x}^{2y}$',
    r'$\sum _{i=1}^{p}\sum _{j=1}^{q}\sum _{k=1}^{r}{a}_{ij}{b}_{jk}{c}_{ki}$',
    r'$\sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+\sqrt{1+x}}}}}}}$',
    r'$\left(\frac{{\partial }^{2}}{\partial {x}^{2}}+\frac{{\partial }^{2}}{\partial {y}^{2}}\right){|\varphi \left(x+iy\right)|}^{2}=0$',
    r'${2}^{{2}^{{2}^{x}}}$',
    r'${\int }_{1}^{x}\frac{\mathrm{dt}}{t}$',
    r'$\int {\int }_{D}\mathrm{dx} \mathrm{dy}$',
    # mathtex doesn't support array
    # 'mmltt18'    : r'$f\left(x\right)=\left\{\begin{array}{cc}\hfill 1/3\hfill & \text{if_}0\le x\le 1;\hfill \\ \hfill 2/3\hfill & \hfill \text{if_}3\le x\le 4;\hfill \\ \hfill 0\hfill & \text{elsewhere.}\hfill \end{array}$',
    # mathtex doesn't support stackrel
    # 'mmltt19'    : ur'$\stackrel{\stackrel{k\text{times}}{\ufe37}}{x+...+x}$',
    r'${y}_{{x}^{2}}$',
    # mathtex doesn't support the "\text" command
    # 'mmltt21'    : r'$\sum _{p\text{\prime}}f\left(p\right)={\int }_{t>1}f\left(t\right) d\pi \left(t\right)$',
    # mathtex doesn't support array
    # 'mmltt23'    : r'$\left(\begin{array}{cc}\hfill \left(\begin{array}{cc}\hfill a\hfill & \hfill b\hfill \\ \hfill c\hfill & \hfill d\hfill \end{array}\right)\hfill & \hfill \left(\begin{array}{cc}\hfill e\hfill & \hfill f\hfill \\ \hfill g\hfill & \hfill h\hfill \end{array}\right)\hfill \\ \hfill 0\hfill & \hfill \left(\begin{array}{cc}\hfill i\hfill & \hfill j\hfill \\ \hfill k\hfill & \hfill l\hfill \end{array}\right)\hfill \end{array}\right)$',
    # mathtex doesn't support array
    # 'mmltt24'   : u'$det|\\begin{array}{ccccc}\\hfill {c}_{0}\\hfill & \\hfill {c}_{1}\\hfill & \\hfill {c}_{2}\\hfill & \\hfill \\dots \\hfill & \\hfill {c}_{n}\\hfill \\\\ \\hfill {c}_{1}\\hfill & \\hfill {c}_{2}\\hfill & \\hfill {c}_{3}\\hfill & \\hfill \\dots \\hfill & \\hfill {c}_{n+1}\\hfill \\\\ \\hfill {c}_{2}\\hfill & \\hfill {c}_{3}\\hfill & \\hfill {c}_{4}\\hfill & \\hfill \\dots \\hfill & \\hfill {c}_{n+2}\\hfill \\\\ \\hfill \\u22ee\\hfill & \\hfill \\u22ee\\hfill & \\hfill \\u22ee\\hfill & \\hfill \\hfill & \\hfill \\u22ee\\hfill \\\\ \\hfill {c}_{n}\\hfill & \\hfill {c}_{n+1}\\hfill & \\hfill {c}_{n+2}\\hfill & \\hfill \\dots \\hfill & \\hfill {c}_{2n}\\hfill \\end{array}|>0$',
    r'${y}_{{x}_{2}}$',
    r'${x}_{92}^{31415}+\pi $',
    r'${x}_{{y}_{b}^{a}}^{{z}_{c}^{d}}$',
    r'${y}_{3}^{\prime \prime \prime }$'
]

def _run_all_tests():
    fig = plt.figure(figsize=(5, len(math_tests) / 2.0))
    for i, test in enumerate(math_tests):
        fig.text(0, float(len(math_tests) - i - 1) / len(math_tests), test)
    return fig

@image_comparison(baseline_images=['mathtext'])
def test_mathtext():
    fig = _run_all_tests()
    fig.savefig('mathtext')

@image_comparison(baseline_images=['mathtext_stix'])
def test_mathtext_stix():
    matplotlib.rcParams['mathtext.fontset'] = 'stix'

    fig = _run_all_tests()
    fig.savefig('mathtext_stix')

    matplotlib.rcParams['mathtext.fontset'] = 'cm'

@image_comparison(baseline_images=['mathtext_stixsans'])
def test_mathtext_stixsans():
    matplotlib.rcParams['mathtext.fontset'] = 'stixsans'

    fig = _run_all_tests()
    fig.savefig('mathtext_stixsans')

    matplotlib.rcParams['mathtext.fontset'] = 'cm'

