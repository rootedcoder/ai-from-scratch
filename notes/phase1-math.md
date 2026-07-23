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

## 1.3.3 — Matrices: What They Represent, Shapes, Notation

**Concept:** A matrix is a 2D grid of numbers — rows and columns — describable as a list of vectors stacked together. Shape is `rows × columns`; a `2×3` matrix ≠ a `3×2` matrix even with rearranged values. Entries addressed by `(row, col)`.

**Why it matters for ML:** a single neuron's weights are a vector (1.3.1/1.3.2). A whole layer of neurons (multiple neurons, same inputs) stacks their weight vectors into a matrix — one row per neuron. Every layer in a real network is fundamentally a weight matrix; matrix operations (starting 1.3.4) let a whole layer's computation happen in one operation instead of looping neuron-by-neuron.

**Worked example:** a tiny 2-neuron layer, each looking at 3 inputs:
```
W = [ 0.1  0.2  0.3 ]   ← neuron 1's weights
    [ 0.4  0.5  0.6 ]   ← neuron 2's weights
```
Shape: `2×3` (2 neurons/rows, 3 weights/columns each).

**Code:** `phase1-math/1_3_3_matrices.py` — matrix represented as a list of lists (pre-NumPy).
```python
def matrix_shape(M):
    rows = len(M)
    columns = len(M[0])
    return rows, columns

def get_row(M, i):
    return M[i]

def get_column(M, j):
    return [M[i][j] for i in range(len(M))]
```

**Practice results (all correct):**
- `matrix_shape(W) = (2, 3)` ✓
- `get_row(W, 0) = [0.1, 0.2, 0.3]` ✓
- `get_column(W, 1) = [0.2, 0.5]` ✓ (Python 0-indexed second column). Function logic verified correct in general (comprehension walks every row at fixed column index j).
- Correctly predicted: transposing a `2×3` matrix produces a `3×2` matrix (rows/columns swap counts).

**Gotcha (tutor-side, noted for accuracy):** the lesson's worked example used 1-indexed math column language ("Column 1", "Column 2"...) while the exercise instructions referenced a 0-indexed Python column target — an internal inconsistency introduced by the tutor, not a learner error. Resolved by confirming the `get_column` function's correctness directly rather than requiring a specific index re-run. Worth remembering going forward: default to Python's 0-indexing consistently in exercise instructions from here on.

**End-goal link:** matrices are the actual data structure holding every layer's weights in every model in the Jarvis platform. 1.3.4 (matrix-vector multiplication) is where this stops being just storage and becomes the mechanism for computing a whole layer's output in one operation.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers matrices per prior review.

---

## 1.3.4 — Matrix-Vector Multiplication: By Hand on a 2×2 Example

**Concept:** Multiplying a matrix `M` by a vector `v` produces a new vector, where each entry is the dot product (1.3.2) of one row of `M` with `v`. Mechanically: one dot product per row, collected into a new vector. Requires `M`'s column count to match `v`'s length (formal reasoning why deferred to 1.3.5).

**Why it matters for ML:** for a weight matrix `W` (2 neurons × 3 inputs, from 1.3.3) and input vector `x` (3 values), `W·x` computes *both* neurons' outputs simultaneously — row 1 dotted with x gives neuron 1's output, row 2 gives neuron 2's output. No loop over neurons needed. This is the exact operation inside every forward pass of every layer in every network built from Phase 3 onward.

**Worked example:** `M=[[2,1],[0,4]]`, `v=[3,5]`. Row 1: `[2,1]·[3,5]=6+5=11`. Row 2: `[0,4]·[3,5]=0+20=20`. Result: `[11,20]`.

**Code:** `phase1-math/1_3_4_matrix_vector.py` (dot_product/get_row reimplemented inline rather than imported — first mention of Python `import`/`from...import` syntax, deferred as unnecessary until codebase grows):
```python
def matrix_vector_multiply(M, v):
    return [vector_dot_product(get_row(M, i), v) for i in range(len(M))]
```

