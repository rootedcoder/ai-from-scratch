# Phase 1 — Math Foundations — Notes

Detailed lesson notes for Phase 1. Append one entry per completed topic.

---

## 1.1.1 — Variables, Expressions, Solving for x

**Concept:** A variable is an unknown placeholder (like `let x` in JS). An expression combines numbers, variables, and operations into a "recipe" that produces a value once the variable is known. An equation states two expressions are equal; solving means finding the value of x that makes the statement true. Core rule: whatever operation is applied to one side of the equation must be applied to the other, to keep it balanced.

**Worked example:** Solve `2x + 3 = 11`.
- Subtract 3 from both sides: `2x = 8`
- Divide both sides by 2: `x = 4`
- Check by substitution: `2(4) + 3 = 11` ✓

**Code mapping:** There's no direct "solve" equivalent in code — this is manual symbolic manipulation done before any code exists. The *verification* step maps directly to a boolean check:
```javascript
const x = 4;
console.log(2 * x + 3 === 11); // true
```

**Practice results (all correct, verified in JS):**
- `3x - 5 = 16` → x = 7
- `x/4 + 2 = 9` → x = 28
- `5(x - 1) = 20` → x = 5

**Gotcha:** The divisibility of the constant term by the multiplier tells you in advance whether the answer will be a whole number or a fraction — worth eyeballing before solving. E.g. `5(x-1) = 22` would have produced x = 5.4 instead of a clean integer.

**End-goal link:** Every ML model is fundamentally an equation with unknowns (called *weights*, introduced formally in Phase 3). Training a model is solving for those unknowns — just with millions of variables instead of one, and using calculus (gradient descent) instead of algebra to do it at that scale. This lesson is the atomic unit everything else in the curriculum builds on.

→ repo: no direct match confirmed in `phases/01-math-foundations/`. The repo's lesson `01-linear-algebra-intuition` was checked directly (content reviewed 2026-07-04) and covers vectors/matrices/dot products/rank — that maps to our 1.3, not 1.1. No basic-algebra-specific lesson confirmed yet; check `aiengineeringfromscratch.com/catalog.html` when this phase's other lessons are reviewed.

---

## 1.1.2 — Functions: what f(x) means, domain, range

**Concept:** A function is a rule that takes an input and produces exactly one output — the same idea as `function f(x) { return ... }` in JS, just terser notation. `f(x) = 2x + 3` means "double the input, add 3." The **domain** is the set of valid inputs; the **range** is the set of possible outputs. These become critical later — e.g. probabilities must live in range `[0, 1]`, which is *why* activation functions like sigmoid/softmax exist instead of using raw unconstrained numbers.

**Worked example:** `f(x) = 2x + 3` → `f(4) = 11`, `f(0) = 3`, `f(-1) = 1`. Domain and range both "all real numbers" (straight line, unrestricted). Contrast: `g(x) = 1/x` has domain = all reals except 0 (undefined at x=0, division by zero).

**Code:** Python, not JS, from this point forward (correction made mid-session — Phase 0 set up a Python/Jupyter environment specifically; "from scratch" means raw Python/NumPy). File: `phase1-math/1_1_functions.py`.

```python
def g(x):
    return 1 / x

def h(x):
    return x**2 - 4

if __name__ == "__main__":
    print(g(0))
    print(h(2))
    print(h(-2))
    print(h(0))
```

**Practice results:**
- Predicted `g(0)` would throw some kind of runtime error (reasoning from JS `Infinity` vs Java behavior) — correct. Python raises `ZeroDivisionError: division by zero`, unlike JS which silently returns `Infinity`. First real Python-vs-JS behavioral gap encountered.
- `h(2) = 0`, `h(-2) = 0` — correctly reasoned that squaring a negative gives a positive.
- `h(0) = -4` — correctly distinguished from `1**0 = 1` (any nonzero number to the power 0 is 1 — separate rule, revisited properly in 1.1.4 exponents/logs).
- Correctly identified exactly two x-values (2 and -2) satisfy `h(x) = 0` — introduced as the **roots** (or zeros) of the function. A quadratic can have 0, 1, or 2 real roots depending on shape (ties into graphing, upcoming).

