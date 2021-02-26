#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter

def main():
    with open('a.txt', 'r') as exfile:
        data = exfile.readlines()
        (D, I, S, V, F) = [int(i) for i in data[0].split()]
        B = []
        E = []
        S_NAME = []
        L = []
        P = []
        d = dict()
        z = 1

        for i in range(S):
            (v, w, x, y) = [j for j in data[z].split()]
            B.append(v)
            E.append(w)
            S_NAME.append(x)
            L.append(y)
            z += 1

        z = 1
        d={i:[] for i in B}

        for i in range(S):
            (v, w, x, y) = [j for j in data[z].split()]
            d[w].append(x)
            z += 1

        for i in range(V):
            P.append(list(j for j in data[z].split()))
            z += 1

        with open('a_output.txt', 'w') as exwfile:
            pass


if __name__ == '__main__':
    main()
