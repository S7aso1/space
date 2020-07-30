#True
#False
#False
#True
#True
#True
#False
#True
#False
#False
#True
#False
#True
#False
>>> False:  not(f or t); not(t); False
>>> False:  not(t or f); not(t); False
#True
#True
>>> False:  f and (not (f or t)); f and (not(t)); f and f; False
#False

---------------------------------------------------------------------

not("sup" == "sup" or 1 > 0 )                      not(t or t); f
not("sup" == "sup" and 1 > 0 )                     not(t and t); f
1 != 0 and (not(1 < 2 or "str" == "str"))          t and (not(t or t)); f
1 == 1 and (not(1 > 2 and "str" != "str"))         t and (not (f and f)); t
not(10 != 10 or "ok" == "ok")                      not(f or t); f

"ted" == "ted" and not(0 == 1 or 1 == 1)           t and not(t or t); f
"ted" == "ted" and (0 == 1 or 1 == 1)              t and (f or t); t
"ted" != "ted" and not(0 == 1 and 1 == 1)          f and not(f and t); f
"ted" != "ted" and not(1 == 1 or 10 == 10)         f and not(t or t); f
"ted" != "ted" or (0 == 1 and 1 == 1)              f or (f and t); f
"ted" != "ted" or not(0 == 0 and 1 == 1)           f or not(t); f
not("ted" == "ted" and 1 == 0)                     not(t and f); t

1 != 4 and not("go" == "go" or 5 - 5 == 4 - 4)     t and not (t or t); f
1 != 4 and ("go" == "go" and 5 - 5 == 4 - 4)       t and (t and t); t
1 != 4 or not("go" == "go" or 5 - 5 == 4 - 1)      t or not(t or f); t
1 == 4 or not("go" == "go" and 5 - 5 == 4 - 1)     f or not(t and f); t
not("go" == "go" and 1 != 1) and not("go" == "go" and 5 - 5 == 4 - 4)    not(t and f) and not(t and t); t and f; f

not("ok" == "ok" or 1 == 1) and not (10 - 9 != 7-3 and "fire" == "fire")    not(t or t) and not(f and t); f and t; f
(16/4 == 20/5 and "how" == "how") or not(7-3 != 4 or "free == free")     (t and t) or not(f or t); t or not(t); t
(20/4 == 35/5 and "how" == "how") and not(7-3 == 4 or "free == free")    (f and t) and not(t or t); f and t; f
(16/4 == 20/5 and "how" == "how") or (7-3 != 4 or "free == free")        (t and t) or (f or t);t or t; t
(16/4 == 20/5 or "how" == "how") or (7-3 != 4 and "free != free")        (t or t) or (f and t);t or f; t
