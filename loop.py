class Loop:
    def __init__(self, name, chain_id, id):
        self.interactions = []
        self.chain_id = chain_id
        self.bases = []
        self.name = name
        self.id = id
        self.filename = "Catalog_results/loop." + self.name + "." + self.chain_id + "." + self.id + ".desc"

    def _get_bases(self):
        return self.bases

    def _set_bases(self, bases):
        self.bases = bases

    def _add_base(self, base):
        self.bases.append(base)

    def _get_interactions(self):
        return self.interactions

    def _set_interactions(self, interactions):
        self.interactions = interactions

    def add_interaction(self, interaction):
        self.interactions.append(interaction)

    def __str__(self):
        return self.filename.split("/")[1]