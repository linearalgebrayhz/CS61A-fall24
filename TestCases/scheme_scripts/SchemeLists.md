1. `cons`: two argument function that creates linked list
2. `car`: return the first element of a linked list
3. `cdr`: returns the rest of a list
4. `nil`: empty list

`(list? (cons 1 (cons 2 nil)))`

null?

```scm
(list 1 2 3 4)
```

List Processing
1. append
2. map
3. filter
4. apply: treat list as args to f