**Traceback reading (new skill, first exposure):** Python tracebacks read bottom-to-top for root cause, then the frames above show the call chain top-to-bottom. Bottom line = error type + message. Line above = exact failing code. Line above that = the call site that triggered it. Same pattern holds no matter how deep the stack gets.

**Gotcha:** JS's `1/0 === Infinity` (silent) vs Python's `ZeroDivisionError` (loud, crashes unless caught) is a real behavioral difference to carry forward — not just a syntax difference.

**End-goal link:** This ZeroDivisionError is a preview of real production concerns — a model-serving endpoint must validate inputs so a malformed request (e.g. a zero in the wrong place) doesn't crash the whole service. Same failure shape, much later payoff (Phase 11).

→ repo: no direct match confirmed — `01-linear-algebra-intuition` (the only Phase 1 lesson reviewed so far) covers vectors/matrices, not functions/domain/range. Check catalog for the correct lesson when reached.

---

## 1.1.3 — Graphing Lines: Slope, Intercept (y = mx + b)

**Concept:** `y = mx + b` generalizes the line seen in 1.1.2 (`f(x) = 2x + 3`, which is m=2, b=3). `m` (slope) = rate of change of y per unit increase in x. `b` (y-intercept) = value of y when x=0. Slope between any two points: `m = (y2 - y1) / (x2 - x1)` — constant for any pair of points on the same line, not just adjacent ones.

**Worked example:** `y = 2x + 3` → table (x=0,1,2,3 → y=3,5,7,9). y increases by 2 for every +1 in x, matching m=2. Verified via slope formula on points (1,5) and (3,9): m = (9-5)/(3-1) = 2 ✓.

**Code:** `phase1-math/1_3_slope.py`
```python
def line(x, m, b):
    return m * x + b

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
```

**Practice results:**
- Generated table for m=2, b=3 across x=0..4 (extended one point beyond what was asked): 0→3, 1→5, 2→7, 3→9, 4→11.
- Verified slope using non-adjacent points (1,5) and (4,11) → slope=2.0, matches m. Stronger check than requested — confirms slope is constant across *any* two points, not just neighbors.
- Tested m=-5, b=5: y1=5, y2=0, y3=-5 — correctly decreasing as x increases, confirming negative slope behavior.
- Correctly predicted m=0 produces a horizontal line at y=b — refined to: slope is *rate of change*, so zero rate of change means y never moves regardless of x, i.e. y=b for all x (not just "passes through b" but flat everywhere).

**Gotcha:** none new this topic — mechanically straightforward given 1.1.1/1.1.2 foundation.

**End-goal link:** `y = mx + b` is the exact structural shape of linear regression (Phase 2) — `m` becomes a **weight**, `b` becomes a **bias**, and training means using data to find the best m/b automatically instead of choosing them by hand. This is the core idea Phase 1 is scaling toward: the same shape, generalized to millions of dimensions. Also flagged conceptually: a "dead" unit in a network (zero output change regardless of input) is diagnosable the same way as zero slope — no learning signal from that input.

→ repo: no direct match confirmed — same caveat as above; `01-linear-algebra-intuition` doesn't cover slope/intercept. This lesson's real content (reviewed 2026-07-04) will instead be the correct second-pass reference once we reach 1.3 (vectors, dot product, matrix multiply, projection, Gram-Schmidt) — flagged for reuse there.

---

## 1.1.4 — Exponents and Logarithms

**Concept:** An exponent `xⁿ` means "multiply x by itself n times." A logarithm is the inverse question: "what power of the base gives this number?" `log₂(16) = 4` because `2⁴ = 16`. Log undoes exponent, the same relationship as subtraction/addition or division/multiplication. Different bases exist — log₂, log₁₀, and natural log (base e, written `ln` in math, `math.log()` in Python).

**Why it matters for ML:** probabilities are always in [0,1]; multiplying many small probabilities together underflows to 0 on real hardware. `log(a×b) = log(a) + log(b)` turns multiplication into addition, which is numerically stable. This is why `log` appears in nearly every loss function starting in Phase 2 — a practical fix for a real computational problem, not stylistic.

**Worked example:** `2⁴=16` → `log₂(16)=4`. `10²=100` → `log₁₀(100)=2`. `2⁰=1` → `log₂(1)=0` for any base (ties back to `1**0=1`, first noted in 1.1.2).

