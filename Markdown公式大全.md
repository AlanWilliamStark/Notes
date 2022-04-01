# Preface

This document aimed to recording MD type expression of all of mathematical formula. Because it's same like LATEX when I need to use it I can search everything I want at here.

# List

|             math expression             |           LaTeX code            |
| :-------------------------------------: | :-----------------------------: |
|          **Sup & sub script**           |                                 |
|                  $x^2$                  |               x^2               |
|                  $x_n$                  |               x_n               |
|             **Placeholder**             |                                 |
|              $x \qquad y$               |           x \qquad y            |
|               $x \quad y$               |            x \quad y            |
|                 $x \ y$                 |              x \ y              |
|          **Basic operations**           |                                 |
|                 $a+b-c$                 |              a+b-c              |
|           $\times \cdot \ast$           |        \times \cdot \ast        |
|               $a\div{b}$                |            a\div{b}             |
|              $\frac{a}{b}$              |           \frac{a}{b}           |
|               $\sqrt{a}$                |            \sqrt{a}             |
|              $\sqrt[3]{8}$              |           \sqrt[3]{8}           |
|                 $\log$                  |              \log               |
|                $a\pm{b}$                |             a\pm{b}             |
|                $\cdots$                 |             \cdots              |
|       **Trigonometric functions**       |                                 |
|             $\sin{\theta}$              |          \sin{\theta}           |
|             $\cos{\theta}$              |          \cos{\theta}           |
|             $\tan{\theta}$              |          \tan{\theta}           |
|             $\cot{\theta}$              |          \cot{\theta}           |
| **Vector, accumulate, multiply, limit** |                                 |
|                $\vec{F}$                |             \vec{F}             |
|               $\sum_{a}$                |             \sum{a}             |
|               $\prod{a}$                |            \prod{a}             |
|                 $\int$                  |              \int               |
|    $\frac{\partial{x}}{\partial{y}}$    | \frac{\partial{x}}{\partial{y}} |
|                $\lim{x}$                |             \lim{x}             |
|       $\sum\limits_{i=1}^{n} k^2$       |    \sum\limits_{i=1}^{n} k^2    |
|         **relational operator**         |                                 |
|                 $\leq$                  |              \leq               |
|                 $\geq$                  |              \geq               |
|                  $\gt$                  |               \gt               |
|                  $\lt$                  |               \lt               |
|                   $=$                   |                =                |
|                 $\neq$                  |              \neq               |
|           $\ngeq or \not\geq$           |        \ngeq or \not\geq        |
|           $\nleq or \not\leq$           |        \nleq or \not\leq        |
|                $\approx$                |             \approx             |
|                $\equiv$                 |             \equiv              |
|                                         |                                 |



# Position of the formula

## in line: 

Use **one** dollar symbol at each side of formula. \$content\ of\ formula \$ such as $x=1+2$

## new line: 

Use **two** dollar symbol at each side of formula. \$\$ content\ of\ formula\$\$

Such as: 
$$
x = 1+2
$$
by the way if you use Typora to edit MD document you can use hot key(Ctrl+shift+m) to have a new line formula quickly.



