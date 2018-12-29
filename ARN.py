class ARN:
    def __init__(self, name):
        self.name = name
        self.filename = "DATA/" + name + "_interactions_FR3D.txt"
        self.bases = []
        self.interactions = []
        self.chain_id=""
        self.chain=""
        self.loops=[]

    def _get_bases(self):
        return self.bases

    def _set_bases(self, bases):
        self.bases = bases

    def _add_base(self, base):
        self.bases.append(base)

    def _get_interactions(self):
        return self.interactions

    def _set_interactions(self,interactions):
        self.interactions=interactions

    def _add_interaction(self,interaction):
        self.interactions.append(interaction)

    def _add_loop(self,loop):
        self.loops.append(loop)

    def __str__(self):
        return self.name
