(define (line) (fd 50))
(define (twice fn) (fn) (fn))
(define (repeat k fn) 
  (fn) 
  (if (> k 1) (repeat (- k 1) fn)))

(define (tri fn) 
  (repeat 3 (lambra () (fn) (lt 120))))

; sierpinski triangle funtion with recursive depthd and size k
(define (sier d k) 
  (tri (lambda () (if (= d 1) (fd k) (leg d k)))))

(define (leg d k)
  (sier (- d 1) (/ k 2))
  (penup) (fd k) (pendown))