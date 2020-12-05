#!/usr/bin/env python3

def find_location(rows, line, marker):
    if len(rows) == 1:
        return rows.start
    return find_location(
        (range(rows.start, rows.start + (rows.stop - rows.start) // 2) if line.pop(0) == marker 
            else range(rows.stop - (rows.stop - rows.start) // 2, rows.stop)), 
        line, 
        marker
    )

with open('input.txt') as f:
    ids = sorted(
        [
            (find_location(range(0, 128), line[0:7], 'F') * 8) + find_location(range(0, 8), line[7:10], 'L') 
            for line in ((list(l.strip())) for l in f.readlines())
        ]
    )
    print([x for x in range(ids[0], ids[-1] + 1) if x not in ids][0])
    
