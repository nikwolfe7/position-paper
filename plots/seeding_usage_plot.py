#!/usr/bin/python

import matplotlib.pyplot as plt
#font = "Times New Roman"

plt.xlabel("Days Since Seeding Event")#, fontname=font)
plt.ylabel("Number of Call Interactions with Polly")#, fontname=font)


#plt.yscale("log")

def extract(filename):
    f = open(filename,"r")
    f = [item.strip().split() for item in f.readlines() if item.strip()]
    f = [(str(x),int(y)) for x,y in f]
    return f

def process(f):
    Xs = [x for x,y in f]
    Xs = range(len(Xs))

    Ys = [y for x,y in f]

    return Xs, Ys

def plot(filename, label, marker="o"):
    f = extract(filename)
    Xs, Ys = process(f)
    plt.plot(Xs, Ys, label=label, marker=marker, linewidth="3")
    return Xs, Ys

def preparePlot(Xs):
    XMAX = max(Xs)
    XMIN = min(Xs)
    plt.xlim(XMIN - 0.015*XMAX, 1.015*XMAX)

if __name__ == "__main__":
    filename1 = "seeding_game1.txt"
    label1 = "(2/10)  First In-Person"
    Xs1, Ys1 = plot(filename1, label1)

    filename2 = "seeding_game2.txt"
    label2 = "(3/4)    Second In-Person"
    Xs2, Ys2 = plot(filename2, label2)

    filename3 = "seeding_game3_coldseeding.txt"
    label3 = "(3/10)  Cold-Seeding attempt"
    Xs3, Ys3 = plot(filename3, label3)

    filename5 = "seeding_SMS2.txt"
    label5 = "(3/26)  SMS blast to 10,000 people"
    Xs5, Ys5 = plot(filename5, label5)
    
    filename4 = "seeding_game4_schoolchildren.txt"
    label4 = "(4/3)    In-Person with School Children"
    Xs4, Ys4 = plot(filename4, label4)

    
    Xs = Xs1 + Xs2 + Xs3 + Xs4 + Xs5
    preparePlot(Xs)
    
    plt.legend()
    #plt.show()
    plt.savefig("seeding_usage_plot.png", bbox_inches="tight")#, format="pdf")
