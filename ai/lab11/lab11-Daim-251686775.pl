% individuals
female(pam).
female(ann).
female(liz).
male(bob).
male(tom).
male(pat).
male(jim).
male(joe).

% relations
parent(pam, bob).
parent(bob, ann).
parent(bob, pat).
parent(tom, bob).
parent(tom, liz).
parent(pat, jim).
parent(joe, jim).

% parents
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

% grandparent fn
grandparent(X, Z) :-
    parent(X, Y),    % X is a parent of Y
    parent(Y, Z).    % Y is a parent of Z
