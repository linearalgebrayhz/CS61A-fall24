;From Week 13 Macros
(define (square-expr term) `(* ,term ,term))

`(+ ,(square-expr `a) ,(square-expr `b))

; define macro
(define-macro (check expr) (list 'if expr ''passed (list 'quote (list 'failed: expr))))

(define fact (lambda (n)
    (if (zero? n) 1 (* n (fact (- n 1))))
))

(define original fact)
(define fact (lambda (n)
    (print (list 'fact n))
    (original n)
))

; trace !
(define-macro (trace expr)
    (define operator (car expr))
    `(begin
        (define original ,operator)
        (define ,operator (lambda (n)
                                (print (list (quote ,operator) n))
                                (original n)
        ))
        (define result ,expr)
        (define ,operator original)
        result
    )
)