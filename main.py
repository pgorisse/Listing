import os
import glob
from interaction import Interaction
from base import Base
from loop import Loop
from ARN import ARN


dir_name="DATA2/"

for filename in os.listdir(dir_name):
    file=open(dir_name+filename,'r')
    print("file: "+dir_name+filename)

    #On construit l'objet ARN
    arn=ARN(filename.split("_")[0])
    file.readline()
    file.readline()
    chain=file.readline().split(" ")[1].rsplit('\t')
    chain_id=chain[0]
    chain=chain[1].rsplit('\n')[0]
    arn.chain=chain
    arn.chain_id=chain_id
    file.readline()

    #On ajoute les interactions a l'ARN
    for line in file:
        line=line.rsplit('\t')
        base1=Base(line[2],line[5])
        base2=Base(line[6],line[9].rsplit('\n')[0])
        interaction=Interaction(base1,line[1],base2)
        arn._add_interaction(interaction)

    #On ajoute les boucles a l'ARN
    expr="Catalog_results/loop."+arn.name+"*"
    for loop_file_name in glob.glob(expr):
        print("loop file: "+loop_file_name)
        loop_file=open(loop_file_name)
        loop=Loop(arn.name,arn.chain_id,loop_file.readline().split(":")[1].rsplit('\n')[0])
        loop_file.readline()
        loop_file.readline()
        for line in loop_file:
            line=line.rsplit('\t')
            base1=Base(line[0][:1],line[0][1:])
            base2=Base(line[2][:1],line[2][1:].rsplit('\n')[0])
            interaction=Interaction(base1,line[1],base2)
            loop.add_interaction(interaction)
        arn._add_loop(loop)
        loop_file.close()
        print(loop)
    file.close()





#ancient code:
# for filename in os.listdir(dir_name):
#     #open the .desc file
#     file=open(dir_name+filename,"r")
#     print("file: "+dir_name+filename)
#
#     #Skip th 4 first lines, keep list of bases
#     loop_id=file.readline().split(":")[1]
#     print("loop-id: "+loop_id)
#     bases = file.readline().split(sep=", ")
#     bases[0] = bases[0].split(sep=": ")[1]
#     bases[-1] = bases[-1][:len(bases[-1]) - 1]
#     print("bases: "+str(bases))
#     file.readline()
#
#     bases_dist=[]
#     for line in file:
#         line=line.rsplit('\t')
#         line[-1]=line[-1][:len(line[-1])-1]
#         if not line[0] in bases:
#             bases_dist.append(line)
#         if not line[2] in bases:
#             bases_dist.append(line)
#     file.close()
# print("bases distantes: "+str(bases_dist))