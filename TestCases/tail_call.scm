; example from play list for EC of Scheme Project
; The last expression is not a tail call expression
(define (length s)
    (if (?null s) 0
        (+ 1 (length (cdr s))) ; frame is needed for each recurive call
    )
)

(define (length-tail s)
    (define (length-iter s n) ; like we define helper function
        (if (null? s) n
            (length-iter (cdr s) (+ 1 n))
        )
    )
    (length-iter s 0) ; tail call
)

; E.g., Reduce

(define (reduce procedure s start)
    (if (null? s) start
        (reduce procedure (cdr s) (procedure start (car s))) ; depends on the property of procedure
    )
)

; E.g., Map

(define (map procedure s)
    (if (null? s) nil
        (cons (procedure (car s)) ; not tail call context
            (map procedure (cdr s))
        )
    )
)

(define (map procedure s)
    (define (map-reverse s m)
        (if (null? s)
            m
            (map-reverse (cdr s)
                        (cons (procedure (car s)) m)) ; build list in a reversed manner
        )
    )
    (reverse (map-reverse s nil))
)

(define (reverse s)
    (define (reverse-iter s r)
        (if (null? s)
            r
            (reverse-iter (cdr s)
                        (cons (car s) r)
            )
        )
    )
    (reverse-iter s nil)
)