**Code:** `phase1-math/1_1_4_logs.py`
```python
import math

print(math.log2(16))
print(math.log10(100))
print(math.log(1))
```

**Practice results (all correct):**
- `log2(16)=4.0`, `log10(100)=2.0`, `log(1)=0.0`
- `2**10=1024`, `log2(1024)=10.0` — confirmed exponent and log invert each other.
- Correctly predicted `math.log(0)` would raise an error before running. Actual output: `ValueError: expected a positive input` (Python 3.14's updated, more descriptive wording for what's classically called "math domain error" in older Python versions — worth knowing both phrasings exist).
- Correctly reasoned through *why* structurally: a positive base raised to any real exponent is always strictly greater than 0 — it approaches 0 as the exponent goes to -∞ but never reaches it. So 0 is outside the domain of any log function, same domain-restriction concept first introduced with `g(x)=1/x` in 1.1.2.

**Gotcha:** `ZeroDivisionError` (from `1/0`) and `ValueError` (from `log(0)`) are different exception types for related-but-distinct reasons — both are Python refusing an undefined operation, but worth being able to name which is which when debugging later. Also: exact error message wording can differ across Python versions (3.14 here is more descriptive than the classic "math domain error" phrasing seen in older references).

**End-goal link:** log-based loss functions (cross-entropy, log-likelihood) are the numerical-stability backbone of virtually every classifier and language model trained from Phase 2 onward — this lesson is the reason that machinery exists rather than just being "the way it's done."

→ repo: no confirmed match yet for exponents/logs specifically. Check `aiengineeringfromscratch.com/catalog.html` when convenient rather than guess a lesson name.

---

**Section 1.1 (Algebra) — complete.** All four lessons (variables/solving, functions, slope/intercept, exponents/logs) closed 2026-07-04. Next: 1.2 Calculus.

---

## 1.2.1 — What a Derivative Is: Rate of Change, Slope of a Curve, Numeric Intuition

**Concept:** For a straight line, slope (1.1.3) is constant everywhere. A derivative extends the same idea to curves, where the rate of change is different at every point. Zoom in close enough on any point of a smooth curve and it looks like a straight line — the derivative is the slope of that local line. Core intuition: **derivative = slope, measured locally instead of globally.**

**Why it matters for ML:** training adjusts weights to reduce error. Knowing which direction (and how much) to adjust a weight requires knowing the local slope of the error function at the current weight value — that's exactly what a derivative provides. Gradient descent (hand-built in Phase 2) is "compute local slope, step in the direction that decreases error, repeat."

**Worked example:** `f(x) = x²` at `x=3`. Using two very close points (x=3, x=3.001):
```
f(3) = 9, f(3.001) = 9.006001
m = (9.006001 - 9) / 0.001 = 6.001 ≈ 6
```
Shrinking the gap further converges toward exactly 6 — the true derivative at x=3.

**Code:** `phase1-math/2_1_derivative.py`
```python
def f(x):
    return x**2

def numeric_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h
```

**Practice results:**
- `x=3` → `6.000100000012054` ≈ 6
- `x=0` → `9.999999999999999e-05` ≈ 0
- `x=-2` → `-3.999900000000167` ≈ -4
- Pattern discovered directly from the numbers: derivative of `x²` is `2x` everywhere (the power rule, to be derived algebraically in 1.2.2).
- `h` shrinking experiment: `h=0.0001` gave error ≈ +0.0001; `h=1e-8` gave error ≈ -3.6e-8 — smaller `h` was more accurate, as expected.
- Extended reasoning (not yet run, flagged as worth trying): shrinking `h` far enough (e.g. 1e-12 to 1e-15) eventually makes accuracy *worse* rather than better, due to **catastrophic cancellation** — `f(x+h) - f(x)` becomes subtraction of two nearly-identical floats, and floating point only carries ~15-17 significant digits. Below that precision floor, the result is mostly rounding noise. Directly foreshadows curriculum topic 1.3.12 (numerical stability).
- Correctly reasoned (after one initial miss, confusing "derivative" with "solve for x") that a straight line's derivative equals its constant slope: `f(x)=2x+3` → derivative is `2` everywhere; `f(x)=5` (flat line) → derivative is `0` everywhere. Both derived by connecting back to 1.1.3's `m` concept rather than new computation.

