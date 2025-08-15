(define (over-or-under num1 num2) 
   (if (> num1 num2)
      1
      (if (> num2 num1)
          -1
          0)))

(define (over-or-under-2 num1 num2) 
(cond ((> num1 num2) 1)
      ((> num2 num1) -1)
      (else 0)))

(define (make-adder num) (define (adder inc) (+ num inc)) adder)

(define (make-adder-1 num) (lambda (inc) (+ num inc)))

; ((make-adder-1 2) 3)

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n) (if (= n 0) (lambda (x) x) (composed (repeat f (- n 1)) f)))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) (if (zero? b) a (gcd b (modulo a b))))
