# Phase 1 — Math Foundations — Notes

Detailed lesson notes for Phase 1. Append one entry per completed topic.

---

## 1.1.1 — Variables, Expressions, Solving for x

**Concept:** A variable is an unknown placeholder (like `let x` in JS). An expression combines numbers, variables, and operations into a "recipe" that produces a value once the variable is known. An equation states two expressions are equal; solving means finding the value of x that makes the statement true. Core rule: whatever operation is applied to one side of the equation must be applied to the other, to keep it balanced.

**Worked example:** Solve `2x + 3 = 11`.

- Subtract 3 from both sides: `2x = 8`
- Divide both sides by 2: `x = 4`
- Check by substitution: `2(4) + 3 = 11` ✓

**Code mapping:** There's no direct "solve" equivalent in code — this is manual symbolic manipulation done before any code exists. The _verification_ step maps directly to a boolean check:

```javascript
const x = 4;
console.log(2 * x + 3 === 11); // true
```

**Practice results (all correct, verified in JS):**

- `3x - 5 = 16` → x = 7
- `x/4 + 2 = 9` → x = 28
- `5(x - 1) = 20` → x = 5

**Gotcha:** The divisibility of the constant term by the multiplier tells you in advance whether the answer will be a whole number or a fraction — worth eyeballing before solving. E.g. `5(x-1) = 22` would have produced x = 5.4 instead of a clean integer.

**End-goal link:** Every ML model is fundamentally an equation with unknowns (called _weights_, introduced formally in Phase 3). Training a model is solving for those unknowns — just with millions of variables instead of one, and using calculus (gradient descent) instead of algebra to do it at that scale. This lesson is the atomic unit everything else in the curriculum builds on.

→ repo: no direct match confirmed in `phases/01-math-foundations/`. The repo's lesson `01-linear-algebra-intuition` was checked directly (content reviewed 2026-07-04) and covers vectors/matrices/dot products/rank — that maps to our 1.3, not 1.1. No basic-algebra-specific lesson confirmed yet; check `aiengineeringfromscratch.com/catalog.html` when this phase's other lessons are reviewed.

---

## 1.1.2 — Functions: what f(x) means, domain, range

**Concept:** A function is a rule that takes an input and produces exactly one output — the same idea as `function f(x) { return ... }` in JS, just terser notation. `f(x) = 2x + 3` means "double the input, add 3." The **domain** is the set of valid inputs; the **range** is the set of possible outputs. These become critical later — e.g. probabilities must live in range `[0, 1]`, which is _why_ activation functions like sigmoid/softmax exist instead of using raw unconstrained numbers.

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
- Verified slope using non-adjacent points (1,5) and (4,11) → slope=2.0, matches m. Stronger check than requested — confirms slope is constant across _any_ two points, not just neighbors.
- Tested m=-5, b=5: y1=5, y2=0, y3=-5 — correctly decreasing as x increases, confirming negative slope behavior.
- Correctly predicted m=0 produces a horizontal line at y=b — refined to: slope is _rate of change_, so zero rate of change means y never moves regardless of x, i.e. y=b for all x (not just "passes through b" but flat everywhere).

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
- Correctly reasoned through _why_ structurally: a positive base raised to any real exponent is always strictly greater than 0 — it approaches 0 as the exponent goes to -∞ but never reaches it. So 0 is outside the domain of any log function, same domain-restriction concept first introduced with `g(x)=1/x` in 1.1.2.

**Gotcha:** `ZeroDivisionError` (from `1/0`) and `ValueError` (from `log(0)`) are different exception types for related-but-distinct reasons — both are Python refusing an undefined operation, but worth being able to name which is which when debugging later. Also: exact error message wording can differ across Python versions (3.14 here is more descriptive than the classic "math domain error" phrasing seen in older references).

**End-goal link:** log-based loss functions (cross-entropy, log-likelihood) are the numerical-stability backbone of virtually every classifier and language model trained from Phase 2 onward — this lesson is the reason that machinery exists rather than just being "the way it's done."

→ repo: no confirmed match yet for exponents/logs specifically. Check `aiengineeringfromscratch.com/catalog.html` when convenient rather than guess a lesson name.

---

**Section 1.1 (Algebra) — complete.** All four lessons (variables/solving, functions, slope/intercept, exponents/logs) closed 2026-07-04. Next: 1.2 Calculus.

---
