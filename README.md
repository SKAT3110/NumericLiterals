# Numeric Literals
Program utilizing deterministic finite automata to recognize numeric literals according to python 3.12 documentation

## Contributors 
### Group - Smurf Kat
Brenden Johnson - BVOLT <br>
Kevin Wenas - ssmckevin <br>
Colin Mcgough - aziac

## Task Division
Brenden Johnson - NFA & DFA Diagrams, Decimal Integer, Floating Point <br>
Colin McGough - Octal Integer Class <br>


## Decimal Integer

```python
decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"
```

### NFA

![alt text](NFADiagrams/DecIntNFA.jpg?raw=true)


## Octal Integer

```python
octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
octdigit     ::=  "0"..."7"
```

### NFA

![alt text](NFADiagrams/OctIntNFA.jpg?raw=true)


## Hexadecimal Integer

```python
hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
hexdigit     ::=  digit | "a"..."f" | "A"..."F"
digit        ::=  "0"..."9"
```

### NFA

![alt text](NFADiagrams/HexIntNFA.jpg?raw=true)


## Floating Point Literals

```python
floatnumber   ::=  pointfloat | exponentfloat
pointfloat    ::=  [digitpart] fraction | digitpart "."
exponentfloat ::=  (digitpart | pointfloat) exponent
digitpart     ::=  digit (["_"] digit)*
fraction      ::=  "." digitpart
exponent      ::=  ("e" | "E") ["+" | "-"] digitpart
digit         ::=  "0"..."9"
```

### NFA

![alt text](NFADiagrams/FloatingPointNFA.jpg?raw=true)
