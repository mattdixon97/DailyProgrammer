{-
Determine if there exists a subset of a set that sums to zero

https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/
-}

module SubsetSum where

  import Data.List

  subsetSum :: [Int] -> Bool
  subsetSum list
    | length (subsets list 0) > 0 = True
    | otherwise = False

  subsets :: [Int] -> Int -> [[Int]]
  subsets list num = [ sublist | sublist <- subsequences list, (sum sublist) == num, (length sublist) /= 0 ]
