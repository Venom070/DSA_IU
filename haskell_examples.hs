-- Haskell Example: Arithmetic operation
1 + 2 -- Evaluates only when required

-- Data structure example
myList = [1, 2, 3]
head myList -- Access the first element: 1

-- Recursion example - Factorial
factorial 0 = 1
factorial n = n * factorial (n - 1)
factorial 5 -- Output: 120

-- Function example
add :: Int -> Int -> Int
add a b = a + b
add 5 10 -- Output: 15
