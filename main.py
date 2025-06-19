# main.py

from rules_data import rules
from prettytable import PrettyTable

class ForwardChainingSystem:
    def __init__(self, initial_facts, rules):
        self.known_facts = set(initial_facts)
        self.rules = rules
        self.inferred_facts = set()
        self.trace = []

    def infer(self):
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                if rule["if"].intersection(self.known_facts) and rule["then"] not in self.known_facts:

                    self.known_facts.add(rule["then"])
                    self.inferred_facts.add(rule["then"])
                    self.trace.append((rule["if"], rule["then"]))
                    changed = True

    def show_results(self):
        table = PrettyTable()
        table.field_names = ["Rule Triggered (IF)", "Conclusion (THEN)"]
        for condition, conclusion in self.trace:
            table.add_row([", ".join(condition), conclusion])
        print("\n=== TRACE OF INFERENCES ===")
        print(table)

        print("\nFinal Inferred Facts:")
        print(", ".join(self.inferred_facts))


def input_symptoms():
    print("Masukkan gejala-gejala yang dialami (pisahkan dengan koma):")
    print("Contoh: demam, batuk, sakit_tenggorokan, pilek, mual, dll.")
    user_input = input(">> ").lower()
    symptoms = set(i.strip() for i in user_input.split(",") if i.strip())
    return symptoms

if __name__ == "__main__":
    print("=== Sistem Pakar Diagnosa Penyakit dengan Forward Chaining ===")
    facts = input_symptoms()
    system = ForwardChainingSystem(facts, rules)
    system.infer()
    system.show_results()