# Superscript and subscript and their combinations
| math expression | LaTeX code  |
| :-------------: | :---------: |
| [**Sup & sub script**](# Superscript and subscript and their combinations) |                                 |
|                            $x^2$                             |               x^2               |
|                            $x_n$                             |               x_n               |
| $x_{1}+x_2^2+x^3_3+\cdots+x_{i-1}^{i-1}+x^i_i+x_{i+1}^{i+1}+\cdots+x^n_n$ | x_{1}+x_2^2+x^3_3+\cdots+x_{i-1}^{i-1}+x^i_i+x_{i+1}^{i+1}+\cdots+x^n_n |



## Superscript:

**Symbol:	**'^' such as:$x^2$

## Subscript:

**Symbol:	**'_' such as: $x_1$

## Their combinations:

**Symbol:	**'{}' such as: $x_{1}+x_2^2+x^3_3+\cdots+x_{i-1}^{i-1}+x^i_i+x_{i+1}^{i+1}+\cdots+x^n_n$

Observe above formula carefully you will see that the order of symbol '_' and '^' is doesn't matter. 

# Placeholder

| math expression | LaTeX code |
| --------------- | ---------- |
|             **Placeholder**             |                                 |
|              $x \qquad y$               |           x \qquad y            |
|               $x \quad y$               |            x \quad y            |
|                 $x \ y$                 |              x \ y              |




## Biggest space:

**Symbol:	**'\qquad' such as  $x \qquad y$

## Mid space:

**Symbol:	**'\quad' such as $x \quad y$

## Smallest space:

**Symbol:	**'\' such as $x \ y$

# Basic operations
| math expression | LaTeX code |
| --------------- | ---------- |
|          **Basic operations**           |                                 |
|                 $a+b-c$                 |              a+b-c              |
|           $\times \cdot \ast$           |        \times \cdot \ast        |
|               $a\div{b}$                |            a\div{b}             |
|              $\frac{a}{b}$              |           \frac{a}{b}           |
|               $\sqrt{a}$                |            \sqrt{a}             |
|              $\sqrt[3]{8}$              |           \sqrt[3]{8}           |
|                 $\log$                  |              \log               |
|                $a\pm{b}$                |             a\pm{b}             |
|                $\cdots$                 |             \cdots              |


**Plus:	** "+" 

**Minus:	** "-" 

**Multi:	** "*" 

**Divide:	** "/div{}" 

**Fraction:	** "/frac{}{}" 

**Root:	** "/sqrt{}" 

**Plus and minus:	** "/pm{}" 

**Dots:	** "/cdots{}" 

# Trigonometric functions
| math expression | LaTeX code |
| --------------- | ---------- |
|       **Trigonometric functions**       |                                 |
|             $\sin{\theta}$              |          \sin{\theta}           |
|             $\cos{\theta}$              |          \cos{\theta}           |
|             $\tan{\theta}$              |          \tan{\theta}           |
|             $\cot{\theta}$              |          \cot{\theta}           |

# Vector, accumulate, multiply, limit
| math expression | LaTeX code |
| --------------- | ---------- |
| **Vector, accumulate, multiply, limit** |                                 |
|                $\vec{F}$                |             \vec{F}             |
|               $\sum_{a}$                |             \sum{a}             |
|               $\prod{a}$                |            \prod{a}             |
|                 $\int$                  |              \int               |
# Relational operator
| math expression | LaTeX code |
| :-------------: | :--------: |
|         **relational operator**         |                                 |
|                 $\leq$                  |              \leq               |
|                 $\geq$                  |              \geq               |
|                  $\gt$                  |               \gt               |
|                  $\lt$                  |               \lt               |
|                   $=$                   |                =                |
|                 $\neq$                  |              \neq               |
|           $\ngeq or \not\geq$           |        \ngeq or \not\geq        |
|           $\nleq or \not\leq$           |        \nleq or \not\leq        |
|                $\approx$                |             \approx             |
|                $\equiv$                 |             \equiv              |

# Greek alphabet

| math expression | LaTeX code  |
| :-------------: | :---------: |
|    $\alpha$     |   \alpha    |
|     $\beta$     |    \beta    |
|    $\gamma$     |   \gamma    |
|    $\delta$     |   \delta    |
|   $\epsilon$    |  \epsilon   |
|  $\varepsilon$  | \varepsilon |
|     $\eta$      |    \eta     |
|    $\theta$     |   \theta    |
|    $\kappa$     |   \kappa    |
|     $\iota$     |    \iota    |
|     $\zeta$     |    \zeta    |
|    $\lambda$    |   \lambda   |
|      $\mu$      |     \mu     |
|     $\phi$      |    \phi     |
|      $\pi$      |     \pi     |
|     $\rho$      |    \rho     |
|      $\xi$      |     \xi     |
|      $\nu$      |     \nu     |
|   $\upsilon$    |  \upsilon   |
|    $\varphi$    |   \varphi   |
|     $\chi$      |    \chi     |
|     $\psi$      |    \psi     |
|    $\omega$     |   \omega    |

