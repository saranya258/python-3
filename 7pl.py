vt= input()
print(''.join([ vt[h:h+2][::-1] for h in range(0, len(vt), 2) ]))
