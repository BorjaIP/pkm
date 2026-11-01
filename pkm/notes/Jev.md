-
-
-


t
i
t
l
e
:
 
J
e
v


c
r
e
a
t
e
d
:
 
S
u
n
d
a
y
 
1
s
t
 
N
o
v
e
m
b
e
r
 
2
0
2
6
 
1
2
:
0
0


a
l
i
a
s
e
s
:


 
 
-
 
J
e
v
 
A
I


 
 
-
 
T
y
p
e
S
a
f
e
 
J
e
v


t
a
g
s
:


 
 
-
 
l
l
m


 
 
-
 
a
g
e
n
t
s


 
 
-
 
a
i


p
a
r
t
_
o
f
:


 
 
-
 
"
[
[
L
L
M
]
]
"


u
s
e
s
:


 
 
-
 
"
[
[
A
I
 
A
g
e
n
t
s
]
]
"


-
-
-


*
*
J
e
v
*
*
 
i
s
 
a
 
n
o
n
-
g
e
n
e
r
a
t
i
v
e
 
"
d
e
c
i
s
i
o
n
 
m
o
d
e
l
"
 
f
r
o
m
 
T
y
p
e
S
a
f
e
 
A
I
.
 
I
t
 
n
e
v
e
r
 
w
r
i
t
e
s
 
t
e
x
t
:
 
y
o
u
 
g
i
v
e
 
i
t
 
a
 
s
t
a
t
e
 
a
n
d
 
a
 
t
y
p
e
d
 
q
u
e
s
t
i
o
n
 
(
p
i
c
k
 
o
n
e
 
o
p
t
i
o
n
,
 
s
c
o
r
e
,
 
o
r
 
y
e
s
/
n
o
)
 
a
n
d
 
i
t
 
r
e
t
u
r
n
s
 
a
n
 
a
n
s
w
e
r
 
w
i
t
h
 
a
 
c
a
l
i
b
r
a
t
e
d
 
c
o
n
f
i
d
e
n
c
e
.
 
I
t
 
i
s
 
m
e
a
n
t
 
t
o
 
s
i
t
 
n
e
x
t
 
t
o
 
a
 
c
h
a
t
 
[
[
L
L
M
]
]
 
a
n
d
 
m
a
k
e
 
t
h
e
 
c
h
e
a
p
,
 
s
t
r
u
c
t
u
r
e
d
 
d
e
c
i
s
i
o
n
s
 
a
r
o
u
n
d
 
i
t
,
 
s
u
c
h
 
a
s
 
r
o
u
t
i
n
g
,
 
r
e
l
e
v
a
n
c
e
 
f
i
l
t
e
r
i
n
g
 
a
n
d
 
v
e
r
i
f
i
c
a
t
i
o
n
,
 
s
o
 
t
h
e
 
l
a
r
g
e
 
m
o
d
e
l
 
o
n
l
y
 
g
e
n
e
r
a
t
e
s
.




#
#
 
H
o
w
 
i
t
 
w
o
r
k
s




-
 
I
n
p
u
t
 
i
s
 
c
o
n
t
e
x
t
 
p
l
u
s
 
a
 
q
u
e
s
t
i
o
n
 
w
i
t
h
 
a
 
f
i
x
e
d
 
s
e
t
 
o
f
 
p
o
s
s
i
b
l
e
 
a
n
s
w
e
r
s
;
 
o
u
t
p
u
t
 
i
s
 
t
h
e
 
c
h
o
s
e
n
 
a
n
s
w
e
r
 
a
n
d
 
a
 
c
o
n
f
i
d
e
n
c
e
.


-
 
I
t
 
i
s
 
a
 
c
l
o
u
d
 
A
P
I
 
(
a
b
o
u
t
 
0
.
4
 
s
 
p
e
r
 
r
o
u
t
i
n
g
 
d
e
c
i
s
i
o
n
 
a
c
c
o
r
d
i
n
g
 
t
o
 
t
h
e
 
H
e
r
m
e
s
 
s
k
i
l
l
s
 
r
e
p
o
)
.
 
