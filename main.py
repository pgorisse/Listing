import os
import glob
from interaction import Interaction
from base import Base
from loop import Loop
from ARN import ARN

data_folder = "DATA2/"


# Returns a list of ARN objects created from data files in dir_name
def parse(dir_name):
    print("#####PARSING#####")
    arn_list = []
    for filename in os.listdir(dir_name):
        file = open(dir_name + filename, 'r')
        print("file: " + dir_name + filename)

        # On construit l'objet ARN
        arn = ARN(filename.split("_")[0])
        file.readline()
        file.readline()
        chain = file.readline().split(" ")[1].rsplit('\t')
        chain_id = chain[0]
        chain = chain[1].rsplit('\n')[0]
        arn.chain = chain
        arn.chain_id = chain_id
        file.readline()

        # On ajoute les interactions et bases a l'ARN
        arn._set_bases()
        for line in file:
            line = line.rsplit('\t')
            base1 = Base(line[2], int(line[5]))
            base2 = Base(line[6], int(line[9].rsplit('\n')[0]))
            interaction = Interaction(base1, line[1], base2)
            arn._add_interaction(interaction)

        # On ajoute les boucles a l'ARN
        expr = "Catalog_results/loop." + arn.name + "*"
        for loop_file_name in glob.glob(expr):
            print("|\tloop file: " + loop_file_name)
            loop_file = open(loop_file_name)
            loop = Loop(arn.name, arn.chain_id, loop_file.readline().split(":")[1].rsplit('\n')[0])
            loop_file.readline()
            loop_file.readline()
            for line in loop_file:
                line = line.rsplit('\t')
                base1 = Base(line[0][:1], int(line[0][1:]))
                base2 = Base(line[2][:1], int(line[2][1:].rsplit('\n')[0]))
                interaction = Interaction(base1, line[1], base2)
                print("|\t|\tadding interaction " + str(interaction))
                loop.add_interaction(interaction)
            arn._add_loop(loop)
            loop_file.close()

        # On cherche les bases libres dans l'ARN
        for base in arn.bases:
            test = 0
            for interaction in arn.interactions:
                if int(base.number) == int(interaction.base1.number) and str(base.type) == str(
                        interaction.base1.type) and interaction.is_canonique():
                    test = 1
                elif int(base.number) == int(interaction.base2.number) and str(base.type) == str(
                        interaction.base2.type) and interaction.is_canonique():
                    test = 1
                if base.number == 497:
                    print(interaction,base)
            if test == 0:
                arn.bases_libres.append(base)
        file.close()
        arn_list.append(arn)
    print("#####FINISHED PARSING#####")
    return arn_list


arn_list = parse(data_folder)
for arn in arn_list:
    print("ARN: "+str(arn))
    print("bases libres: "+str([str(base) for base in arn.bases_libres]))

