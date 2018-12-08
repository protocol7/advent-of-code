import sys

def parse_node(inp):
    c_count = inp[0]
    m_count = inp[1]

    end_pos = 2
    children = []
    for c in range(c_count):
        ep, v = parse_node(inp[end_pos:])
        end_pos += ep
        children.append(v)

    metadata = inp[end_pos:end_pos + m_count]

    value = 0
    if children:
        for m in metadata:
            m -= 1
            if m < len(children):
                value += children[m]
    else:
        value = sum(metadata)

    end_pos += m_count

    return (end_pos, value)

line = sys.stdin.read().strip()

root = parse_node([int(x) for x in line.split()])

print(root[1])
