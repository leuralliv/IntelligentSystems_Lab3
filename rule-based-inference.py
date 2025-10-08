class RuleBasedInference:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_rules(self, antecedents, consequents):
        self.rules.append((antecedents, consequents))

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

    def forward_chaining(self):
        new_fact_found = True
        while new_fact_found:
            new_fact_found = False
            for ante, cons in self.rules:
                if self.evaluate_condition(ante) and cons not in self.facts:
                    self.facts.add(cons)
                    new_fact_found = True
                    print(f"Inferred new fact: {cons}")

        print("\nInference complete. Final facts:")
        for fact in sorted(self.facts):
            print(f"- {fact}")


if __name__ == "__main__":
    system = RuleBasedInference()

    # Normal rules
    system.add_rules("has_fur", "is_mammal")
    system.add_rules("has_feather", "is_bird")
    system.add_rules(["is_mammal", "eats_meat"], "is_carnivore")
    system.add_rules(["is_mammal", "has_hooves"], "is_ungulate")
    system.add_rules(["is_carnivore", "has_tawny_color", "has_dark_spots"], "is_cheetah")
    system.add_rules(["is_carnivore", "has_tawny_color", "has_black_stripes"], "is_tiger")
    system.add_rules(["is_ungulate", "has_long_neck", "has_long_legs"], "is_giraffe")
    system.add_rules(["is_ungulate", "has_black_stripes"], "is_zebra")
    system.add_rules("is_bird", "is_animal")
    system.add_rules("is_mammal", "is_animal")

    # Example rule with OR
    system.add_rules(["has_wings", "OR", "has_feather"], "can_fly")

    # Example rule with NOT
    system.add_rules(["has_scales", ["NOT", "is_mammal"]], "is_reptile")

    # Facts
    system.add_fact("has_fur")
    system.add_fact("has_black_stripes")
    system.add_fact("eats_meat")
    system.add_fact("has_tawny_color")
    system.add_fact("has_dark_spots")

    system.forward_chaining()
