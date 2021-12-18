import dotenv, json, os
from datetime import datetime

NECESSARY_ENV = ["vault_path"]
PATH_INPUT_PROMPT = {
    "vault_path": "Full Path of your obsidian vault? (saving into .env)"
}


class FlopSetting:
    def __init__(self):

        # ENV for .env
        # RULE for flop_rule.json
        # SETTINGS for
        self.env = {"vault_path": ""}
        self.rule = {"vault_path": ""}
        self.setting = {
            "vault_path": "./",
            "output_path": "./",
            "attachment_path": "./",
        }
        self.rule_path = ""
        self.get_env_setting("vault_path")
        self.setting.update(self.env)
        self.get_flop_rule_path()
        self.get_vault_rule()
        self.setting.update(self.rule)

    def get_env_setting(self, setting_name):
        self.env[setting_name] = dotenv.get_key(".env", setting_name) or ""
        if self.env[setting_name] == "" and setting_name in NECESSARY_ENV:
            self.env[setting_name] = input(PATH_INPUT_PROMPT["vault_path"]) or ""
            dotenv.set_key(".env", setting_name, self.env[setting_name])
            print(f'{setting_name} = "{self.env[setting_name]}" saved.')
        return self.env[setting_name]

    def get_flop_rule_path(self):
        self.rule_path = os.path.join(
            self.env["vault_path"], ".obsidian", "flop_rule.json"
        )
        return self.rule_path

    def get_vault_rule(self):
        self.get_env_setting("vault_path")
        self.rule_path = self.get_flop_rule_path()
        if not os.path.exists(self.rule_path):
            with open(self.rule_path, "w") as f:
                json.dump({"createStamp": datetime.now().timestamp()}, f)
        with open(self.rule_path) as f:
            self.rule = json.load(f)
            f.close()
        return self.rule


if __name__ == "__main__":
    # for mod test
    flop_setting = FlopSetting()
    flop_setting.get_env_setting("vault_path")
    flop_setting.get_vault_rule()
    print("ENV:")
    print(flop_setting.env)
    print("RULE:")
    print(flop_setting.rule)
    print("SETTINGS:")
    print(flop_setting.setting)
