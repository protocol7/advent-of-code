s = "vtbrntöwkujjyluxbpwyrkyvbrkpupwöljoqjyp"
c = "abcdefghijklmnopqrstuvwxyzåäö"

print("".join(c[-c.index(x) - 1] for x in s))