**Practice results (all correct):**
- `M·v = [11, 20]` — matches worked example.
- `W·x` for `W=[[0.1,0.2,0.3],[0.4,0.5,0.6]]`, `x=[1,2,3]` → `[1.4, 3.1999999999999997]`. Hand-computed first: row1=0.1+0.4+0.9=1.4, row2=0.4+1.0+1.8=3.2 — trailing digits are the same floating-point representation quirk seen in earlier lessons (3.2 isn't exactly representable in binary float), not a bug.
- **Shape-mismatch prediction — notably strong, independent reasoning:** correctly distinguished two different failure modes based on which vector's length drives `vector_dot_product`'s internal loop (`range(len(v1))`, where `v1` is always the matrix row):
  - `M` is `2×2` (rows length 2), `v` has length 3 → loop only reaches indices 0,1 of `v`; `v[2]` is silently never accessed. No error, silently incomplete/wrong result.
  - `M` is `4×4` (rows length 4), `v` has length 3 → loop tries to reach index 3 of `v`, which doesn't exist → `IndexError`.
  Both predicted correctly before running, with accurate reasoning about the *mechanism* (not just the outcome) — a genuinely subtle point about how the same category of shape mismatch can fail silently or loudly depending on implementation direction.

**Gotcha:** silent failure (Case 1 above) is more dangerous than a loud error (Case 2) precisely because nothing signals anything went wrong — a real category of bug to watch for once real matrix/vector shapes get large and errors aren't visually obvious.

**End-goal link:** this is literally the forward-pass computation for one layer of a neural network, computed by hand for the first time. 1.3.5 (matrix-matrix multiplication) extends this from "one input vector" to "a whole batch of inputs at once" — the actual training-time operation.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers matrix-vector operations per prior review.

---

## 1.3.5 — Matrix-Matrix Multiplication: By Hand, Why the Shapes Must Match

**Concept:** Matrix-matrix multiplication is matrix-vector multiplication extended to a whole batch of vectors at once — stack input vectors as columns of a second matrix. `result[i][j] = row i of A · column j of B`. Shape rule follows directly from dot product's equal-length requirement (1.3.2): row i of A has length = A's column count; column j of B has length = B's row count; these must match for the dot product to be defined. Stated precisely: `(m×n)·(n×p) = (m×p)` — inner dimensions must match, outer dimensions become the result shape.

**Why it matters for ML:** `W` (neurons × inputs) times `X` (inputs × batch_size) gives every neuron's output for every batch example in one operation — the actual computation GPUs are optimized for, and the reason "shape mismatch" errors are extremely common once real models are built (Phase 3+).

**Worked example:** `A=[[1,2],[3,4]]`, `B=[[5,6],[7,8]]`, both 2×2. `A·B=[[19,22],[43,50]]` (each entry a row·column dot product).

**Code:** `phase1-math/1_3_5_matrix_matrix.py`
```python
def matrix_multiply(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    if len(A[0]) != len(B):
        return "Error: Number of columns in A must equal number of rows in B..."
    result = []
    for i in range(rows_A):
        row_result = []
        for j in range(cols_B):
            row_result.append(dot_product(get_row(A, i), get_column(B, j)))
        result.append(row_result)
    return result
```
Notably added the shape-validation guard **without being asked** — independently arrived at the same defensive-programming pattern real ML frameworks use (raising a clear shape-mismatch error rather than letting execution fail deep inside with a confusing low-level exception).

**Practice results (all correct):**
- `A·B = [[19,22],[43,50]]` ✓
- `W(2×3)·X(3×2) = [[1.4,3.2],[3.2,7.7]]` — first full mini-batch forward pass by hand and code; correctly interpreted result shape (2×2) as "2 neurons × 2 batch examples," e.g. result[1][1]=7.7 is neuron 2's output for batch example 2.
- Mismatch test: with validation, correctly caught `2×3`×`2×3` (inner dims 3≠2) and returned a custom error message. With validation removed, correctly predicted and confirmed `IndexError: list index out of range` — traced the exact mechanism: dot_product loops `range(len(row))` where row length is 3 (from W's columns), but each column of the mismatched second matrix only has length 2, so index 2 doesn't exist.

**Gotcha:** none new mechanically — this topic's real lesson was as much about defensive input validation as about the matrix math itself.

**End-goal link:** this is the literal batch forward-pass computation used in every real training step from Phase 2 onward — one matrix multiplication computing every neuron's output for every example in a batch simultaneously. The self-added validation pattern previews Phase 3.13 (debugging neural networks) and general production practices (Phase 11) where clear error messages at shape-mismatch boundaries save significant debugging time.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers matrix multiplication per prior review.

---

## 1.3.6 — Matrix Transformations & Eigenvalues: What a Matrix "Does" to Space

**Concept:** A matrix can be understood geometrically as a transformation of space — `M·v` moves `v` according to the matrix's rule (stretch, rotate, reflect, etc.). An **eigenvector** is a special vector whose direction a matrix doesn't change, only its length (or it flips exactly opposite): `M·v = λ·v`. The scalar `λ` is the **eigenvalue** — how much that direction gets stretched/shrunk. Most vectors get genuinely redirected by a matrix; eigenvectors are the rare exceptions that only get scaled.

**Clarified during session (worth keeping as reference):** the identity matrix is a degenerate example — every vector is an eigenvector of `I` with `λ=1`, since `I` changes nothing. Not the general case, just the simplest possible one.

**Why it matters for ML:** eigenvectors/eigenvalues underlie PCA (1.3.10, finding the most important directions of variation in data) and explain why repeated matrix multiplication in deep networks can cause values to explode (large eigenvalues) or vanish (small eigenvalues) — directly connects to 1.3.12 (numerical stability) and the real Phase 3 problem of vanishing/exploding gradients.

**Worked example:** `M=[[2,0],[0,1]]`. `[1,0]` → `[2,0]` = `2×[1,0]`, eigenvector, λ=2. `[0,1]` → `[0,1]` = `1×[0,1]`, eigenvector, λ=1. `[1,1]` → `[2,1]`, direction genuinely changed, not an eigenvector.

**Code:** `phase1-math/1_3_6_eigen.py`
```python
def check_eigenvector(M, v):
    result = matrix_vector_multiply(M, v)
    ratios = [result[i] / v[i] for i in range(len(v)) if v[i] != 0]
    if all(abs(r - ratios[0]) < 1e-9 for r in ratios):
        return True, ratios[0]
    return False, None
```

**Extended line-by-line discussion (significant portion of this session), each resolved before continuing:**
- List comprehension `if v[i] != 0` clarified as a *filter* — skips (never computes) the expression for indices where the condition is false, preventing division by zero, distinguished from a general transform.
- `all(abs(r - ratios[0]) < 1e-9 for r in ratios)` broken into three layers: (1) `abs(diff) < tolerance` as "are these two numbers essentially equal, accounting for floating-point noise," (2) the generator expression producing one True/False per ratio (same pattern as 1.3.2's `dot_product`), (3) `all()` as Python's equivalent of JS `.every()` — every check must pass.
- Addressed why `diff > 0` doesn't work (only tests direction/magnitude of inequality, not closeness, and misses cases where `r` is slightly *smaller* than `ratios[0]`) and why rounding to whole numbers is too coarse (would incorrectly equate distinct eigenvalues like 1.5 vs 2.3, throwing away far more precision than floating-point noise actually requires). Connected to `np.isclose()` as the real-world standard version of this exact pattern, to be met again in gradient-checking (Phase 3).

**Practice results (all correct, all predicted before running):**
- `M=[[2,0],[0,1]]`, `v=[1,0]` → `(True, 2.0)` ✓
- `M=[[2,0],[0,1]]`, `v=[1,1]` → `(False, None)` ✓ — components scaled by different amounts (2x vs 1x), direction changes.
- `N=[[0,1],[1,0]]` (reflection across y=x), `v=[1,1]` → `(True, 1.0)` ✓ — lies exactly on the mirror line, reflection leaves it unchanged.
- `N=[[0,1],[1,0]]`, `v=[1,-1]` → `(True, -1.0)` ✓ — perpendicular to the mirror line, reflection flips it to point exactly opposite, same length.
- Self-observed pattern: a reflection matrix has exactly two eigenvector directions (the mirror line itself, and its perpendicular) — every other vector gets partially rotated rather than purely scaled.

**Gotcha:** none new mathematically — the real depth this session came from thoroughly understanding the verification code itself (filtering, tolerance comparison, generator expressions) rather than treating it as a black box, which is worth preserving as a good pattern to keep encouraging.

**End-goal link:** eigenvalues explain why weight initialization matters (Phase 3.9) and why very deep networks can suffer from vanishing/exploding values during training — both are, at their core, about what happens when you repeatedly apply matrices whose eigenvalues are consistently above or below 1.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers matrix transformations per prior review.

---

## 1.3.7 — Norms & Distances: L1, L2, Cosine Distance

**Concept:** A norm measures a vector's magnitude/length. **L2 norm** = ordinary geometric (Euclidean) length: `√(sum of squares)` — the same `|a|`, `|b|` that appeared undefined in 1.3.2's geometric dot product formula. **L1 norm** = sum of absolute values ("Manhattan/taxicab distance" — grid-walking distance rather than straight-line). **Distance between vectors** = norm of their difference: `||a-b||`. **Cosine similarity** = `(a·b)/(||a||×||b||)` — a direct rearrangement of 1.3.2's `a·b=|a||b|cos(θ)` to isolate `cos(θ)`, meaning it measures *only* the angle between vectors, completely ignoring their length. Cosine distance = `1 - cosine_similarity`.

**Why it matters for ML:** L2 is smooth, penalizes large values heavily (squaring), used in most loss functions and weight decay (3.8). L1 treats all distance equally, encourages sparsity (pushing weights to exactly zero) — relevant to feature selection (2.7) and LoRA (8.6). Cosine similarity is the standard tool for embedding/semantic comparison (8.2) precisely because it's length-invariant — two similar-meaning texts can have embeddings of different magnitudes for incidental reasons, but cosine similarity correctly measures direction alone.

**Worked example:** `a=[3,4]`, `b=[1,2]` (reused from 1.3.2, where a·b=11). `||a||₂=5`, `||b||₂≈2.236`. `cosine_similarity ≈ 11/11.18 ≈ 0.984` — close to 1, confirming near-same direction.

**Code:** `phase1-math/1_3_7_norms.py`
```python
def l1_norm(v):
    return sum(abs(x) for x in v)

def l2_norm(v):
    return math.sqrt(sum(x**2 for x in v))

def eucledian_distance(a, b):
    diff = [a[i] - b[i] for i in range(len(a))]
    return l2_norm(diff)

def cosine_similarity(a, b):
    return dot_product(a, b) / (l2_norm(a) * l2_norm(b))
```

**Practice results (all correct):**
- `L1([3,4])=7`, `L2([3,4])=5.0`
- `euclidean_distance([3,4],[1,2])≈2.828` — matches hand-check (`diff=[2,2]`, `√8≈2.828`)
- `cosine_similarity([3,4],[1,2])≈0.9839` — matches worked example
- **Key result:** `cosine_similarity([3,4],[6,8])=1.0` — `[6,8]` is `[3,4]` scaled 2x (same direction, different length). Confirms cosine similarity is entirely length-invariant, capturing direction only. Explicitly contrasted with raw dot product, which *would* be affected by length, making it a worse similarity metric for embeddings where magnitude carries no semantic meaning.

**Gotcha:** none new mechanically — straightforward given the dot product foundation from 1.3.2.

**End-goal link:** cosine similarity computed here is the exact metric used in Phase 8.2 (embeddings & vector search) and Phase 8.4 (RAG) to find semantically relevant documents/chunks — comparing a query embedding against stored document embeddings via this same formula.

**Milestone:** Section 1.3 progress: vectors → dot product → matrices → matrix-vector → matrix-matrix → eigenvalues → norms/distances, seven lessons deep, all self-verified. Five lessons remain in 1.3 (tensors, SVD, dimensionality reduction, linear systems, numerical stability).

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — relevant, covers norms/distances per prior review.

---

## 1.3.8 — Tensor Operations: N-Dimensional Arrays, Shape, Axes, Broadcasting

**Concept:** A tensor generalizes scalar (0D) → vector (1D) → matrix (2D) → N-D arrays. Shape is a tuple of any length; each position is an **axis**. Real ML data is almost always higher-dimensional: a batch of images is 4D `(batch, height, width, channels)`. **Broadcasting** lets operations combine tensors of different shapes by implicitly "stretching" the smaller one — already used informally in 1.3.1's `vector_scale` (a scalar stretched across a whole vector).

**Why it matters for ML:** every real neural network operation works on tensors of exactly this kind. Broadcasting is how a single bias vector gets added to every row of a batch matrix without an explicit loop — the actual mechanism used constantly once NumPy/PyTorch are introduced.

**Worked example:** `M=[[1,2,3],[4,5,6]]` (2×3), `b=[10,20,30]` (shape (3,), matching M's columns). Broadcasting `b` across every row: `M+b = [[11,22,33],[14,25,36]]`.

**Code:** `phase1-math/1_3_8_tensors.py`
```python
def get_shape(tensor):
    if not isinstance(tensor, list):
        return ()
    return (len(tensor),) + get_shape(tensor[0])

def broadcast_add_bias(M, b):
    return [[M[i][j] + b[j] for j in range(len(b))] for i in range(len(M))]
```

**Recursion deep-dive (significant portion of session):** requested and received a full manual trace of `get_shape` on a 2×2×2 nested list — walked through all 4 recursive calls (base case at the innermost plain number, then unwinding back up building `(2,)→(2,2)→(2,2,2)` via tuple concatenation). Initial self-description ("pushed to the end result") corrected to the accurate framing: each call *waits* for the one below it, then builds a slightly bigger tuple on the way back up — no appending/pushing occurs, it's return-value composition, not list mutation. Also clarified `isinstance()` (≈ JS `Array.isArray`), the required trailing comma for single-item tuples `(x,)`, and `+` as tuple concatenation (≈ JS `.concat()`) rather than arithmetic addition.

**Bugs (both self-produced, both fixed within the session — real debugging reps):**
1. Copy-paste slip: tested `print(get_shape(v))` a second time instead of `print(get_shape(M))` after redefining `M` — silently retested the wrong variable rather than erroring. Caught and corrected.
2. `broadcast_add_bias` initially written as a **flat** comprehension with two chained `for` clauses (`[expr for j in ... for i in ...]`), which Python flattens into one list rather than nesting — produced `[11,14,22,25,33,36]` instead of `[[11,22,33],[14,25,36]]`. Fixed to a properly **nested** comprehension (inner brackets build one row, outer brackets collect rows), matching the same pattern already used in 1.3.5's `matrix_multiply`.

**Practice results (all correct, after fixes):**
- `get_shape([1,2,3]) = (3,)`, `get_shape` on a 3×2 matrix `= (3,2)`, `get_shape` on the 2×2×2 nested list `= (2,2,2)` — all matched hand predictions.
- `broadcast_add_bias(M, [10,20,30]) = [[11,22,33],[14,25,36]]` ✓
- Mismatch tests, generalizing the 1.3.4/1.3.5 pattern correctly: `b=[10,20]` (shorter than M's 3 columns) → silent incomplete result `[[11,22],[14,25]]` (M's third column never touched, since the loop is driven by `range(len(b))`). `b=[10,20,30,40]` (longer) → `IndexError`, since the loop tries `M[i][3]`, out of bounds for 3-column rows. Both correctly predicted before running.

**Gotcha:** the same "which array's length drives the loop" failure-mode pattern has now recurred identically across three different functions (`dot_product`, `matrix_multiply`, `broadcast_add_bias`) — worth recognizing as one root cause (unchecked loop bounds), not three separate bugs. This is precisely why real broadcasting rules in NumPy/PyTorch check shape compatibility explicitly upfront rather than relying on loop bounds silently matching or not.

**End-goal link:** tensor shape reasoning is the single most-used debugging skill in Phase 3+ — nearly every early neural network bug is a shape mismatch somewhere in a forward pass, and being able to trace *why* a particular mismatch fails silently vs. loudly (as practiced repeatedly this lesson) is directly transferable.

**Milestone:** Section 1.3 — 8 of 12 lessons complete. Remaining: SVD (1.3.9), dimensionality reduction/PCA (1.3.10), linear systems (1.3.11), numerical stability (1.3.12).

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — check for tensor/broadcasting-specific coverage; not yet confirmed present in the reviewed content.

---

## 1.3.9 — Singular Value Decomposition (SVD): Concept + Why It Underlies Embeddings & Compression

**Concept:** any matrix `M` decomposes as `M = U·Σ·Vᵀ`. `Σ` (diagonal, non-negative, sorted largest-to-smallest) holds the **singular values** — a ranked list of "how much information/importance each direction carries." `U` and `Vᵀ` are rotation-like matrices (orthonormal columns, related to but not identical to eigenvectors, 1.3.6) that reorient without adding/removing information. Plain-language framing used to rebuild the concept after initial difficulty: "any matrix's behavior = rotate, stretch along a few key directions by ranked amounts, rotate again." Not hand-derived — the actual algorithm is genuinely advanced numerical computation; used via `np.linalg.svd` as a tool, consistent with the curriculum's "NumPy allowed" rule. **First lesson using NumPy for real computation rather than pure from-scratch loops.**

**Why it matters for ML:** because singular values are ranked by importance and often drop off fast, you can discard the small ones and reconstruct a good approximation from far less data — the core idea behind compression, and behind classical (pre-neural) word embeddings: a giant word-co-occurrence matrix can be compressed via SVD into a much smaller per-word vector, capturing most of the real signal in far fewer numbers. Modern neural embeddings are learned differently, but rest on the same underlying intuition.

**Worked example:** `M=[[3,0],[0,1]]` (already axis-aligned, same shape as 1.3.6's stretching matrix) → singular values exactly `[3,1]`, matching the diagonal directly, with `U`/`Vt` both identity (no rotation needed since the matrix was already in its simplest form).

**Code:** `phase1-math/1_3_9_svd.py` — line-by-line walkthrough given before running anything:
```python
import numpy as np
M = np.array([[3, 0], [0, 1]])
U, S, Vt = np.linalg.svd(M)
reconstructed = U @ np.diag(S) @ Vt
```
Explained: `np.array()` converts a nested list into NumPy's fast array type (the "graduated" version of hand-built matrices); `np.linalg.svd()` returns three values unpacked via tuple-unpacking (same pattern as 1.2.4's `x, y = gradient_step(...)`); `@` is NumPy's matrix multiplication operator, doing what hand-built `matrix_multiply` (1.3.5) does; `np.diag(S)` converts the flat singular-value list into a proper diagonal matrix so it can be multiplied. Compression demo also introduced `.copy()` (explicit duplication, avoiding aliasing/reference-sharing bugs — same underlying issue as JS object/array reference semantics) and negative indexing (`S[-1]` = last element, a genuine Python convenience with no direct JS array equivalent).

**Practice results:**
- `M=[[3,0],[0,1]]` → singular values `[3,1]`, `U`/`Vt` both identity — confirmed.
- `M2=[[4,0],[3,-5]]` → singular values `[6.3246, 3.1623]`; reconstruction matched `M2` within floating-point noise (~1e-15, same representation-error theme as earlier lessons).
- Compression: zeroed the smaller singular value, reconstructed `approx=[[2,-2],[4,-4]]` vs real `M2=[[4,0],[3,-5]]` — a notably rough approximation, not close. Correctly predicted "won't be exact," though initial reasoning conflated dropping small-but-nonzero values with dropping already-zero ones. Corrected: compression only works well when there's a large gap between important and unimportant singular values; this toy 2×2 case had both values within 2x of each other (6.3 vs 3.2), too close for a good approximation — unlike real large matrices, where the value gap between dominant and negligible singular values is typically much larger, making the same technique highly effective at scale.

**Gotcha:** the honest, non-idealized result (rough approximation, not a clean demo) is itself the most useful takeaway — compression quality depends entirely on how lopsided the singular value spectrum is, not on the technique alone.

**End-goal link:** first real exposure to "use NumPy as a tool, not reimplement it" — previews the transition happening gradually through the rest of Phase 1 and fully arriving in Phase 2+. SVD-style compression ideas reappear directly in Phase 8.6 (LoRA, low-rank adaptation — literally built on this exact decomposition) and PCA (next lesson, 1.3.10).

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — confirmed by prior direct review to cover SVD/rank/projection content; genuinely relevant second-pass reading now.

---

**Addendum — how singular values are actually computed (follow-up question after initial lesson):** learner correctly noticed M1's singular values ([3,1]) matched its diagonal directly, but guessed M2's singular values ([6.32, 3.16]) might come from reading matrix entries directly (e.g. "[4,3]") — this guess was incorrect, and the real mechanism was walked through using only prior tools:

**Real recipe:** singular values of `M` = `√(eigenvalues of MᵀM)`. `MᵀM` is guaranteed to have real, non-negative eigenvalues (unlike ordinary eigenvalues, 1.3.6, which can be negative) — this is precisely why singular values are always non-negative.

**Verified by hand on M2=[[4,0],[3,-5]]:**
- Transpose (1.3.3): `M2ᵀ=[[4,3],[0,-5]]`
- `M2ᵀ·M2` (1.3.5, matrix multiply): `[[25,-15],[-15,25]]`
- Eigenvalues of that result (not hand-derived, quadratic equation): `40` and `10`
- `√40≈6.3246`, `√10≈3.1623` — exactly matches NumPy's SVD output.

**Why M1 looked deceptively simple:** M1 is diagonal and symmetric, so `M1ᵀ=M1`, and `M1ᵀM1=M1²` just squares each diagonal entry directly (`9` and `1`). For a diagonal matrix, eigenvalues *are* the diagonal entries (same reasoning as 1.3.6's axis-aligned stretching matrix) — so the singular values fell right out to `3` and `1`, purely because M1 had no off-diagonal "cross-talk" between rows/columns. M2's nonzero off-diagonal `3` is exactly why it required the full `Mᵀ·M`→eigenvalues→square-root pipeline rather than a shortcut readout.

**Key takeaway:** SVD isn't new math — it's a specific composition of tools already hand-built in this curriculum (transpose, matrix multiply, eigenvalues, square root). Nothing about it is a black box in principle, only the eigenvalue-solving step for larger matrices is deferred as "genuinely advanced, not hand-derived here."

---

**Addendum 2 — naming U/S/Vt and precisely what "rotation" means (second follow-up):**

**Names:** `U` = left singular vectors (its columns). `Σ`/`S` = singular values. `V` = right singular vectors (`Vt` is `V` transposed, what NumPy actually returns).

**Precision of the "rotation":** not vague or approximate — `V`'s columns are exactly the eigenvectors of `MᵀM`; `U`'s columns are exactly the eigenvectors of `MMᵀ`. Built from tools already known (eigenvectors, 1.3.6), constrained to be:
1. **Unit length** (L2 norm = 1, per 1.3.7)
2. **Mutually perpendicular** (pairwise dot product = 0, per 1.3.2)

Columns satisfying both are called **orthonormal**; a square matrix of orthonormal columns is an **orthogonal matrix** — the formal term for "rotation-like": preserves all lengths and angles, adds zero new information, purely reorients. This is exactly why all "importance" information concentrates in `Σ` alone.

**Verified directly against M2's real output**, not taken on faith:
- `Vt=[[-0.7071,0.7071],[-0.7071,-0.7071]]` → since `Vt=Vᵀ`, each row of `Vt` is a column of `V`: `v1=[-0.7071,0.7071]`, `v2=[-0.7071,-0.7071]`.
- Unit length check: `L2(v1)=√(0.5+0.5)=1` ✓
- Perpendicularity check: `v1·v2 = 0.5-0.5 = 0` ✓
- Eigenvector check: `(M2ᵀM2)·v1 ≈ [-28.28,28.28]`, and `40×v1 ≈ [-28.28,28.28]` — matches exactly, confirming v1 is the eigenvector for eigenvalue 40 (√40=6.3246, the largest singular value — consistent ordering by decreasing eigenvalue).

**Honest subtlety:** eigenvectors/singular vectors are unique only up to sign (`v` and `-v` are equally valid). NumPy applies some internal consistent sign convention so `U·Σ·Vᵀ` correctly reconstructs `M`, but the *direction* (the line through space) is what's truly unique — which way counts as "positive" along that line isn't.

**Summary answer to "how specific are the rotations":** fully and uniquely determined (up to sign) by the requirement of unit-length, mutually-perpendicular eigenvectors of `MᵀM`/`MMᵀ`, ordered by decreasing eigenvalue — nothing arbitrary about it, every piece traces back to tools already hand-built earlier in section 1.3.

---

## 1.3.10 — Dimensionality Reduction: PCA from Scratch, t-SNE/UMAP Concept

**Concept:** PCA finds the small number of directions that capture the most variation in high-dimensional data, allowing compression/visualization with minimal information loss. Built almost entirely from tools already hand-built: eigenvectors (1.3.6) of the data's **covariance matrix** (a `MᵀM`-shaped construction, same pattern as 1.3.9's SVD addendum) reveal the directions of maximum spread — the eigenvector with the largest eigenvalue is the **first principal component**. PCA and SVD are deeply related; real libraries typically compute PCA via SVD internally for efficiency/stability.

**Why it matters for ML:** compressing high-dimensional data (weights, embeddings) down to a manageable, interpretable number of dimensions while preserving most real structure — same underlying idea as 1.3.9's compression story, now applied to datasets rather than single matrices.

**Worked example:** 4 points nearly on a line: `[[2,3],[3,4],[4,5],[5,6]]`. Expected: one large eigenvalue (along the [1,1] line direction), one near-zero eigenvalue (perpendicular, almost no spread that way).

**Code:** `phase1-math/1_3_10_pca.py` — full line-by-line walkthrough given before running, covering: `.mean(axis=0)` (axis vocabulary from 1.3.8, now used for real — averaging down columns); `data - mean` as automatic broadcasting (1.3.8) rather than a manual loop; `centered.T @ centered / (n-1)` as the covariance matrix (the `MᵀM` pattern from 1.3.9, plus Bessel's correction, deferred to Phase 1.4); `np.linalg.eig()` as the "find" counterpart to 1.3.6's "check" function (`check_eigenvector`); `np.argsort(...)[::-1]` for descending-order index sorting (argsort returns sorting *indices*, not sorted values; `[::-1]` reverses a sequence); `eigenvectors[:, order[:n_components]]` as NumPy's 2D "all rows, selected columns" indexing.
```python
def pca(data, n_components):
    data = np.array(data, dtype=float)
    mean = data.mean(axis=0)
    centered = data - mean
    cov_matrix = (centered.T @ centered) / (len(data) - 1)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    order = np.argsort(eigenvalues)[::-1]
    top_components = eigenvectors[:, order[:n_components]]
    reduced = centered @ top_components
    return reduced, eigenvalues[order]
```

**Practice results (all correct, all predicted before running):**
- Eigenvalues: `[3.333, ~0]` (`-4.44e-16`, essentially zero) — massive gap, exactly as predicted, confirming the data is secretly near-1-dimensional.
- Dominant eigenvector: `[0.7071, 0.7071]` — matches the predicted `[1,1]` line direction exactly.
- Reduced (1D) values: `[-2.1213, -0.7071, 0.7071, 2.1213]` — every consecutive gap exactly `1.4142` (`=√2`), correctly matching the length of each `[1,1]` step in the original evenly-spaced data. PCA preserved the even spacing when projecting down to one dimension.
- New gotcha encountered: `np.linalg.eig` returns complex-typed output (`+0.j` suffix) even when eigenvalues are guaranteed real (as they always are for symmetric covariance matrices) — NumPy defaults to complex dtype since it can't assume realness for arbitrary matrices in general. Not an error, just a type quirk to recognize.

**Conceptual question (PCA vs. t-SNE/UMAP) — needed correction:** initial answer ("PCA for straightforward tasks, t-SNE/UMAP when there are multiple truths") was vague and didn't capture the real distinction. Corrected framing: **PCA preserves global/linear structure** — best when the meaningful relationships in data really are roughly linear, good for compression and gives mathematically interpretable axes. **t-SNE/UMAP preserve local neighborhood relationships** ("which points were near which"), even at the cost of distorting overall/global shape — better suited for visualizing genuinely non-linear clustering, e.g. an embedding space where semantically similar code snippets should appear close together even if their true high-dimensional relationship isn't a straight line. Connected to the learner's own Jarvis-platform goal: PCA fits compression-style questions (e.g. "how does this weight matrix vary along its dominant axes," echoing 1.3.9); t-SNE/UMAP fit exploratory visualization of a coding-assistant's embedding space.

**Gotcha:** none new mechanically beyond the complex-dtype quirk noted above.

**End-goal link:** PCA (and dimensionality reduction generally) reappears throughout the curriculum — visualizing high-dimensional embeddings (5B.3, 8.2), compressing model representations, and conceptually anticipating why some directions in weight-space matter far more than others during training (a recurring theme from 1.3.6's eigenvalues through 1.3.9's SVD to here).

**Milestone:** Section 1.3 — 10 of 12 lessons complete. Remaining: linear systems (1.3.11), numerical stability (1.3.12) — the latter directly follows up on floating-point themes that have recurred since 1.2.1.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — confirmed by prior review to cover dimensionality reduction/projection content directly.

---

## 1.3.11 — Linear Systems: Solving Ax = b

**Concept:** Generalizes 1.1.1 (solve one equation, one unknown) to many equations, many unknowns simultaneously, expressed compactly as `A·x = b` (A = coefficient matrix, x = unknowns vector, b = results vector) — a direct application of matrix-vector multiplication (1.3.4). If `A` has an inverse `A⁻¹` (satisfying `A⁻¹A=I`, the identity matrix from the earlier eigenvalue-clarification question), then `x = A⁻¹b` — the matrix analog of dividing both sides of `2x=8` by 2.

**Why it matters for ML:** solving `Ax=b` is a core building block inside other algorithms — linear regression (2.2) has a closed-form solution built on exactly this; Newton's method (a gradient-descent alternative) also reduces to repeatedly solving linear systems. Also introduces the well-posed vs. ill-posed distinction, setting up 1.3.12 directly.

**Worked example:** `A=[[2,1],[1,-1]]`, `b=[11,1]`. `det(A)=(2)(-1)-(1)(1)=-3`. Using the 2×2 inverse formula, `A⁻¹=[[1/3,1/3],[1/3,-2/3]]`, giving `x=A⁻¹b=[4,3]`. Verified by substitution: `2(4)+3=11` ✓, `4-3=1` ✓.

**Code:** `phase1-math/1_3_11_linear_systems.py` — used `np.linalg.solve(A,b)` rather than the manual inverse-formula approach, flagged as the numerically better real-world method (previews 1.3.12).

**Practice results (all correct):**
- `A=[[2,1],[1,-1]]`,`b=[11,1]` → `[4,3]` ✓, matches hand-worked example.
- Own example: `A=[[3,2],[1,-1]]`,`b=[12,1]` → `[2.8,1.8]`, verified by substitution into both original equations (`3(2.8)+2(1.8)=12` ✓, `2.8-1.8=1` ✓).
- `A=[[2,4],[1,2]]`,`b=[10,5]`: correctly computed `det(A)=(2)(2)-(4)(1)=0` and predicted no inverse exists before running. Confirmed with `LinAlgError: Singular matrix`. Initial reasoning ("1/0 crashes it during inverse computation") was directionally right but refined: `np.linalg.solve` doesn't literally compute a naive inverse internally, but hits the same underlying mathematical wall regardless of algorithm — `det=0` defines a **singular matrix** (new term), geometrically explained here as the second row (`[1,2]`) being an exact scalar multiple of the first (`[2,4]`) — the two equations describe the same line rather than two independent constraints, so the system has either infinitely many or zero solutions, never exactly one. Connected back to 1.3.6: singular matrices always have `0` as one of their eigenvalues (they collapse some direction of space entirely).

**Gotcha:** none new mechanically — the real depth was in precisely correcting *why* solve() fails (algorithm-independent mathematical fact, not merely "some internal division by zero").

**End-goal link:** solving linear systems efficiently and stably is the literal computational core of closed-form linear regression (Phase 2.2) and appears repeatedly as a subroutine inside more advanced optimization methods throughout later phases.

**Addendum — t-SNE/UMAP depth check (follow-up after 1.3.10, before starting 1.3.11):** confirmed the shallow treatment of t-SNE/UMAP was intentional, per the curriculum's own distinction in wording ("PCA from scratch" vs. "t-SNE/UMAP concept"). Extra intuition given: t-SNE computes neighbor probabilities in both high-D and low-D space, then uses gradient descent (same core mechanism as 1.2.4) to minimize the KL divergence (previewed, formally covered in Phase 1.5.2) between them — different loss function, same underlying optimization mechanism already known. UMAP is topology-based (out of scope for this curriculum), generally faster, and tends to better preserve global structure — the more commonly reached-for default of the two in current practice. Not formally logged as its own topic; folded in here as context.

**Milestone:** Section 1.3 — 11 of 12 lessons complete. Only numerical stability (1.3.12) remains to close out Linear Algebra entirely — directly continuing the floating-point precision theme that has recurred since 1.2.1.

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — check for linear-systems-specific coverage; not yet confirmed present in the reviewed content.

---

## 1.3.12 — Numerical Stability: Why Floating Point Errors Matter in Deep Learning

**Concept:** No new math — this lesson names and consolidates a theme that has recurred throughout the entire section: floating point isn't perfectly precise, and algorithm structure determines whether that imprecision stays harmless or compounds into real errors. Recap of prior sightings: 1.2.1 (h-shrinking, catastrophic cancellation first named), 1.2.5 (floating noise breaking an unstable equilibrium), 1.3.4/1.3.5/1.3.8 (float tails like 3.1999999999999997), 1.3.9/1.3.10/1.3.11 (NumPy's internal algorithms flagged as deliberately different from naive by-hand formulas).

**Why it matters for ML:** deep networks chain thousands of operations; small per-operation errors can compound into **exploding gradients** (errors amplify) or **vanishing gradients** (errors shrink to nothing, learning stalls) — both connect directly to 1.3.6's eigenvalues (repeated multiplication by matrices with eigenvalues consistently >1 or <1).

**Two concrete failure modes demonstrated:**

**1. Underflow with exponential decay.** `phase1-math/1_3_12_numerical_stability.py`: multiplying 200 copies of `0.01` directly collapsed to exactly `0.0` around iteration 162 (float64's absolute representable floor, ≈5×10⁻³²⁴). The log-space equivalent (`sum of log(0.01)` instead of `product of 0.01`) stayed a precise, meaningful number the entire time (-833.5 at iteration 180) — concrete, live demonstration of why 1.1.4 called `log` a numerical-stability necessity rather than stylistic.

**2. Catastrophic cancellation, sharpest form yet.** Predicted `(1.0 + 1e-16) - 1.0` would print something close to `1e-16` (reasonable in principle) — **actual result: exactly `0.0`**, a genuine miss worth understanding precisely. Introduced **machine epsilon** (~2.22×10⁻¹⁶ near magnitude 1.0 — the smallest gap float64 can represent between two distinct numbers at that scale): `1e-16` is smaller than that gap, so `1.0 + 1e-16` rounds back down to exactly `1.0` *before* any subtraction even happens — the information is destroyed at the addition step, not the subtraction. `relative_error` correctly returned `0.0` too — not a bug, an accurate report that 100% of the intended signal was lost, not partially degraded.

**Code:**
```python
def underflow_computation():
    p = 0.01
    product = 1.0
    log_p = math.log(p)
    log_sum = 0.0
    for i in range(200):
        product *= p
        log_sum += log_p
```

**Conceptual question on why NumPy's real algorithms (LU/QR decomposition — named, not built here) beat naive inverse-via-determinant:** required a full rebuild from scratch after an initial "not sure I understand" response. Resolved by directly connecting to the just-observed cancellation result: computing an explicit inverse (determinant + cofactors, as hand-done in 1.3.11) involves many multiplication/subtraction/division steps, each a potential site for the exact kind of catastrophic information loss just witnessed in the `1e-16` example — worse as matrices grow larger or determinants shrink toward zero. NumPy's internal algorithms are structured specifically to avoid ever subtracting two dangerously close numbers, which is the real (not merely speed-related) reason they're preferred in practice.

**Gotcha:** the `1e-16` prediction miss is itself the most valuable result of this lesson — a clean, first-hand demonstration that "small errors accumulate gradually" isn't the only failure mode; some operations lose information *instantly and completely* the moment a value crosses below the local precision floor.

**End-goal link:** this lesson is the direct conceptual bridge to Phase 3.13 (debugging neural networks — vanishing/exploding gradients) and explains, in advance, why real training code is written with specific numerically-stable patterns (log-space probability computation, careful subtraction ordering, library-provided solvers instead of hand-rolled linear algebra) rather than the mathematically-equivalent-but-fragile naive versions.

---

## Milestone: Section 1.3 (Linear Algebra) — FULLY COMPLETE

All 12 lessons closed: vectors → dot product → matrices → matrix-vector multiply → matrix-matrix multiply → eigenvalues → norms/distances → tensors/broadcasting → SVD → PCA/dimensionality reduction → linear systems → numerical stability. Every lesson was hand-built, numerically self-verified, and (from 1.3.9 onward) supplemented with real NumPy tool usage per the curriculum's "NumPy allowed, frameworks not" rule. Two topics (1.3.9 SVD, 1.3.12 numerical stability) each had substantial follow-up depth added after initial close, reflecting genuine engagement rather than surface-level completion.

**Next: Phase 1.4 — Probability & Statistics**, starting with **1.4.1 — Mean, variance, standard deviation — by hand on a small dataset.**

→ repo: `phases/01-math-foundations/01-linear-algebra-intuition` — this lesson (confirmed by direct content review earlier in this project) is now a genuinely comprehensive second-pass read, having covered vectors, matrices, dot products, rank, projection, Gram-Schmidt/QR, and low-rank decomposition (LoRA-relevant) — all territory now familiar from this section. Worth reading in full as a capstone to Section 1.3.

---

# Phase 1.4 — Probability & Statistics

## 1.4.1 — Mean, Variance, Standard Deviation: By Hand on a Small Dataset

**Concept:** Mean = center of data (already used unnamed in 1.3.10's `data.mean(axis=0)`). Variance = average squared distance from the mean (squaring prevents positive/negative distances from cancelling — same reasoning as L2 norm, 1.3.7). Standard deviation = `√variance`, bringing units back to the original scale (variance of dollar values is in "dollars²," std dev is back in plain dollars).

**Why it matters for ML:** the covariance matrix used in 1.3.10's PCA is this exact idea generalized to multiple dimensions/features jointly. Standard deviation is central to feature normalization (Phase 2, near-universal preprocessing), weight initialization (Phase 3.9 — poorly chosen std dev causes training instability, connecting to 1.3.12), and noise control in diffusion models (Phase 5D.5).

**Worked example:** `[2,4,4,4,5,5,7,9]` → mean=5, diffs=[-3,-1,-1,-1,0,0,2,4], squared=[9,1,1,1,0,0,4,16], sum=32, variance=32/8=4, std=√4=2.

**Code:** `phase1-math/1_4_1_mean_variance.py`
```python
def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    squared_diffs = [(x - m)**2 for x in data]
    return sum(squared_diffs) / len(data)

def std_dev(data):
    return variance(data) ** 0.5
```
Noted: `** 0.5` is the same operation as `math.sqrt`, via the fractional-exponent connection to the power rule (1.2.2).

**Practice results (all correct):**
- `[2,4,4,4,5,5,7,9]` → mean=5.0, variance=4.0, std=2.0 — matches worked example.
- `[3,4,5,6,7]` (same mean, tighter spread) → variance=2.0, std≈1.414 — correctly smaller than the first dataset's variance, confirming "tighter clustering around the same center → lower variance."
- `[5,5,5,5,5]` (identical values) → variance=0.0, std=0.0 — correctly predicted before running: every point's distance from the mean is exactly 0, so the average of all-zero squared distances is 0.

**Gotcha:** none new — clean, direct application of prior lessons (L2-style squared distance, fractional exponents).

**End-goal link:** zero variance is a real, meaningful signal — a feature or neuron output that never varies carries no information a model can learn from, a concept that recurs when diagnosing "dead" neurons or uninformative features later in the curriculum.

→ repo: not yet checked for this phase — verify against catalog when convenient.

---

## 1.4.2 — Probability Basics: Events, Independence, Combinations

**Concept:** Probability = `favorable outcomes / total outcomes`, range [0,1]. An event is the specific thing being measured. **Independence**: two events are independent if one tells you nothing about the other; for independent events, `P(A and B) = P(A) × P(B)`. **Combinations**: `C(n,k) = n!/(k!(n-k)!)` — number of distinct ways to choose k items from n, order irrelevant.

**Why it matters for ML:** Naive Bayes (2.12) is literally named after assuming feature independence. Combinations matter for counting configurations/search spaces (e.g. possible move sequences in a game — directly relevant to game-generation goals). Probability underlies classifier outputs directly — a network's final classification output is literally a probability distribution.

**Worked example:** `P(rolling a 4 on a d6)=1/6`. `P(heads,heads)=0.5×0.5=0.25`. `C(4,2)=4!/(2!2!)=6`, verified against the hand-listed pairs `{AB,AC,AD,BC,BD,CD}`.

**Code:** `phase1-math/1_4_2_probability.py`
```python
def probability(favorable, total):
    return favorable / total

def independent_and(p_a, p_b):
    return p_a * p_b

def combinations(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
```

**Practice results (all correct):**
- `P(rolling a 4) ≈ 0.1667` ✓
- `P(heads,heads)=0.25` ✓; three flips computed via recursive reuse (`independent_and(0.5, independent_and(0.5,0.5))` rather than new code) → `0.125` ✓. Noted the halving pattern (0.5→0.25→0.125→...) as structurally the same shrink-toward-zero shape as 1.3.12's underflow demo — enough independent multiplications and this hits the same floating-point floor.
- `C(4,2)=6.0` ✓, `C(6,3)=20.0` ✓ — correctly predicted the larger pool (6 vs 4) yields more combinations.
- `C(n,n)`: correctly predicted `=1` before running (only one way to "choose everything," regardless of n) — confirmed with `C(5,5)=1.0`.

**Gotcha:** none new — direct, mechanically clean application, main value was recognizing the underflow connection to 1.3.12.

**End-goal link:** independence assumptions and probability multiplication recur throughout classical ML (2.12 Naive Bayes) and directly motivate why classifier training uses log-probabilities (cross-entropy loss, upcoming in 2.3/3.4) rather than raw probability products — the exact underflow risk just observed in miniature here.

→ repo: not yet checked for this phase — verify against catalog when convenient.

---

## 1.4.3 — Bayes' Theorem: Worked Example, Why It's Foundational

**Concept:** `P(A|B) = P(B|A)×P(A)/P(B)` — lets you compute a hard-to-measure conditional probability (`P(A|B)`) from an easier-to-measure reverse one (`P(B|A)`). `P(A)` is the **prior** (belief before evidence); `P(A|B)` is the **posterior** (updated belief after evidence).

**Why it matters for ML:** foundation of Naive Bayes (2.12, builds on 1.4.2's independence assumption) and Bayesian thinking generally (prior → evidence → posterior), reappearing in RL (5E) and underlying how to correctly interpret any model's confidence score.

**Worked example (classic medical test):** disease prevalence 1%, test 95% sensitive, 5% false-positive rate. `P(B) = 0.95×0.01 + 0.05×0.99 = 0.059`. `P(disease|positive) = 0.95×0.01/0.059 ≈ 0.161` — dramatically lower than the naive "95%" intuition, because false positives from the large healthy population outnumber true positives from the small sick population.

**Code:** `phase1-math/1_4_3_bayes.py`
```python
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    p_not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b
```

**Practice results:**
- Original example → `0.161` ✓
- `p_a=0.5` (common disease, same test) → exactly `0.95`. Explained: with 50/50 prevalence and symmetric error rates (both 5%), the prior perfectly cancels out of the formula, collapsing the posterior to the test's raw accuracy. Confirms: the same test becomes far more trustworthy as the condition being tested for becomes more common.
- Worse-test experiment initially changed two parameters simultaneously (sensitivity 0.6 AND false-positive rate 0.4 together) rather than isolating one — result `0.0149`. Clarifying question asked and resolved (see below). Rerun with only sensitivity changed (0.6, false-positive rate unchanged at 0.05) → `0.108` — correctly lower than 0.161, but a noticeably smaller drop than the combined-effect run, correctly distinguishing "one property got worse" from "both properties got worse."

**Clarifying question, resolved (important conceptual fix):** "why isn't P(B|not A) just 1-P(B|A)?" Resolved by distinguishing two different rules that look superficially similar: `P(B|A) + P(not B|A) = 1` genuinely holds (within one fixed population — sick people either test positive or negative, covering all outcomes). But `P(B|A)` and `P(B|not A)` describe **two separate populations** (sick vs. healthy) with independently-measured, unrelated error rates — no subtraction relationship connects them. A test's sensitivity and false-positive rate are set by how it actually behaves in each group, measured separately; nothing forces one to be `1-` the other.

**Gotcha:** conflating "complement within one condition" (`P(B|A)+P(not B|A)=1`, always true) with "relationship between two different conditions" (`P(B|A)` vs `P(B|not A)`, no fixed relationship) — a very natural and common point of confusion, worth remembering precisely.

**End-goal link:** Bayes' theorem is the direct mathematical foundation of Naive Bayes classifiers (2.12) and the general Bayesian framing (prior/evidence/posterior) that reappears throughout RL and any probabilistic reasoning about model confidence.

→ repo: not yet checked for this phase — verify against catalog when convenient.

---