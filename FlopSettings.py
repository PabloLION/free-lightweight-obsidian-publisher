import dotenv, json, os
from datetime import datetime

global SETTINGS  # SETTINGS for .env
global RULE  # RULE for flop_rule.json
global RULE_PATH
SETTINGS = {"VAULT_PATH": "", "OUTPUT_PATH": "", "ATTACHMENT_PATH": ""}
NECESSARY_ENV = ["VAULT_PATH"]
PATH_INPUT_PROMPT = {
    "VAULT_PATH": "Full Path of your obsidian vault? (saving into .env)"
}


def get_global_setting(setting_name):
    global SETTINGS
    SETTINGS[setting_name] = dotenv.get_key(".env", setting_name) or ""
    if SETTINGS[setting_name] == "" and setting_name in NECESSARY_ENV:
        SETTINGS[setting_name] = input(PATH_INPUT_PROMPT["VAULT_PATH"]) or ""
        dotenv.set_key(".env", setting_name, SETTINGS[setting_name])
        print(f'{setting_name} = "{SETTINGS[setting_name]}" saved.')
    return SETTINGS[setting_name]


def get_flop_rule_path():
    global RULE_PATH
    RULE_PATH = os.path.join(SETTINGS["VAULT_PATH"], ".obsidian", "flop_rule.json")
    return RULE_PATH


def get_vault_rule():
    global SETTINGS
    global RULE_PATH
    global RULE
    get_global_setting("VAULT_PATH")
    RULE_PATH = get_flop_rule_path()
    if not os.path.exists(RULE_PATH):
        with open(RULE_PATH, "w") as f:
            json.dump({"createStamp": datetime.now().timestamp()}, f)
    with open(RULE_PATH) as f:
        RULE = json.load(f)
        f.close()
    return RULE


def test():
    global SETTINGS
    get_global_setting("VAULT_PATH")
    get_vault_rule()
    print("SETTINGS:")
    print(SETTINGS)
    print("RULE:")
    print(RULE)


if __name__ == "__main__":
    test()
