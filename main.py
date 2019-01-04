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
            loop_bases = loop_file.readline().split(": ")[1].split(", ")
            loop_bases[-1] = loop_bases[-1].rsplit('\n')[0]
            loop.bases = [Base(b[:1], b[1:]) for b in loop_bases]
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
        file.close()
        arn_list.append(arn)
    print("#####FINISHED PARSING#####")
    return arn_list


def main():
    arn_list = parse(data_folder)
    for arn in arn_list:
        # On cherche les bases libres dans chaque boucle de l'ARN (BL)
        for loop in arn.loops:
            for base in loop.bases:
                test = 0
                for interaction in loop.interactions:
                    if base == interaction.base1 and interaction.is_canonique():
                        test = 1
                        print(interaction)
                    elif base == interaction.base2 and interaction.is_canonique():
                        test = 1
                        print(interaction)
                if test == 0:
                    loop.bases_libres.append(base)
            # On cherche les interactions non-canoniques distantes ayant une extrémité dans BL (ID)
            for base in loop.bases_libres:
                for interaction in arn.interactions:
                    if base == interaction.base1 or base == interaction.base2:
                        if interaction not in loop.interactions and interaction not in loop.interactions_dist \
                                and not interaction.is_canonique():
                            loop.interactions_dist.append(interaction)
    display(arn_list)


def display(arn_list):
    for i in range(len(arn_list)):
        print("ARN: " + str(arn_list[i]))
        for j in range(len(arn_list[i].loops)):
            print("Boucle: " + str(arn_list[i].loops[j]))
            print("Bases libres:" + str([str(bl) for bl in arn_list[i].loops[j].bases_libres]))
            print("Interactions distantes: " + str(
                [str(interaction) for interaction in arn_list[i].loops[j].interactions_dist]))


main()
