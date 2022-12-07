from matchers import And, HasAtLeast, HasFewerThan, PlaysIn,  Not, All, Or


class QueryBuilder():

    def __init__(self, matcher=All()):
        self.matcher_object = matcher

    def And(self):
        return And(self.matcher_object)

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher_object, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher_object, HasFewerThan(value, attr)))

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher_object, PlaysIn(team)))

    def Not(self):
        return Not(self.matcher_object)

    def All(self):
        return QueryBuilder(All())

    def build(self):
        return self.matcher_object

    def oneOf(self, query1, query2):

        return QueryBuilder(Or(query1, query2))