import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  rule_string TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_rule(name, rule_string):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("INSERT INTO rules (name, rule_string) VALUES (?, ?)", (name, rule_string))
    conn.commit()
    conn.close()

def get_all_rules():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rules")
    rules = c.fetchall()
    conn.close()
    return rules

def get_rule(rule_id):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT * FROM rules WHERE id = ?", (rule_id,))
    rule = c.fetchone()
    conn.close()
    return rule
