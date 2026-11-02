import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import sys

    print(sys.version)
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 1.2 Definition eines Algorithmus""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Implementierung 1.1: Horner-Schema**

    Als ersten Algorithmus implementieren wir das Horner-Schema. Dafür müssen wir im ersten Schritt die Ordnung des Polynoms, d.h., die Anzahl der Koeffizienten bestimmen, und dann rückwärts durch die Liste der Koeffizienten iterieren.
    """
    )
    return


@app.function
def horner_schema(koeffizienten, x):
    n = len(koeffizienten)
    p = koeffizienten[-1]
    for i in range(n - 1, 0, -1):
        p = koeffizienten[i - 1] + x * p
    return p


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Diese Funktion wenden wir auf das Polynom $$p(x) = 3x^5 - 2 x^4 + 1$$ an. Dabei müssen wir beim Übergeben der Koeffizienten vorsichtig sein, dass wir diese in der richtigen Reihenfolge und die Koeffizienten 0 für Terme niedriger Ordnung, die wir in dem Polynom nicht explizit aufgeschrieben haben, mit übergeben.""")
    return


@app.cell
def _():
    horner_schema([1, 0, 0, 0, -2 ,3], 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    *Ergänzende Einzelheiten zum Code*
    - Mit negativen Indizes können wir von rechts auf Elemente der Liste zugreifen.
    - Mit der Funktion `range(a, b, n)` können über die ganzen Zahlen im **halboffenen Inverval** $[a,b)$ in Schritten der Größe `n` iterieren.
    - Die `list` der Koeffizienten `koeffizienten` hat `n` Einträge. In Python starten Indizes, wie in den meisten Programmiersprachen, mit 0. Der Eintrag `koeffizienten[n - 1]` ist also der **letzte** der Liste. Daher müssen wir noch eine Indexverschiebung `i - 1` vornehmen.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Implementierung 1.2: Vollständiges Horner-Schema**

    Für das vollständige Horner-Schema nehmen wir Matrizen aus der Python-Bibliothek `numpy`, die sehr viele Werkzeuge zum wissenschaftlichen Rechnen in Python zur Verfügung stellt. In dieser Matrix (`array`) werden dann die Werte gespeichert, die wir zum Auswerten des Polynoms und dessen Ableitungen benötigt werden.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import math

    def vollstaendiges_horner_schema(koeffizienten, x):
        n = len(koeffizienten)
        p = np.zeros(n)
        a = np.zeros((n + 1, n))
        a[:, -1] = koeffizienten[-1]
        a[0, :] = koeffizienten

        for k in range(n):
            for j in range(n - 1, k, -1):
                a[k + 1, j - 1] = a[k, j - 1] + a[k + 1, j] * x
            p[k] = math.factorial(k) * a[k + 1, k]
        return p
    return (vollstaendiges_horner_schema,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Diesen Algorithmus wenden wir jetzt auf die obige Aufgabe an:""")
    return


@app.cell
def _(vollstaendiges_horner_schema):
    vollstaendiges_horner_schema([1, 0, 0, 0, -2 ,3], 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    *Ergänzende Einzelheiten zum Code*

    - Mit `a[:, -1]` setzen wir den Wert in **allen Reihen** in der **letzten Spalte**.
    - Bei `numpy` Objekten müssen wir besonders vorsichtig sein, dass wir die Einträge der bereits angelegten `array`s ändern, und nicht den Verweis auf das Objekt überschreiben.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Programmierabgabe

    **Gruppenmitglieder von Gruppe X**

    Name, Matrikel Nummer <br>
    Viktor Kosin, 123456789 <br>
    Tobias Knoke, 987654321 <br>

    Python Version: 3.XX
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Augabenteil a)**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Aufgabenteil b)**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Aufgabenteil c)**""")
    return


if __name__ == "__main__":
    app.run()