**Gotcha:** `h` selection is a real tradeoff — too large gives a poor approximation of instantaneous slope (secant line, not tangent line); too small triggers floating-point cancellation error. There's a practical sweet spot, not a "smaller is always better" rule.

**End-goal link:** this numeric-derivative approach is literally how you'd sanity-check a hand-derived analytical gradient later (a technique called "gradient checking," common when debugging backprop by hand in Phase 3) — comparing the numeric approximation against the algebraic formula to catch implementation bugs.

→ repo: not yet checked — verify against `aiengineeringfromscratch.com/catalog.html` rather than assume a lesson name, per the correction made in section 1.1.

---

## 1.2.2 — Derivative Rules: Power Rule, Chain Rule

**Concept:** The power rule gives the exact derivative of any power of x without numeric approximation: `f(x)=xⁿ → f'(x)=n·x^(n-1)` (bring the exponent down as a multiplier, reduce exponent by 1). Confirms 1.2.1's discovered pattern: n=2 gives f'(x)=2x. The chain rule handles nested functions: `f(x)=g(h(x)) → f'(x)=g'(h(x))·h'(x)` — derivative of the outer function (evaluated at the inner function's output), times the derivative of the inner function.

**Why it matters for ML:** a neural network is a chain of nested functions (each layer feeds the next). Computing how an early-layer weight affects final error requires the chain rule applied repeatedly, layer by layer — this exact algorithm is backpropagation (Phase 3.5). The chain rule is the mathematical engine underneath it.

**Worked example (power rule):** `f(x)=x³ → f'(x)=3x²`. At x=2: f'(2)=12, confirmed numerically.

**Worked example (chain rule):** `f(x)=(2x+3)²`, outer `g(u)=u²`, inner `h(x)=2x+3`. `g'(u)=2u`, `h'(x)=2`. `f'(x)=2(2x+3)·2=8x+12`. At x=1: f'(1)=20, confirmed numerically.

**Code:** `phase1-math/1_2_2_rules.py` — generalized beyond what was asked: built `f_exponent(x, n)` and `f_exponent_derivative(x, n)` for any power n (not hardcoded to cubic), reusing `power_rule(n)` helper. Chain rule implemented by explicitly separating and multiplying the outer-derivative and inner-derivative components rather than just hardcoding the final formula.

**Practice results (all correct):**
- Power rule, x³ at x=3: exact=27, numeric≈27.0009 ✓
- Chain rule, (2x+3)² at x=3: exact=36, numeric≈36.0004 ✓
- Predicted derivative of x¹ (mechanically applying the rule: multiplier=1, new_exponent=0) = 1. Correctly connected this to 1.1.3 — f(x)=x is y=mx+b with m=1, so derivative=1 is just confirming the already-known slope.

**Gotcha:** none new — this topic was mostly a formalization/confirmation of 1.2.1's numeric findings rather than introducing new failure modes.

**End-goal link:** power rule + chain rule are the two rules that, applied together and repeatedly, constitute backpropagation. Every gradient computed in Phase 3 onward is built from exactly these two mechanisms, just applied at much larger scale (many nested layers, many variables) — nothing conceptually new happens between here and hand-deriving backprop, only more bookkeeping.

→ repo: not yet checked — verify against catalog when reached.

---

## 1.2.3 — Partial Derivatives: Multi-Variable Functions

**Concept:** For functions of multiple variables (`f(x,y)`), a partial derivative asks "how does f change if I nudge one variable, freezing all others?" Notation: `∂f/∂x`. Mechanics: treat every other variable as a plain constant, then apply the same single-variable rules already known (power rule etc.) to the variable being differentiated.

**Why it matters for ML:** a model with a million weights is a function of a million variables. Training requires knowing how error changes with respect to each individual weight, one at a time, holding the rest fixed — that's a partial derivative, computed once per weight. 1.2.4 (gradients) is just "collect all partials into one list."

**Worked example:** `f(x,y)=x²+y²`. `∂f/∂x`: treat y² as a constant (derivative 0), x² gives 2x via power rule → `∂f/∂x=2x`. Symmetric: `∂f/∂y=2y`. Verified numerically at (3,4): nudging only x gives ≈6, matching 2(3)=6.

**Code:** `phase1-math/1_2_3_partials.py` — generalized `f(x,y,n)=xⁿ+yⁿ` with parameterized exponent, reused across the discovery exercise and the three-variable extension.

**Practice results (all correct):**
- `f(x,y)=x²+y²` at (3,4): ∂f/∂x≈6.0001 (matches 2x=6), ∂f/∂y≈8.0001 (matches 2y=8).
- `f(x,y)=x·y` at (3,4): ∂f/∂x≈4.0000 (matches y=4), ∂f/∂y≈3.0000 (matches x=3). Pattern: the two variables swap places in each other's partial — when y is held constant, x·y is "constant times x," whose derivative is just the constant. This is the seed of the **product rule** (not formally in the curriculum's named-rules list, but self-discovered here through direct experimentation).
- `f(x,y,z)=x²+y²+z²` at (3,4,5): all three partials correct (6.0001, 8.0001, 10.0001) — correctly reasoned each partial depends only on its own variable, since squared terms in different variables don't interact under single-variable differentiation.

