import itertools
class propositionalLogic:
    def_init_(self)
        self.clauses=[]
        def add_clauses(self,claues):
            self.clauses.append(clause)
            def p1_resolution(self):
                """Perform propositional logic resolution to determine satisfiability."""
                new = set()
                while True:
                    n= len(self.clauses)
                    pairs=[(self.clauses[i],self.clauses[j])for i in range(n) for j in range(i+1,n)]
                    for(ci,cj)in paris:
                        resolvents = self.pl_resolve(ci,cj)
                        if[] in resolvents:
                            return False
                        for res in resolvents:
                            new.add(tuple(res))
                    if new.issubset(set(map(tuple,self.clauses))):
                        return True
                    for clause in new:
                        if list(clause)not in self.clauses:
                            self.clauses.append(list(clause))
                            new = set()
                            def p1_resolsolve(self,ci,cj):
                                """Resolve two clauses to produce a set of resolvents."""
                                resolvents=[]
                                for di in ci:
                                    for dj in cj:
                                        if di==-dj:
                                            resolvent= list(set(ci)-{di})+list(set(cj)-{dj})
                                            resolvents.append(resolvent )
                                        return resolvents
                                    p1=propositionallogic()
                                    p1.add_clauses([1,2])
                                    p1.add_clauses([-1,3])
                                    p1.add_clauses([-2,-3])
                                    is_satisfiable = p1.p1_resolution()
                                    if is_satisfiable:
                                        print("the knowledge base is satisfiable.")
                                    else:
                                        print("the knowlwdge base is not satisfiable.")
                                        
