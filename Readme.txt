
4. Listing
------------

Produces the listing of interaction motifs (distant interactions) of a RNA structure.
The algorithm is described in section 4.3.2 of the thesis.

================ INPUT: =====================================================
Two kinds of files are used:

1) The DATA/ folder contains annotations of the RNA structures produced by the annotation program FR3D.

It contains the sequence of the RNA, and the following information for every found interaction:

PDB_ID					The identifier of the RNA 3D data file in the "Protein Data bank" (PDB), search for it in https://www.rcsb.org/pdb if you want to visualize the molecule.
Interaction				The interaction type
Nucleotide_1_Base			The nucleotide 1 type (A,C,G,U)
Nucleotide_1_PDB_Number			Residue number of nucleotide 1 in the PDB file (useless for us)
Nucleotide_1_Chain			Chain that contains nucleotide 1 in the PDB file (useless for us)
Nucleotide_1_Sequence_Position		Position of nucleotide 1 in the sequence
Nucleotide_2_Base			The nucleotide 2 type (A,C,G,U)
Nucleotide_2_PDB_Number			Residue number of nucleotide 2 in the PDB file (useless for us)
Nucleotide_2_Chain			Chain that contains nucleotide 2 in the PDB file (useless for us)
Nucleotide_2_Sequence_Position		Position of nucleotide 2 in the sequence

Signification of the "interaction type" codes:
- For basepairs: c refers to cis, t refers to trans. W, H and S are the 3 sides of the RNA base that can interact with something. W refers to the Watson-Crick edge, H refers to the Hoogsteen (CH) edge, and S refers to the sugar edge of the base.
Then cWW is a "cis" basepair between the two "Watson-Crick" sides of the nucleotides 1 and 2.
A cWW interaction between A and U or G and C or G and U is called a "canonical basepair".
- For RNA backbone connectivity: c35, c53, c25 and c52 indicates that the two nucleotides are bound. This happens between consecutive nucleotides in the sequence.
- For RNA backbone conformations: things like 1a
- For base-phosphate interactions: things like BPh and BR (H_0BPh, W_6BR...) indicate that there is a hydrogen bond between a side of nucleotide 1 and the phosphate of nucleotide 2.
- For stacking ("empilement") interactions: s35, s53, s33, and s55. These mean that two nucleotides are stacked. It happens mostly between consecutive bases, but sometimes between distant ones, in particular in distant interaction motifs.

For more details on these codes, consult http://rna.bgsu.edu/FR3D/AnalyzedStructures/All/ were the data comes from.

2) The Catalog_results/ folder contains .desc files (naming convention: loop.PDB-id.chain-id.loop-id.desc). Each file describe a single loop identified in the RNA, with the position of nucleotides involved and the types of interactions.
Your algorithm iterates on these Catalog results elements.

	file: loop.1A1T.B.1.desc 
	<<<<<<<<<<<<<<<<
	loop-id:1
	bases: C208, G209, G210, A211, G212, G213
	#base1	interaction	base2
	A211	c35	G212
	G210	c35	A211
	G212	c35	G213
	C208	cWW	G213
	G209	s55	G213
	...
	>>>>>>>>>>>>>>>>
... etc for every interaction in the loop involving the loop base. 

================ OUTPUT : =====================================================
For each distant interaction motif, create a file following the .desc format:
- Which first lists the distant interactions,
- And then lists the different interacting local elements (interacting interfaces).

For example:

	file: dist.1A1T.B.1.desc  (naming convention : dist.PDB-id.chain-id.distant-id.desc)
	<<<<<<<<<<<<<<<<
	dist-id:1
	bases: G54, U63, C65, A69, A70
	#base1	interaction	base2
	G54	tsS	A69
	C65	csS	A69
	U63	cWH	A70
	
	#interacting interfaces:
	
	loop-id:1
	bases: A52, C53, G66, A67, U68, A69, A70, G71, C72, G105, A106, U107, U108, U109 
	#base1	interaction	base2
	U107	c35	U108
	A106	c35	U107
	G105	c35	A106
	C72	s55	A106
	C72	cWW	G105
	G71	cWS	U107
	G71	cWW	A106
	G71	c35	C72
		etc...
	
	loop-id:9
	bases: U55, G56, C57, C58, A59, A60, G61, C62, U63, G64
	#base1	interaction	base2
	C62	c35	U63
	G61	c35	C62
	A60	c35	G61
	A59	cSH	A60
	U55	cWW	G64
		etc...
	
	loop-id:pairing
	bases: G54, C65
	#base1	interaction	base2
	G54	cWW	C65	
	>>>>>>>>>>>>>>>>

