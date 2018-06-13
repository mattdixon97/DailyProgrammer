/*
Given a set of numbers, calculate using mathematical operations to solve for a target number.

https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/
*/

countdown(Nums, Target, Rslt) :-
  permutation(Nums, [X|Xs]),
  countdownSolver([X|Xs], Target, Z),
  Rslt = [X|Z].

countdownSolver([X], X, []).

countdownSolver([X,Y|Xs], Target, [Op,Y|Tail]) :-
  (Op = +; Op = -; Op = *; Op = /),
  S =.. [Op,X,Y],
  R is S,
  countdownSolver([R|Xs], Target, Tail).
