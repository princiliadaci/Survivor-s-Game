# The Survivor's Number

Python code for Problem 0.6, *Survivor's number*, of the course
Mathematical Problem Solving at AIMS Senegal (2026-2027), Group 6.

## The problem

People numbered 1 to n stand in a circle. Starting with person 1, we skip one
person and eliminate the next one, again and again, until only one person is
left. J(n) is the number of this survivor. For example, J(10) = 5.

If n = 2^m + l with 0 <= l < 2^m, then

    J(n) = 2l + 1.

In base 2, J(n) is obtained by moving the first digit of n to the end.
If the game starts with person s instead of person 1, the survivor is the
person 2l places after s.

## Functions

| Function        | What it does                                                  |
|-----------------|---------------------------------------------------------------|
| `J_0(n)`        | plays the game and prints the circle after each elimination   |
| `J_1(n)`        | uses the formula, searching for m and l over all pairs        |
| `J_2(n)`        | uses the formula, finding 2^m by doubling                     |
| `J_binary(n)`   | moves the first binary digit of n to the end                  |
| `J_start(n, s)` | survivor when the game starts with person s                   |
| `play(n, s=1)`  | plays the game without printing, used for the checks          |
| `check(N)`      | compares the game with the formulas for n = 1, ..., N         |

## How to run

You only need Python 3, no extra package.

    python survivor_code.py

Output:

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ...
    So 5 is the only survivor
    5 5 5 8
    all the checks passed for n = 1, ..., 200

## The report

The folder `report` contains the full LaTeX source of our written report,
made with the AIMS Senegal Assignment template, and the compiled PDF
`Group6_MPS.pdf`.

| File                | Content                                        |
|---------------------|------------------------------------------------|
| `Group6_MPS.tex`    | main file: header, title page, abstract        |
| `introduction.tex`  | Section 1, Introduction                        |
| `tests.tex`         | Section 2, Playing the Game by Hand            |
| `observations.tex`  | Section 3, What the Table Shows, and Why       |
| `formula.tex`       | Section 4, The Formula and Its Generalisation  |
| `binary.tex`        | Section 5, Very Large Circles: Base 2          |
| `code.tex`          | Section 6, The Python Code                     |
| `conclusion.tex`    | Section 7, Conclusion                          |
| `lstlisting.tex`    | style of the Python listings (AIMS template)   |
| `AIMSSenegalLogo.jpeg` | logo used in the header                     |

To compile, run `pdflatex` three times on the main file (for the table of
contents and the references):

    cd report
    pdflatex Group6_MPS.tex
    pdflatex Group6_MPS.tex
    pdflatex Group6_MPS.tex

On Overleaf, upload the content of the folder `report` and choose
`Group6_MPS.tex` as the main document, with the pdfLaTeX compiler.

## Group 6

Daci Yimete Princilia Doleresse, Dlamini Sandziso Siyabonga,
Fadhul Abdouroihamane, Kambale Maruba Exauce,
Marie Hortense Lucie Senamie Saizonou, Oumar Sow,
Razan Salah Mohammed Salih Mansour, Samba Diallo.

Supervised by Dr Audace A. V. Dossou-Olory, African Institute for
Mathematical Sciences (AIMS), Senegal.