In this example (note that the whole list of interactions is truncated with "etc..."), two local motifs from the catalogue are interacting together (loop 9 with base U63 and loop 1 with base A70) and with another portion of the RNA (a cWW basepair that did not belong to a catalog entry).

============= REPORT: ==========================================================
No report is required, you will be evaluated on:
- Program accuracy (it works/it works not):
	- input file parsing and graph building
	- research of distant interactions
	- distant motif reconstruction
- program speed (this is more a penalty if your code is obviously slower than what it should)

Your are not expected to run it over all example files in DATA/, they are just provided as examples.


Bonjour Pierrick,

Votre code doit repérer si les boucles d'un ARN, déjà listées par le module "catalogue",
 que vous prenez en entré interagissent entre elles au moyen d'interactions non canoniques.
L'algorithme est écrit en pseudocode français page 69 de la thèse, je peux paraphraser,
 mais c'est difficile de faire mieux.

- Chaque fichier *interactions_FR3D.txt liste toutes les interactions entre bases d'un
 ARN. Ces interactions sont de différents types (j'explique rapidement dans le fichier
  Readme.txt, mais une connaissance détaillée de la nature des interactions n'est pas
   nécessaire de toutes façons). Simplement, retenez que les interactions dites
    "canoniques" sont celles de type cWW entre un A et un U ou entre un G et un C
    ou entre un G et un U.
- Le module "catalogue" créé par certains de vos collègues scanne ce fichier pour en
 extraire les "loops" ou boucles et les isoler dans un fichier .desc : le fichier
  .desc liste les interactions entre bases d'une même boucle.
- La procédure "Listing" prend les différentes boucles d'un ARN en entrée, et
 cherche parmi les bases de ces boucles qui n'interagissent pas au sein de la boucle
 si par hasard elle n'interagiraient pas ailleurs à l'extérieur de la boucle (
 les "interactions non canoniques distantes ayant une extrémité dans BL").
La procédure rajoute aussi au motif d'interaction les bases proches de celles
interagissant à distance, si ces bases proches forment un empilement (ou "stacking"
en anglais, c'est à dire une interaction de type s35 ou s53 par exemple).

Chaque motif d'interaction identifié (appelé G dans le pseudo code) est ajouté à une
 liste que vous rendez à la fin du programme sous la forme d'autres fichiers .desc
  (un par motif distant), listant les interactions à distance entre bases, et rappelant
   plus bas celles des boucles qui interagissent dans ce motif distant ("interacting
    interfaces") à partir des fichiers .desc que vous avez utilisé en entrée.

Le "nouveau" site (déjà lui aussi obsolète) est à l'adresse http://rna3dmotif.lri.fr ,
 vous pouvez y jeter un oeil mais j'ai peur que ça vous embrouille (j'ai fait un
 effort de simplification pour le projet).
Un exemple de résultats de la procédure Listing :
 http://rna3dmotif.lri.fr/LISTING/index.html (Mais je ne vous en demande pas autant,
  je vous demande juste l'équivalent des fichiers .txt.) Dans l'exemple de ce lien,
  chaque motif distant trouvé se voit assigner un numéro de 1S72.0.0 à 1S72.0.96,
   les lettres servent à exprimer rapidement le type d'interactions non canoniques
   observées, et le fichier .txt est l'équivalent du .desc que je vous demande.
   Le fichier .pdb sert à visualiser en 3D la portion d'ARN concernée (non demandé).

Autre remarque : si vous n'êtes pas familiers avec le vocabulaire de la théorie des
 graphes (vertex, arête, étiquette, sous-graphe, etc...) dites le moi vite, il est
 évident que sans c'est incompréhensible.


Base libre: base ne réalisant pas d'interaction canonique
int. canonique: cWW entre AU, CG, GU, c53 et 35 pas interactions du tout, toutes les s** pas interactions.

-Identifier bases libres: dans un fichier interaction_fr3D, on cherche les bases ne réalisant pas d'interactions canoniques.
Parmis celle-ci, on sélectionne celles qui réalisent des int. non-canoniques, et distantes (l'interaction qu'elle réalise ne doit
pas se faire au sein d'une boucle déja listée.)
classe: ARN, Boucles, arrête