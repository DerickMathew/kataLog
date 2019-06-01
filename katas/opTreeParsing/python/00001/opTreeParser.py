class OpTreeParser:
    def printEquation(self, treeJson):
        getLeft = lambda node : (
            self.printEquation(node['lhs'])
                if isinstance(treeJson['lhs'], dict) else node['lhs']
            )
        getOp = lambda node : node['op']
        getRight = lambda node : (
            self.printEquation(node['rhs'])
                if isinstance(treeJson['rhs'], dict) else node['rhs']
            )
        return getLeft(treeJson) + getOp(treeJson) + getRight(treeJson)

    def swapLhsAndRhs(self, treeJson):
        if not (treeJson['lhs'] and treeJson['rhs']):
            return treeJson
        return {
            'lhs': treeJson['rhs'],
            'op': treeJson['op'],
            'rhs':treeJson['lhs']
        }
