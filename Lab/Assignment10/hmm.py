from sys import argv


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def transform(line):
    prob = []
    e = []
    for i in line:
        if isfloat(i):
            prob.append(float(i))
        else:
            e.append(True) if i == 't' else e.append(False)
    return prob, e


def cumulative_sum(a, b):
    x0, x1 = a
    y0, y1 = b
    return (x0*y0 + x1*y1), (x0*(1-y0) + x1*(1-y1))


def normalisation(a, b):
    return (a / (a + b)), (1 - (a / (a + b)))


def filtering(prob, e_arr):
    a, b, c, d, f = prob
    prevX = (a, 1 - a)

    for e in e_arr:
        if e:
            pE = (d, f)
        else:
            pE = (1 - d, 1 - f)
        s = cumulative_sum(prevX, (b, c))
        tmp = normalisation(pE[0] * s[0], pE[1] * s[1])
        prevX = tmp

    return prevX


def readFile(fname):
    with open(fname) as fp:
        lines = fp.readlines()
        for line in lines:
            prob, e = transform(line.strip().split(','))
            x, y = filtering(prob, e)
            print("{}--><{:.4f},{:.4f}>".format(line.strip(), x, y))


if __name__ == "__main__":
    #readFile('cpt.txt')
    readFile(argv[1])
