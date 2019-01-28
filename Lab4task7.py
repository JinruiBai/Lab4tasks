import os

def sed(pattern, replacement, fin, fout):
    finMem = open(fin)
    foutMem = open(fout, 'w+')
    for line in finMem:
        if pattern in line:
            print 'pattern found'
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)

if __name__ == '__main__':
    print os.getcwd()
    pattern = 'oy'
    replacement = 'it'
    fin = "/home/matt/projects/Skools_Kool/Chapter_14/Exercise2_Test.txt"
    fout = "/home/matt/projects/Skools_Kool/Chapter_14/Exercise2_Out.txt"
    sed(pattern, replacement, fin, fout)
