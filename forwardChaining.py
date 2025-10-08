class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_rule(self, antecedent, consequent):
        self.rules.append((antecedent, consequent))

    def add_fact(self, fact):
        self.facts.add(fact)

    def evaluate_condition(self, condition):
        if isinstance(condition, list):
            if condition[0] == "NOT":
                return condition[1] not in self.facts

            if "OR" in condition:
                parts = [c for c in condition if c != "OR"]
                return any(self.evaluate_condition(c) for c in parts)

            return all(self.evaluate_condition(c) for c in condition)

        return condition in self.facts

    def forward_chain(self):
        new_fact_found = True
        while new_fact_found:
            new_fact_found = False
            for antecedent, consequent in self.rules:
                if self.evaluate_condition(antecedent) and consequent not in self.facts:
                    self.facts.add(consequent)
                    new_fact_found = True
                    print(f"Inferred new fact: {consequent}")

        print("\nInference complete. Final facts:")
        for fact in sorted(self.facts):
            print(f"  {fact}")


if __name__ == "__main__":
    system = RuleBasedSystem()

    # Basic rules (AND condition)
    system.add_rule("has_fur", "is_mammal")
    system.add_rule("has_feathers", "is_bird")
    system.add_rule("eats_grass", "is_ambivore")
    system.add_rule(["is_mammal", "eats_meat"], "is_carnivore")
    system.add_rule(["is_mammal", "has_hooves"], "is_ungulate")
    system.add_rule(["is_carnivore", "has_tawny_color", "has_dark_spots"], "is_cheetah")
    system.add_rule(["is_carnivore", "has_tawny_color", "has_black_stripes"], "is_tiger")
    system.add_rule(["is_ungulate", "has_long_neck", "has_long_legs"], "is_giraffe")
    system.add_rule(["is_carnivore","has_fur", "eats_meat"], "is_lion")
    system.add_rule(["is_ungulate", "has_black_stripes"], "is_zebra")
    system.add_rule("is_bird", "is_animal")
    system.add_rule("is_mammal", "is_animal")

    # Example rule with OR condition
    system.add_rule(["has_scales", "OR", "lays_eggs"], "is_reptile")
    system.add_rule(["lives_in_water", "OR", "has_gills"], "is_fish")
    system.add_rule(["has_beak", "OR", "can_fly"], "is_birdlike")
    system.add_rule(["is_carnivore", "OR", "is_reptile"], "is_predator")
    system.add_rule(["is_predator", "OR", "is_ambivore"], "is_hunter")
    system.add_rule(["can_fly", "OR", "is_birdlike"], "has_wingspan")
    system.add_rule(["is_ungulate", "OR", "is_carnivore"], "is_land_animal")

    # Example rule with NOT condition
    system.add_rule(["has_scales", ["NOT", "is_mammal"]], "is_reptile")
    system.add_rule(["NOT", "is_mammal"], "is_non_mammal")
    system.add_rule(["NOT", "is_aquatic"], "is_land_animal")
    system.add_rule(["is_mammal", ["NOT", "has_fur"]], "is_hairless_mammal")
    system.add_rule([["NOT", "is_reptile"], "is_cold_blooded"], "is_amphibian")
    system.add_rule(["is_animal", ["NOT", "is_fish"]], "is_land_animal")
    system.add_rule(["is_bird", ["NOT", "lays_eggs"]], "is_mutant_bird")
    system.add_rule(["NOT", "is_carnivore"], "is_non_predator")

    # Add facts
    system.add_fact("has_wings")
    system.add_fact("has_feathers")

    # system.add_fact("can_fly")
    # system.add_fact("eats_grass")

    # system.add_fact("eats_meat")
    # system.add_fact("is_mammal")

    

    system.forward_chain()
