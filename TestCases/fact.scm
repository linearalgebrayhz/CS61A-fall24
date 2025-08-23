; From video lecture: Programs as Data

(define (fact n)
    (if (= n 0) 1 (* n (fact (- n 1))))
)

(define (fact-exp n)
    (if (= n 0) 1 (list '* n (fact-exp (- n 1))))
)

; Exercise: Fib and Fib-exp