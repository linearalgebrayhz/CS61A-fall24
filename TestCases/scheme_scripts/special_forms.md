There are several special forms in scheme

1. Cond & Begin

`cond` has the rest of its expressions, a bunch of pairs, where the pairs are the conditions and what to do do if the condition is true

```scm
(cond ((> x 10) (print 'big))
      ((> x 5)  (print 'medium))
      (else     (print 'small))
)
(print
    (cond ((> x 10) 'big)
        ((> x 5)  'medium)
        (else     'small)
))
```

The begin special form combines multiple expressions into one expression

```scm
(cond ((> x 10) (begin (print 'big) (print 'guy)))
      (else     (begin (print 'small) (print 'fry)))
)
```

2. Let expression

binds symboals to values temporarily; just for one expression

```scm
(define c (let ((a 3)
                (b (+ 2 2)))
                (sqrt (+ (* a a) (* b b)))
                ))
```