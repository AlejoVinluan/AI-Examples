% Color predicate indicicating 4 colors
color(red).
color(blue).
color(yellow).
color(green).

% Different predicate ensuring 2 colors are different
different(X, Y) :-
    color(X),
    color(Y),
    X \= Y.

% Coloring predicate
%  M - Assignment
%  G - Graph
%   1st list - List of vertices
%   2nd List - (list of lists) Adjacency list of each vertex
%  SAMPLE - coloring(M,[[a,b],[[b],[a]]]).
coloring(M, G) :-
    complete(M, G),
    consistent(M, G).

% Complete creates all possible combinations of the graph
complete([], [[],[]]).
complete([paint(X, C) | T], [[X | T1], [_ | T2]]) :-
    color(C),
    complete(T, [T1, T2]).

% Consistent predicate ensuring graph is valid
consistent(_ , [[],[]]).


% Assign
assign([paint(X, C) | _], X, Xc).
assign([_ | R], X, Xc) :-
    assign(R, X, Xc).