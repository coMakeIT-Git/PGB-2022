class SubLists:
    def sub_sets(self, x):
        return self.subsetsRecur([], sorted(x))

    def subsetsRecur(self, current, x):
        if x:
            return self.subsetsRecur(current, x[1:]) + self.subsetsRecur(current + [x[0]], x[1:])
        return [current]

x=list(map(int, (input().split())))
print(SubLists().sub_sets(x))
