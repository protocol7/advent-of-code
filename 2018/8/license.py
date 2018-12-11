import sys

def parse_node(inp):
    msum = 0
    pos = 2
    for c in range(inp[0]):
        p, ms = parse_node(inp[pos:])
        pos += p
        msum += ms

    m_count = inp[1]
    msum += sum(inp[pos:pos + m_count])

    pos += m_count

    return pos, msum

line = sys.stdin.read().strip()
root = parse_node([int(x) for x in line.split()])

print(root[1])
