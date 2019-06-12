class CNF_Loader():

    chars = {'p', 'c'}

    def __init__(self, size):
        self.num_variables = 0
        self.variables = set()
        self.clauses = []
        self.size = size
        self.givens = 0


    def load_cnf(self, lines):
        lines = lines.split('\n')
        self.givens = len(lines[11989:]) - 1
        for l in lines:
            l = l.strip()
            if len(l) > 0 and l[0] not in self.chars:
                if l[-1] == '0':
                    cl = [int(l) for l in l.split()[:-1]]
                    self.variables.update([abs(l) for l in cl])
                    self.clauses.append(cl)



    def parse_cnf(self, file_name):
        with open(file_name, 'r') as f:
            self.load_cnf(f.read())
