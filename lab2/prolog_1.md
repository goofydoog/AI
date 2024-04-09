__Zadanie 1.1__

a)
    Rodzeństwo, dwie osoby, X i Y, są połączone bezpośrednio z tymi samymi dwoma osobami, więc są rodzeństwem.

b)
    Kuzyn, X i Y są kuzynami, ponieważ ich rodzice są rodzeństwem.

c)
    Wspołdziadkowie, X i Y są współdziadkami dla tej samej osoby, ponieważ oboje mają wspólnego wnuka.

d)
    Macocha, Y jest macochą X, ponieważ jest partnerką rodzica X, ale nie jest biologicznym rodzicem.

e)
    Przyrodnie rodzenstwo, X i Y są przyrodnim rodzeństwem, mają wspólnego jednego rodzica, ale drugie rodzice są różni.

f)
    Szwagier, Y jest szwagrem X, bo jest w związku małżeńskim z rodzeństwem X.

g)
    Wujek (brat rodzica) i przyrodnie rodzeństwo.


__Zadanie 1.2__

a)
    *anna i jakub to rodzice michala i karola.*
    rodzic(michal,anna).
    rodzic(michal,jakub).
    rodzic(karol,anna).
    rodzic(karol,jakub).

b)
    *marek to rodzic ewy i tomasza, ewa to rodzic olafa, a tomasz to rodzic filipa.*
    rodzic(ewa,marek).
    rodzic(tomasz,marek).
    rodzic(olaf,ewa).
    rodzic(filip,tomasz).

c)
    *aleksander to rodzic henryka, grzegorz to rodzic eweliny, henryk i ewelina to rodzice jakuba*
    rodzic(henryk,aleksander).
    rodzic(ewelina,grzegorz).
    rodzic(jakub,henryk).
    rodzic(jakub,ewelina).
d)
    *ignacy to rodzic andrzeja i antoniego, beata to rodzic antoniego*
    rodzic(andrzej,ignacy).
    rodzic(antoni,ignacy).
    rodzic(antoni,beata).
e)
    *elżbieta to rodzic agnieszki, monika to rodzic krzysztofa, piotr to rodzic agnieszki i krzysztofa*
    rodzic(agnieszka,elżbieta).
    rodzic(krzysztof,monika).
    rodzic(agnieszka,piotr).
    rodzic(krzysztof,piotr).
f)
    *łukasz i karolina to rodzice maksymiliana, sebastian to rodzic karoliny i nikodema*
    rodzic(maksymilian,łukasz).
    rodzic(maksymilian,karolina).
    rodzic(karolina,sebastian).
    rodzic(nikodem,sebastian).
g)
    *dariusz to rodzic broniława i cypriana, anita to rodzic broniława i wiktoria, wiktoria to rodzic cypriana*
    rodzic(broniław,dariusz).
    rodzic(cyprian,dariusz).
    rodzic(broniław,anita).
    rodzic(wiktoria,anita).
    rodzic(cyprian,wiktoria).

h)
    *Definicja reguły, która określa, kiedy dwie osoby są rodzeństwem.*
    rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(Y, A),
    rodzic(X, B),
    rodzic(Y, B),
    X \= Y,
    A \= X,
    A \= Y,
    B \= X,
    B \= Y,
    B \= A.

i)
    *Ta reguła definiuje, kiedy dwie osoby, X i Y, są kuzynami.*
    kuzyn(X, Y) :-
    rodzic(A, C),
    rodzic(B, C),
    rodzic(X, A),
    rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

j)
    *Ta reguła definiuje, kiedy dwie osoby, X i Y, są współdziadkami, co oznacza, że dzielą wspólnego wnuka, ale ich dzieci (rodzice tego wnuka) nie są tymi samymi osobami.*
    wspoldziadkowie(X, Y) :-
    rodzic(A, X),
    rodzic(B, Y),
    rodzic(C, A),
    rodzic(C, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.

k)
    *Ta reguła definiuje relację, w której X jest macochą lub ojczymem Y.*
    macocha(X, Y) :-
    rodzic(X, A),
    rodzic(B, A),
    rodzic(B, Y),
    \+rodzic(X ,Y),
    \+rodzic(Y, X),
    A \= X,
    A \= Y,
    A \= B,
    B \= X,
    B \= Y,
    B \= A,
    X \= Y.
l)
    *Ta reguła określa, kiedy dwie osoby, X i Y, są przyrodnim rodzeństwem, czyli mają wspólnego jednego rodzica, ale każde z nich ma innego drugiego rodzica.*
    przyrodnie_rodzenstwo(X, Y) :-
    rodzic(X, A),
    rodzic(X, B),
    rodzic(Y, A),
    rodzic(Y, C),
    \+rodzic(X, C),
    \+rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.
m)
    *Ta reguła określa, kiedy dwie osoby, X i Y, są szwagrami. Definicja szwagra może obejmować zarówno*
    *męża siostry jak i brata żony, dlatego ta reguła sprawdza dwa scenariusze za pomocą konstrukcji alternatywnej*
    szwagier(X, Y) :-
    (   
    	(   
        	rodzic(A, X),
    		rodzic(A, B),
    		rodzic(B, C),
    		rodzic(Y, C),
    		\+rodzic(A, C),
    		\+rodzic(C, A),
    		\+rodzic(X, Y),
   			\+rodzic(Y, X)
        );
    	(
        	rodzic(A, Y),
    		rodzic(A, B),
    		rodzic(B, C),
    		rodzic(X, C),
    		\+rodzic(A, C),
    		\+rodzic(C, A),
    		\+rodzic(X, Y),
   			\+rodzic(Y, X)
        )
    ),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.
n)
    *Ta reguła definiuje bardzo nietypowy typ relacji rodzinnej, dziwne_rodzenstwo.*
    *W tej konfiguracji, X i Y mają wspólnego rodzica B, ale drugi rodzic Y (C) jest jednocześnie dzieckiem drugiego rodzica X (A).*
    dziwne_rodzenstwo(X, Y) :-
	rodzic(X, A),
    rodzic(X, B),
    rodzic(C, A),
    rodzic(Y, C),
    rodzic(Y, B),
    A \= X,
    A \= Y,
    A \= B,
    A \= C,
    B \= X,
    B \= Y,
    B \= A,
    B \= C,
    C \= A,
    C \= B,
    C \= X,
    C \= Y,
    X \= Y.





