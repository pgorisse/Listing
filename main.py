import os

dir_name="catalog2/"

for filename in os.listdir(dir_name):
    #open the .desc file
    file=open(dir_name+filename,"r")
    print("file: "+dir_name+filename)

    #Skip th 4 first lines, keep list of bases
    loop_id=file.readline().split(":")[1]
    print("loop-id: "+loop_id)
    bases = file.readline().split(sep=", ")
    bases[0] = bases[0].split(sep=": ")[1]
    bases[-1] = bases[-1][:len(bases[-1]) - 1]
    print("bases: "+str(bases))
    file.readline()

    bases_dist=[]
    for line in file:
        line=line.rsplit('\t')
        line[-1]=line[-1][:len(line[-1])-1]
        if not line[0] in bases:
            bases_dist.append(line)
        if not line[2] in bases:
            bases_dist.append(line)
    file.close()
print("bases distantes: "+str(bases_dist))