import yaml
import re
import random


class FoodGrammar:
    def __init__(self, filename="grammar.yaml"):
        self.grammar_data = self.load_grammar_data(filename)
        # TODO: Run health check

    def load_grammar_data(self, filename):
        with open(filename, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc

    non_terminal_symbol_pattern = r"\$(\w+)"

    def replace_non_terminal_symbols(self, str, repl):
        return re.sub(self.non_terminal_symbol_pattern, repl, str)

    def random_replacement_for_non_terminal(self, non_terminal):
        if non_terminal in self.grammar_data:
            options = self.grammar_data[non_terminal]
            return random.choice(options)
        else:
            raise Exception("No substitutions found for ${}".format(non_terminal))

    def randomly_replace_non_terminal_symbols(self, str):
        return self.replace_non_terminal_symbols(
            str, lambda a: self.random_replacement_for_non_terminal(a[1])
        )

    def has_non_terminal_symbols(self, str):
        return "$" in str

    def recursive_random_replacement(self, str):
        while self.has_non_terminal_symbols(str):
            str = self.randomly_replace_non_terminal_symbols(str)
        return str

    def random_meal(self):
        return self.recursive_random_replacement("$meal")


if __name__ == "__main__":
    print(FoodGrammar().random_meal())
