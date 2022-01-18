import csv
import os
import glob

def convert(files):
    with open(files, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    nb_ligne=len(data)
    nb_colone = len(data[0])

    begin = r"\begin{tabular}{|*{"+str(nb_colone)+r"}{c|}}"

    result = open("{}.txt".format(files), "w")
    result.write(begin)
    result.write("\n" r"\hline")

    for i in range(nb_ligne) :
        result.write("\n")
        for j in range(nb_colone):
            result.write(str(data[i][j]))
            if j != nb_colone-1 :
                result.write(" & ")
        result.write(r"\\ \hline")
    result.write("\n" r"\end{tabular}")
    result.close


files=glob.glob('*.csv')
for object in files :
    convert(object)