E
l
i
g
i
b
l
e
,
 
r
e
d
a
c
t
e
d
 
i
n
p
u
t
 
l
e
a
v
e
s
 
t
h
e
 
m
a
c
h
i
n
e
,
 
s
o
 
c
h
e
c
k
 
w
h
a
t
 
e
a
c
h
 
t
o
o
l
 
s
e
n
d
s
 
b
e
f
o
r
e
 
u
s
i
n
g
 
i
t
 
o
n
 
p
r
i
v
a
t
e
 
c
o
d
e
.


-
 
A
c
c
e
s
s
 
g
o
e
s
 
t
h
r
o
u
g
h
 
a
 
T
y
p
e
S
a
f
e
 
k
e
y
,
 
o
r
 
p
r
o
v
i
d
e
r
s
 
s
u
c
h
 
a
s
 
O
p
e
n
R
o
u
t
e
r
,
 
V
e
r
c
e
l
 
A
I
 
G
a
t
e
w
a
y
 
a
n
d
 
O
p
e
n
C
o
d
e
 
Z
e
n
.


-
 
W
h
e
n
 
t
h
e
 
k
e
y
 
i
s
 
m
i
s
s
i
n
g
,
 
t
h
e
 
c
a
l
l
 
t
i
m
e
s
 
o
u
t
 
o
r
 
c
o
n
f
i
d
e
n
c
e
 
i
s
 
l
o
w
,
 
t
h
e
 
t
o
o
l
s
 
b
e
l
o
w
 
f
a
l
l
 
b
a
c
k
 
t
o
 
s
a
f
e
 
d
e
f
a
u
l
t
s
 
(
k
e
e
p
 
t
h
e
 
c
u
r
r
e
n
t
 
m
o
d
e
l
,
 
r
e
t
u
r
n
 
t
h
e
 
o
r
i
g
i
n
a
l
 
l
i
s
t
)
.




#
#
 
T
y
p
i
c
a
l
 
u
s
e
s




|
 
U
s
e
 
|
 
W
h
a
t
 
J
e
v
 
d
e
c
i
d
e
s
 
|


|
 
-
-
-
 
|
 
-
-
-
 
|


|
 
M
o
d
e
l
 
r
o
u
t
i
n
g
 
|
 
W
h
i
c
h
 
m
o
d
e
l
 
i
s
 
g
o
o
d
 
e
n
o
u
g
h
 
f
o
r
 
e
a
c
h
 
t
u
r
n
 
|


|
 
M
e
m
o
r
y
 
|
 
W
h
i
c
h
 
r
e
t
r
i
e
v
e
d
 
p
a
s
s
a
g
e
s
 
a
r
e
 
w
o
r
t
h
 
r
e
a
d
i
n
g
,
 
a
n
d
 
w
h
i
c
h
 
h
i
d
e
 
i
n
s
t
r
u
c
t
i
o
n
s
 
|


|
 
C
o
m
p
a
c
t
i
o
n
 
|
 
W
h
i
c
h
 
t
u
r
n
s
 
t
o
 
k
e
e
p
 
w
h
e
n
 
a
 
t
r
a
n
s
c
r
i
p
t
 
m
u
s
t
 
b
e
 
c
u
t
 
|


|
 
S
k
i
l
l
 
s
e
l
e
c
t
i
o
n
 
|
 
W
h
i
c
h
 
i
n
s
t
a
l
l
e
d
 
s
k
i
l
l
 
a
 
t
u
r
n
 
n
e
e
d
s
,
 
i
f
 
a
n
y
 
|


|
 
C
o
d
e
 
s
e
a
r
c
h
 
|
 
W
h
i
c
h
 
f
o
l
d
e
r
s
,
 
f
i
l
e
s
 
a
n
d
 
d
e
c
l
a
r
a
t
i
o
n
s
 
a
r
e
 
r
e
l
e
v
a
n
t
 
t
o
 
a
 
q
u
e
s
t
i
o
n
 
|




#
#
 
T
o
o
l
s
 
