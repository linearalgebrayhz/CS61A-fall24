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


From week of interpreters

Procedure definition is short hand of define with a lambda expression

```scm
(define (<name> <formal parameters>) <body>)
; is equivalent to
(define <name> (lambda (<formal parameters>) <body>))
```

## Dynamic Scope

The way in which names are looked up in Scheme and Python is called lexical scope (or static scope)

Lexical Scope: The parent of a frame is the environment in which a procedure was **defined**.

Dynamic scope: The parent of a frame is the environment in which a procedure was **called**.