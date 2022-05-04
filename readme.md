NUM -> d
NUM -> NUM + d
HALF_FLOAT -> NUM + "."
FLOAT -> HALF_FLOAT + d
FLOAT -> FLOAT + d

SYMBOL -> symb(~"=", "*")
HALF_MULTIPLY -> "*"
POWER -> "*" + "*"
HALF_MULTIPLY -> "*"


ID -> alph
ID -> ID + alph
ID -> ID + NUM

SIGNLE_COMMENT -> #
SIGNLE_COMMENT -> SIGNLE_COMMENT + d
SIGNLE_COMMENT -> SIGNLE_COMMENT + alph
SIGNLE_COMMENT -> SIGNLE_COMMENT + sign

HALF_COMMENT -> "/*"
HALF_COMMENT -> "/*" + d
HALF_COMMENT -> "/*" + alph
HALF_COMMENT -> "/*" + sign
HALF_COMMENT -> "/*" + "\n"
HALF_COMMENT -> "/*" + d
MULTI_COMMENT -> HALF_COMMENT + "*/"
