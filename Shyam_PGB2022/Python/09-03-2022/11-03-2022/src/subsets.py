class Subsets:
    def sub_sets(self, xset):
        return self.subsetsRecur([], sorted(xset))

    def subsetsRecur(self, current, xset):
        if xset:
            return self.subsetsRecur(current, xset[1:]) + self.subsetsRecur(current + [xset[0]], xset[1:])
        return [current]


print(Subsets().sub_sets([4, 5, 6]))
