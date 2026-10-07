// KaTeX za formule. pymdownx.arithmatex (generic: true) već pretvara
// $...$ i $$...$$ u \(...\) i \[...\], pa ovdje tražimo samo te oznake.
// Tako se obični znak $ u tekstu nikad ne pokušava protumačiti kao formula.
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    throwOnError: false
  })
})
