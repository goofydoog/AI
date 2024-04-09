__Zadanie 2__

*1*
    kobieta(X):-
        osoba(X),
        \+mezczyzna(X).

*2 - X jest ojcem Y*
    ojciec(X,Y):-
        osoba(X),
        osoba(Y),
        mezczyzna(X),
        rodzic(Y,X),
        X \= Y.

*3 - X jest matką Y*
    matka(X,Y):-
        osoba(X),
        osoba(Y),
        kobieta(X),
        rodzic(Y,X),
        X \= Y.

*4 - X jest córką Y*
    corka(X,Y):-
        osoba(X),
        osoba(Y),
        kobieta(X),
        rodzic(X,Y),
        X \= Y.

*5 - X jest rodzonym bratem Y*
    brat_rodzony(X,Y):-
        mezczyzna(X),
        ojciec(A,X),
        ojciec(A,Y),
        matka(B,X),
        matka(B,Y),
        X \= Y,
        A \= B,
        A \= X,
        A \= Y,
        B \= X,
        B \= Y.

*6 - X jest przyrodnim bratem Y*
    brat_przyrodni(X,Y):- 
        mezczyzna(X),
        rodzic(A,X),
        rodzic(A,Y),
        \+brat_rodzony(X,Y),
        X \= Y.


*7 - X jest kuzynem Y*
    kuzyn(X,Y):-
    osoba(X),
    osoba(Y),
    mezczyzna(X),
    rodzic(A,X),
    rodzic(B,Y),
    (brat_rodzony(A,B); brat_przyrodni(A,B)),
    X \= Y.


*8 - X jest dziadkiem od strony ojca dla Y*
    dziadek_od_strony_ojca(X,Y):-
        ojciec(A,Y),
        ojciec(X,A),
        X \= Y,
        A \= X,
        A \= Y.

*9 - X jest dziadkiem od strony matki dla Y*
    dziadek_od_strony_matki(X,Y):-
        matka(A,Y),
        ojciec(X,A),
        X \= Y,
        A \= X,
        A \= Y.

*10 - X jest dziadkiem Y*
    dziadek(X,Y):-
        dziadek_od_strony_ojca(X,Y);
        dziadek_od_strony_matki(X,Y).

*11 - X jest babcią Y*
    babcia(X,Y):-
        osoba(Y),
        rodzic(Y,A),
        matka(X,A),
        X \= Y,
        A \= X,
        A \= Y.

*12 - Y jest wnuczką X*
    wnuczka(X,Y):-
        kobieta(Y),
        (   
            dziadek(X,Y);
            babcia(X,Y)
        ).

*13 - X jest przodkiem Y do drugiego pokolenia wstecz*
    przodek_do2pokolenia_wstecz(X,Y):-
        osoba(X),
        osoba(Y),
        (   
            rodzic(Y,X);
            dziadek(X,Y);
            babcia(X,Y)
        ),
        X \= Y.

*14 - X jest przodkiem Y do trzeciego pokolenia wstecz*
    przodek_do3pokolenia_wstecz(X,Y):-
        przodek_do2pokolenia_wstecz(X,Y);
        (   
            rodzic(Y,A),
            A \= X,
            A \= Y,
            X \= Y,
            (
                dziadek(X,A);
                babcia(X,A)
            )
        ).