b
u
i
l
t
 
o
n
 
J
e
v




|
 
T
o
o
l
 
|
 
D
e
s
c
r
i
p
t
i
o
n
 
|
 
I
n
s
t
a
l
l
 
|


|
 
-
-
-
 
|
 
-
-
-
 
|
 
-
-
-
 
|


|
 
[
j
e
v
g
r
e
p
]
(
h
t
t
p
s
:
/
/
g
i
t
h
u
b
.
c
o
m
/
d
z
h
n
g
/
j
e
v
g
r
e
p
)
 
|
 
C
L
I
 
(
`
j
g
`
)
 
t
h
a
t
 
f
i
n
d
s
 
r
e
l
e
v
a
n
t
 
f
i
l
e
s
 
a
n
d
 
s
o
u
r
c
e
 
e
x
c
e
r
p
t
s
 
f
o
r
 
n
a
t
u
r
a
l
-
l
a
n
g
u
a
g
e
 
c
o
d
e
 
q
u
e
s
t
i
o
n
s
;
 
r
e
t
u
r
n
s
 
e
v
i
d
e
n
c
e
 
f
o
r
 
t
h
e
 
c
a
l
l
i
n
g
 
a
g
e
n
t
,
 
n
o
t
 
a
n
 
a
n
s
w
e
r
 
|
 
`
n
p
m
 
i
n
s
t
a
l
l
 
-
g
 
@
d
z
h
n
g
/
j
e
v
g
r
e
p
`
,
 
t
h
e
n
 
`
j
g
 
a
u
t
h
`
 
a
n
d
 
`
j
g
 
s
k
i
l
l
`
 
|


|
 
[
h
e
r
m
e
s
-
j
e
v
-
s
k
i
l
l
s
]
(
h
t
t
p
s
:
/
/
g
i
t
h
u
b
.
c
o
m
/
k
e
r
p
o
p
u
l
e
/
h
e
r
m
e
s
-
j
e
v
-
s
k
i
l
l
s
)
 
|
 
J
e
v
-
p
o
w
e
r
e
d
 
r
o
u
t
i
n
g
,
 
m
e
m
o
r
y
,
 
c
o
m
p
a
c
t
i
o
n
 
a
n
d
 
s
k
i
l
l
 
s
e
l
e
c
t
i
o
n
 
f
o
r
 
[
[
H
e
r
m
e
s
]
]
,
 
C
l
a
u
d
e
 
C
o
d
e
 
a
n
d
 
C
o
d
e
x
;
 
1
3
 
p
l
a
i
n
 
`
S
K
I
L
L
.
m
d
`
 
f
i
l
e
s
 
|
 
`
g
i
t
 
c
l
o
n
e
`
,
 
t
h
e
n
 
`
p
y
t
h
o
n
3
 
i
n
s
t
a
l
l
.
p
y
`
 
a
n
d
 
`
j
e
v
 
s
e
t
u
p
-
k
e
y
`
 
|




-
 
*
*
j
e
v
g
r
e
p
*
*
 
n
e
e
d
s
 
N
o
d
e
.
j
s
 
2
2
+
 
a
n
d
 
u
n
d
e
r
s
t
a
n
d
s
 
d
e
c
l
a
r
a
t
i
o
n
s
 
i
n
 
P
y
t
h
o
n
,
 
T
y
p
e
S
c
r
i
p
t
/
J
a
v
a
S
c
r
i
p
t
,
 
G
o
 
a
n
d
 
R
u
s
t
.
 
I
t
 
s
k
i
p
s
 
h
i
d
d
e
n
,
 
d
e
p
e
n
d
e
n
c
y
,
 
b
u
i
l
d
,
 
b
i
n
a
r
y
 
a
n
d
 
l
i
k
e
l
y
 
c
r
e
d
e
n
t
i
a
l
 
f
i
l
e
s
 
b
y
 
d
e
f
a
u
l
t
.


-
 
*
*
h
e
r
m
e
s
-
j
e
v
-
s
k
i
l
l
s
*
*
 
i
n
t
e
g
r
a
t
e
s
 
