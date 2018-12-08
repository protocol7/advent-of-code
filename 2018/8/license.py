import sys

def parse_node(inp):
    c_count = inp[0]
    m_count = inp[1]

    msum = 0
    end_pos = 2
    for c in range(c_count):
        ep, ms = parse_node(inp[end_pos:])
        end_pos += ep
        msum += ms

    msum += sum(inp[end_pos:end_pos + m_count])

    end_pos += m_count

    return (end_pos, msum)

line = sys.stdin.read().strip()
root = parse_node([int(x) for x in line.split()])

print(root[1])
