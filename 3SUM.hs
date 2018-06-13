{-
Determine all subsets of length 3 that sum to zero

https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/
-}

module ThreeSum where

  import Data.List

  subsets :: [Int] -> [[Int]]
  subsets list = [ sublist | sublist <- subsequences list, (sum sublist) == 0, (length sublist) == 3 ]