**Gotcha:** none new — extends 1.2.1/1.2.2 mechanically rather than introducing new numerical pitfalls.

**End-goal link:** this is the exact atomic operation used millions of times over during real model training — one partial derivative per weight, per training step. 1.2.4 (gradients) packages these into a single vector; that vector is what "gradient descent" descends along.

→ repo: not yet checked — verify against catalog when reached.

---

## 1.2.4 — Gradients: Vector of Partial Derivatives, Gradient Descent

**Concept:** A gradient collects all partial derivatives of a function into one list: `∇f(x,y) = [∂f/∂x, ∂f/∂y]`. The gradient points in the direction of steepest *increase*. Moving opposite the gradient decreases the function fastest — that single idea, applied repeatedly in small steps, **is gradient descent** in its entirety.

**Why it matters for ML:** a model's error is a function of its weights. The gradient tells you, for every weight simultaneously, which direction increases error; stepping the opposite way, repeatedly, is the entire training loop before any engineering (batching, optimizers, schedules — Phase 2-3) is layered on.

**Worked example:** `f(x,y)=x²+y²` at (3,4): `∇f=[6,8]`. Moving opposite (toward `[-6,-8]` direction) moves x,y toward 0, which is the function's minimum — consistent with intuition.

**Code:** `phase1-math/1_2_4_gradient.py`
```python
def gradient(x, y, n, h=0.0001):
    df_dx = (f(x + h, y, n) - f(x, y, n)) / h
    df_dy = (f(x, y + h, n) - f(x, y, n)) / h
    return [df_dx, df_dy]

def gradient_step(x, y, n, learning_rate=0.01, h=0.0001):
    grad = gradient(x, y, n, h)
    new_x = x - learning_rate * grad[0]
    new_y = y - learning_rate * grad[1]
    return new_x, new_y
```