f
u
l
l
y
 
w
i
t
h
 
[
[
H
e
r
m
e
s
]
]
 
t
h
r
o
u
g
h
 
a
 
p
l
u
g
i
n
;
 
f
o
r
 
C
l
a
u
d
e
 
C
o
d
e
 
a
n
d
 
C
o
d
e
x
 
i
t
 
i
n
s
t
a
l
l
s
 
t
h
e
 
s
k
i
l
l
s
 
a
n
d
 
e
d
i
t
s
 
`
~
/
.
c
l
a
u
d
e
/
C
L
A
U
D
E
.
m
d
`
 
a
f
t
e
r
 
b
a
c
k
i
n
g
 
i
t
 
u
p
 
(
`
-
-
n
o
-
c
l
a
u
d
e
-
m
d
`
 
s
k
i
p
s
 
t
h
a
t
)
.
 
S
t
a
r
t
 
r
o
u
t
i
n
g
 
i
n
 
s
h
a
d
o
w
 
m
o
d
e
 
(
`
/
j
e
v
 
r
o
u
t
i
n
g
 
s
h
a
d
o
w
`
)
,
 
w
h
i
c
h
 
l
o
g
s
 
d
e
c
i
s
i
o
n
s
 
w
i
t
h
o
u
t
 
s
w
i
t
c
h
i
n
g
 
m
o
d
e
l
s
.




#
#
 
C
a
v
e
a
t
s




-
 
M
o
s
t
 
n
u
m
b
e
r
s
 
(
s
p
e
e
d
,
 
c
o
s
t
 
c
u
t
s
)
 
c
o
m
e
 
f
r
o
m
 
T
y
p
e
S
a
f
e
 
a
n
d
 
t
h
e
 
t
o
o
l
 
a
u
t
h
o
r
s
;
 
i
n
d
e
p
e
n
d
e
n
t
 
v
e
r
i
f
i
c
a
t
i
o
n
 
w
a
s
 
n
o
t
 
f
o
u
n
d
.


-
 
T
h
e
 
h
e
r
m
e
s
-
j
e
v
-
s
k
i
l
l
s
 
r
e
p
o
 
i
t
s
e
l
f
 
r
e
p
o
r
t
s
 
t
h
a
t
 
a
 
J
e
v
-
d
i
g
e
s
t
 
h
a
n
d
o
f
f
 
r
e
c
a
l
l
e
d
 
l
e
s
s
 
t
h
a
n
 
a
 
p
l
a
i
n
 
t
r
a
n
s
c
r
i
p
t
,
 
s
o
 
i
t
s
 
d
e
f
a
u
l
t
 
h
a
n
d
s
 
o
f
f
 
t
h
e
 
w
h
o
l
e
 
d
i
a
l
o
g
u
e
.


-
 
B
a
c
k
g
r
o
u
n
d
:
 
T
y
p
e
S
a
f
e
 
c
a
m
e
 
o
u
t
 
o
f
 
s
t
e
a
l
t
h
 
i
n
 
S
e
p
t
e
m
b
e
r
 
2
0
2
6
 
w
i
t
h
 
a
 
r
e
p
o
r
t
e
d
 
$
4
0
M
 
s
e
e
d
 
(
[
A
n
a
l
y
t
i
c
s
 
V
i
d
h
y
a
]
(
h
t
t
p
s
:
/
/
w
w
w
.
a
n
a
l
y
t
i
c
s
v
i
d
h
y
a
.
c
o
m
/
b
l
o
g
/
2
0
2
6
/
0
9
/
j
e
v
-
e
x
p
l
a
i
n
e
d
/
)
)
.




-
-
-


R
e
l
a
t
e
d
:
 
[
[
H
e
r
m
e
s
]
]
,
 
[
[
A
I
 
A
g
e
n
t
s
]
]
,
 
[
[
A
g
e
n
t
 
S
k
i
l
l
s
]
]
,
 
[
[
L
L
M
]
]
,
 
[
[
T
e
r
m
i
n
a
l
]
]

