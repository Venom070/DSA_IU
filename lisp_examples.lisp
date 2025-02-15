### **2. lisp_examples.lisp (Lisp Code File)**
This file will contain only the Lisp code examples.  

#### *Content:*  
```lisp
; Lisp Example: Arithmetic operation
(+ 1 2) ; Evaluates to 3

; Data structure example
(setq my-list '(1 2 3))
(car my-list) ; Access the first element: 1

; Recursion example - Factorial
(defun factorial (n)
  (if (= n 0) 1 (* n (factorial (- n 1)))))
(factorial 5) ; Output: 120

; Function example
(defun add (a b) (+ a b))
(add 5 10) ; Output: 15