**Practice results:**
- `∇f(3,4) = [6.0001, 8.0001]` ✓ matches [2x,2y].
- One `gradient_step`: (3,4)→(2.94, 3.92), confirmed by hand (3 - 0.01×6 = 2.94, etc.)
- **50-step loop** (first Python `for`/`range` usage, translated directly from JS `for` loop syntax; also first use of modulo for "every 10th step" printing and Python's tuple-unpacking `x, y = gradient_step(...)`): x,y shrank monotonically from (3,4) toward 0; f(x,y) fell 25→24.0→16.0→10.7→7.1→4.8 over 50 steps. Correctly observed the step size decelerating near the minimum — explained by the gradient itself shrinking as x,y shrink (gradient=[2x,2y], smaller x,y → smaller gradient → smaller steps). Directly previews why training loss curves flatten near convergence rather than dropping linearly.

**Gotcha:** none new numerically — the main new material was Python control flow (loops, modulo, tuple unpacking), not math.

**End-goal link:** this is the complete conceptual mechanism of neural network training, seen end-to-end for the first time: compute gradient → step opposite it → repeat → watch loss fall. Phases 2-3 add engineering on top (real datasets, many more parameters, smarter step sizing) but introduce no new core idea beyond what was just run here on a 2-variable toy function.

**Milestone:** closes the numeric-calculus arc (1.2.1→1.2.4) — derivative, rules, partial derivatives, and gradient descent now form one continuous, hands-on-verified thread. 1.2.5 (optimization) and 1.2.6 (convexity) formalize what was just observed empirically.

→ repo: not yet checked — verify against catalog when reached.

---

## 1.2.5 — Optimization: Minimizing a Function, Why We Move Against the Gradient

**Concept:** ML "optimization" almost always means minimizing a loss function — the formal name for the error function informally used since 1.2.3/1.2.4. "Move opposite the gradient" isn't a rule to memorize: the gradient points toward steepest *increase* by definition, so its exact opposite is the direction of steepest *decrease*. New idea this lesson: **local minimum vs global minimum** — gradient descent only sees the local slope at the current point, so on a bumpy (non-bowl-shaped) loss surface, where you start can determine which minimum you end up in.

**Worked example:** `f(x) = x⁴ - 4x²` — a "double valley" shape with two symmetric minima at `x=±√2≈±1.41421`, and a local *maximum* (small hill) at `x=0` between them.

**Code:** `phase1-math/2_5_optimization.py`
```python
def f(x):
    return x**4 - 4 * x**2

def derivative(x, h=0.0001):
    return (f(x + h) - f(x)) / h

def gradient_descent_1d(x_start, steps=100, learning_rate=0.01):
    x = x_start
    for step in range(steps):
        grad = derivative(x)
        x = x - learning_rate * grad
    return x
```

**Debugging note (real, self-caught):** initial version had `return x` indented one level too deep (inside the `for` loop instead of after it), causing the function to exit after exactly 1 step every time — a concrete example of Python's indentation-as-syntax rule silently changing program behavior rather than erroring. Fixed by dedenting `return x` to align with `for`, not the loop body.

**Practice results (100 real steps, after the fix):**
- `x_start=1.5 → 1.41416`, `x_start=-1.5 → -1.41426` — both essentially fully converged to the two separate valleys (±√2), confirming starting point determines which local minimum is reached.
- `x_start=0.01 → 1.4127` — nearly fully converged into the positive valley. Started right next to the unstable local max at x=0, where the gradient is nearly zero (a **plateau**), causing very slow initial movement — but 100 real steps was enough time to escape the plateau and almost fully converge. Key correction made during this lesson: an earlier (bugged, single-step) run made it look like this point barely moves at all; the fully-run version shows the plateau only *delays* convergence, it doesn't prevent it.
- `x_start=0 → 0.1096` — starting exactly at the theoretical zero-slope point (`f'(0)=0` exactly, in true math). In practice, the numeric derivative (finite-difference approximation, h=0.0001) isn't perfectly zero due to floating-point rounding — introduces this as an **unstable equilibrium**: theoretically balanced, but any infinitesimal perturbation (here, numerical noise rather than a deliberate one) causes eventual departure. Over 100 compounding steps, that tiny initial nudge grew into real, visible movement (0.1096), though still far from fully converged by step 100.

**Gotcha:** re-confirms 1.2.1's floating-point precision theme, but now shows it actively *driving* real behavior (breaking a symmetric equilibrium) rather than just being a source of small numeric error to tolerate.

**End-goal link:** local minima, plateaus, and unstable equilibria are not toy-problem curiosities — they are real, named phenomena in deep learning training (loss landscapes are extremely bumpy at real scale). This lesson is the first hands-on encounter with why training isn't a guaranteed, single-path process, and why initialization (Phase 3.9, weight initialization) matters — where you start really can determine where you end up.

**Session note:** learner asked for a conceptual detour before this lesson, questioning why slope → derivative → partial derivative → gradient were each necessary rather than arbitrary rules to accept. Addressed by reframing all four as one continuous question ("which way and how much to turn a knob") asked at increasing scope: single static case (slope) → varies by position (derivative) → multiple knobs individually (partial derivative) → all knobs simultaneously (gradient). Reinforced that every step so far has been numerically self-verified in the learner's own code, not asserted as theorem.

→ repo: not yet checked — verify against catalog when reached.

---

## 1.2.6 — Convex vs Non-Convex Functions

**Concept:** A function is convex if it has exactly one minimum and never dips-rises-dips again — equivalently, a straight line connecting any two points on the curve always lies on or above the curve. Non-convex functions have multiple local minima, saddle points, or plateaus. No new code — this lesson named the distinction between the two shapes already built and run in 1.2.4 (`x²+y²`, convex, always converges to (0,0)) and 1.2.5 (`x⁴-4x²`, non-convex, two valleys, starting point determines outcome).

**Why it matters for ML:** convex loss functions (e.g. linear regression, Phase 2.2) guarantee gradient descent finds the single best answer regardless of starting point. Neural network loss surfaces (Phase 3+) are almost never convex — vast numbers of local minima, saddle points, plateaus. This is the direct, practical reason careful weight initialization (3.9), momentum/adaptive optimizers like Adam (3.7), and run-to-run training variance all exist — none of it is arbitrary engineering, it's a response to non-convexity.

**Conceptual exercises (no code, reasoning only):**
1. `f(x)=3x+5` (straight line): correctly identified as convex — the connecting segment between any two points lies exactly *on* the line, satisfying the "on or above" test as the boundary/degenerate case. Correctly connected to constant slope (always 3) meaning no bowl or hill curvature at all.
2. `f(x)=-x²` (upside-down bowl): correctly recognized gradient descent minimizing this is mismatched (it hunts for a minimum, this function has none). One correction made: this function doesn't have "endpoints" to settle at — it's unbounded below, so minimizing it causes gradient descent to diverge toward -∞ in whichever direction it initially drifts, never converging. Correctly proposed the fix: gradient ascent (same mechanism, move *with* the gradient) to find the actual maximum at x=0.
3. End-goal connection: correctly concluded the learner's own planned models (game generation, coding assistant, 3D generation) will have non-convex loss landscapes. One phrasing corrected: gradients are always locally *accurate* — non-convexity isn't a correctness problem, it's a visibility problem (the gradient has no knowledge of whether a better valley exists elsewhere on the loss surface). Framed as "the compass is accurate, but only sees your immediate surroundings, not the whole map."

**Gotcha:** distinguishing "gradient is locally correct but globally shortsighted" from "gradient can be wrong" — an easy conceptual conflation worth being precise about, since it recurs throughout deep learning (e.g. why multiple training runs of the same architecture can converge to different final performance).

**End-goal link:** every model planned for the Jarvis platform will train on non-convex loss surfaces. Practically, this means: training runs won't be perfectly reproducible run-to-run without fixing random seeds, initialization strategy will matter more than it would for convex problems, and reaching "a good local minimum" rather than "the provably best possible one" is the realistic, expected outcome — not a sign of a bug.

**Milestone: Section 1.2 (Calculus) — complete.** Six lessons (derivative intuition → power/chain rules → partial derivatives → gradients → optimization → convexity) form one continuous, entirely self-verified arc, from first numeric slope approximation through to a full conceptual understanding of why neural network training behaves the way it does. Next: 1.3 (Linear Algebra) — this is also where the previously-reviewed real repo lesson (`phases/01-math-foundations/01-linear-algebra-intuition`, covering vectors/matrices/dot products/rank/projection/Gram-Schmidt) becomes a genuinely relevant second-pass reference, having been confirmed by actually reading its content earlier in this project.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — confirmed relevant for 1.3, not for 1.2. No confirmed match found for calculus-specific lessons in this phase; check catalog if a dedicated one is wanted.

---

## 1.3.1 — Vectors: What They Are, Addition, Scaling, Geometric Intuition

**Concept:** A vector is an ordered list of numbers representing magnitude and direction — geometrically, an arrow from the origin to a coordinate. Already encountered implicitly in 1.2.4 (the gradient `[6,8]` was a vector). Two core operations: **addition** (add corresponding elements; geometrically, place the second arrow's tail at the first arrow's tip) and **scalar multiplication** (multiply every element by one number; geometrically, stretches/shrinks/flips the arrow's length without changing its line of direction unless the scalar is negative).

**Why it matters for ML:** weights, inputs, and gradients in a neural network are vectors — lists of many numbers treated as one object. Vector addition/scaling/dot-product (next lesson) are the actual operations run across a whole layer at once. This is also why NumPy exists and is permitted under the from-scratch rule: it's fast vector arithmetic, and vectors are the real unit neural networks compute with.

**Worked example:** `v1=[3,4]`, `v2=[1,2]`. Addition: `[4,6]`. Scaling `3×v1=[9,12]` (same direction, 3x length). Negative scaling `-1×v1=[-3,-4]` (opposite direction, same length).

**Code:** `phase1-math/1_3_1_vectors.py` — first use of Python list comprehensions:
```python
def vector_add(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_scale(v, scalar):
    return [scalar * x for x in v]
```
Framed against JS: `[... for i in range(len(v1))]` is roughly `v1.map((val,i) => val + v2[i])` — same idea (transform each element), Python syntax built into the language core rather than a method call. Also noted: raw Python `+` on lists concatenates rather than adds element-wise (`[3,4]+[1,2] → [3,4,1,2]`), which is why explicit functions are needed before NumPy is introduced later.

**Practice results (all correct, used own vectors [3,2] and [1,4] rather than the worked example's):**
- `[3,2]+[1,4] = [4,6]`
- `3×[3,2] = [9,6]`
- `-1×[3,2] = [-3,-2]` — correctly reasoned as a direction flip.
- `0×[3,2] = [0,0]` — the **zero vector**: zero magnitude means no direction at all.
- First linear combination, by hand and in code: `2×[1,1] + 3×[2,0] = [2,2]+[6,0] = [8,2]`, matching printed output exactly.

**Gotcha:** raw Python list `+` is concatenation, not element-wise addition — an easy trap coming from JS/math intuition, addressed proactively before it caused confusion.

**End-goal link:** a linear combination (scale several vectors independently, then sum) is *exactly* what a single neuron computes: `weight1×input1 + weight2×input2 + ...`. The `2×[1,1]+3×[2,0]` exercise is, structurally, identical to a tiny 2-input neuron's weighted sum — first direct, concrete bridge from linear algebra mechanics to an actual neural network operation.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — now genuinely relevant; content previously reviewed covers vectors directly. Worth reading as second pass.

---

## 1.3.2 — Dot Product: Arithmetic and Geometric Meaning

**Concept:** The dot product multiplies corresponding elements of two equal-length vectors and sums the results into a single scalar: `[a1,a2]·[b1,b2] = a1×b1 + a2×b2`. Unlike vector addition/scaling (1.3.1), the output is a number, not a vector.

**Why it matters for ML:** this is the exact operation a single neuron performs — `[input1,input2,...]·[weight1,weight2,...]` — before an activation function (Phase 3.3) is applied on top. Also has a geometric meaning via `a·b = |a||b|cos(θ)`: same direction → large positive, perpendicular → exactly zero, opposite direction → large negative. This is the mathematical basis for measuring similarity between vectors — word/document embeddings (5B.3, 8.2) use dot products (or cosine similarity, a normalized version) to quantify "how similar are these two things."

**Worked example:** `[3,4]·[1,2] = 3+8 = 11`. Opposite-direction check: `[3,4]·[-3,-4] = -9-16 = -25` (strongly negative). Perpendicular check: `[3,4]·[4,-3] = 12-12 = 0` (exactly zero — rotating a vector 90° via the swap-and-negate trick).

**Code:** `phase1-math/1_3_2_dot_product.py` — first use of a generator expression:
```python
def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))
```
Framed against JS: roughly `v1.map((val,i)=>val*v2[i]).reduce((a,b)=>a+b)`, but Python feeds values directly into `sum()` without materializing an intermediate list — more memory-efficient for large vectors, relevant later at real model scale.

**Practice results (all correct):**
- `[3,4]·[1,2]=11`, `[3,4]·[-3,-4]=-25`, `[3,4]·[4,-3]=0` — all confirmed the angle-based intuition.
- Own 3D example, `[10,15,20]·[12.5,17.5,22.5]=837.5` — vectors weren't perfectly proportional but shared the same-sign components throughout, still confirming "roughly similar direction → strongly positive."
- Conceptual question (dot product vs. linear combination): correctly identified scalar-vs-vector output as the key distinction. Refined further: a dot product has the same multiply-then-sum shape as a linear combination, but the scaling weights come from the other vector's own components rather than being externally chosen constants — a close structural cousin, not an unrelated operation.

**Gotcha:** none new — mechanically straightforward given 1.3.1's foundation; the generator-expression syntax is the only new Python surface area.

**End-goal link:** every neuron's forward pass, at its core, is one dot product plus a bias plus an activation function. This is also the literal mechanism behind semantic search and retrieval (Phase 8.2/8.4, RAG) — comparing a query embedding against document embeddings via dot product/cosine similarity to find the most relevant matches.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers dot products directly per prior review.

---
