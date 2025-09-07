(define (curry-cook formals body) (if (null? (cdr formals))
                                            (list 'lambda formals body)
                                            (list 'lambda `(,(car formals)) (curry-cook (cdr formals) body))
))

(define (curry-consume curry args)
  (if (null? args)
    curry
    (curry-consume (curry (car args)) (cdr args))
  ))

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

; scm> (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
; (cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons `(equal? ,(car (cdr switch-expr)) ,(car option)) (cdr option)))
             (car (cdr (cdr switch-expr))))))
