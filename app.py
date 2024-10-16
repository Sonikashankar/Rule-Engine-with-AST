from flask import Flask, request, jsonify, send_from_directory
from rule_engine import create_rule, combine_rules, evaluate_rule, print_ast
from database import init_db, add_rule, get_all_rules, get_rule
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/rules', methods=['POST'])
def create_new_rule():
    data = request.json
    rule_string = data['rule']
    name = data['name']
    add_rule(name, rule_string)
    return jsonify({"message": "Rule created successfully"}), 201

@app.route('/api/rules', methods=['GET'])
def get_rules():
    rules = get_all_rules()
    return jsonify(rules)

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    rule_ids = data['rule_ids']
    user_data = data['user_data']
    
    try:
        rules = [get_rule(rule_id)[2] for rule_id in rule_ids]
        print(f"Rules to evaluate: {rules}")  # Debug print
        combined_rule = combine_rules(rules)
        if combined_rule is None:
            return jsonify({"error": "No valid rules to evaluate"}), 400
        
        print(f"Combined rule: {combined_rule}")  # Debug print
        result = evaluate_rule(combined_rule, user_data)
        print(f"Evaluation result: {result}")  # Debug print
        return jsonify({"result": result})
    except Exception as e:
        print(f"Error during evaluation: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/test_rules', methods=['GET'])
def test_rules():
    rule1 = "(age > 30 AND department = 'Sales') AND (salary > 50000 OR experience > 5)"
    rule2 = "(age < 25 AND department = 'Marketing') OR (salary > 60000 AND experience > 8)"
    
    ast1 = create_rule(rule1)
    ast2 = create_rule(rule2)
    
    print("AST for Rule 1:")
    print_ast(ast1)
    print("\nAST for Rule 2:")
    print_ast(ast2)
    
    combined_ast = combine_rules([rule1, rule2])
    print("\nCombined AST:")
    print_ast(combined_ast)
    
    test_data = {"age": 32, "department": "Sales", "salary": 55000, "experience": 6}
    result = evaluate_rule(combined_ast, test_data)
    
    return jsonify({
        "rule1": rule1,
        "rule2": rule2,
        "test_data": test_data,
        "evaluation_result": result
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
