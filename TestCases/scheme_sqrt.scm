(define (square x)
    (* x x))

(define (average x y)
    (/ (+ x y) 2))

(define (sqrt x)
    (define (update guess)
        (if (= (square guess) x)
            guess
            (update (average guess (/ x guess)))))
    (update 1))

(define (plus4 x)
    (+ x 4))

;(define plus4 (lambda (x) (+ x 4)))

((lambda (x y z) (+ x y (square z))) 1 2 3)