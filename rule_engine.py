import re

class Node:
    def __init__(self, type, value, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

def tokenize(rule_string):
    return re.findall(r'\(|\)|AND|OR|[^()\s]+', rule_string)

def parse_rule(tokens):
    def parse_expression():
        if not tokens:
            return None
        if tokens[0] == '(':
            tokens.pop(0)  # Remove opening parenthesis
            left = parse_expression()
            if not tokens:
                return left
            op = tokens.pop(0)
            right = parse_expression()
            if tokens and tokens[0] == ')':
                tokens.pop(0)  # Remove closing parenthesis
            return Node('operator', op, left, right)
        else:
            condition = []
            while tokens and tokens[0] not in ['AND', 'OR', ')', '(']:
                condition.append(tokens.pop(0))
            return Node('condition', ' '.join(condition))

    return parse_expression()

def create_rule(rule_string):
    tokens = tokenize(rule_string)
    return parse_rule(tokens)

def combine_rules(rules):
    if not rules:
        return None
    if len(rules) == 1:
        return create_rule(rules[0])
    
    combined = create_rule(rules[0])
    for rule in rules[1:]:
        new_rule = create_rule(rule)
        combined = Node('operator', 'OR', combined, new_rule)
    
    return combined

def evaluate_condition(condition, data):
    attribute, operator, value = condition.split()
    if attribute not in data:
        return False
    
    if operator == "=":
        return str(data[attribute]) == value.strip("'")
    elif operator == ">":
        return float(data[attribute]) > float(value)
    elif operator == "<":
        return float(data[attribute]) < float(value)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

def evaluate_rule(node, data):
    if node is None:
        return False
    if node.type == 'condition':
        return evaluate_condition(node.value, data)
    elif node.type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    else:
        raise ValueError(f"Unknown node type: {node.type}")

def print_ast(node, indent=""):
    if node is None:
        return
    print(f"{indent}{node.type}: {node.value}")
    if node.left:
        print(f"{indent}Left:")
        print_ast(node.left, indent + "  ")
    if node.right:
        print(f"{indent}Right:")
        print_ast(node.right, indent + "  ")
