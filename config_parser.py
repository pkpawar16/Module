import yaml
import configparser
import json
import os


class ConfigParser:
    config = {}
    def read_config(self, file_path):
        """
        The `read_config` function takes two parameters: `file_path`, which is the path to the configuration file,
        and `file_format`, which represents the format of the configuration file.
        function is responsible for reading the configuration file and returning its contents.
        """
        _, file_extension = os.path.splitext(file_path)
        if file_extension == '.yaml':
            return self.read_yaml_config(file_path)
        elif file_extension == '.cfg':
            return self.read_cfg_config(file_path)
        elif file_extension == '.conf':
            return self.read_conf_config(file_path)
        else:
            raise ValueError(f"Unsupported configuration file format: {file_extension}")

    def read_yaml_config(self, file_path):
        """

        If the file format is YAML (`.yaml`), the function calls `read_yaml_config` to read the YAML file and
        returns the flattened dictionary representation of the config.
        """
        with open(file_path, 'r') as file:
            global config
            config = yaml.safe_load(file)
        return self.flatten_dict(config)

    def read_cfg_config(self, file_path):
        """
        If the file format is CFG (`.cfg`), the function calls `read_cfg_config` to read the CFG file and
        returns the dictionary representation of the config.
        """
        parser = configparser.ConfigParser()
        parser.read(file_path)
        config = {}
        for section in parser.sections():
            for key, value in parser.items(section):
                config[key] = value
        return config

    def read_conf_config(self, file_path):
        """

        If the file format is CONF (`.conf`), the function calls `read_conf_config` to read the CONF file and
        returns the dictionary representation of the config.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
            config = {}
            for line in lines:
                if line.strip() and not line.startswith('#'): # Skip empty and commented lines
                    key, value = line.strip().split('=')
            config[key] = value
        return config

    def write_config(self, config, file_path, file_format):
        """

        The `write_config` method takes three parameters: `config` (a dictionary containing configuration values),
        `file_path` (the path where the config file will be written), and `file_format`
        (the format in which the config file should be written).

        """
        if file_format == '.env':
            self.write_env_config(config, file_path)
        elif file_format == '.json':
            self.write_json_config(config, file_path)
        elif file_format == 'os':
            self.set_os_config(config)
        else:
            raise ValueError(f"Unsupported output file format: {file_format}")

    def write_env_config(self, config, file_path):
        """

        The `write_env_config` method opens the file in write mode using the `file_path` and writes each
        key-value pair from the `config` dictionary in the format of "key=value".
        """
        with open(file_path, 'w') as file:
            for key, value in config.items():
                file.write(f"{key}={value}\n")

    def write_json_config(self, config, file_path):
        """

        The `write_json_config` method opens the file in write mode using the `file_path` and
        uses the `json.dump` function with the `config` dictionary and the file object to write
        the dictionary in JSON format. It also indents the JSON for better readability.
        """
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)

    def set_os_config(self,config):
        """
        This method takes a `config` dictionary as an argument and sets environment variables based on
        the key-value pairs in the `config` dictionary.

        """

        for key, value in config.items():
            if isinstance(value, (list, tuple, set)):
                value = ','.join(str(v) for v in value)
                os.environ[str(key)] = str(value)

    def flatten_dict(self, d, parent_key='', sep='_'):
        """
        This function takes in a nested dictionary as input and returns a flattened version of the dictionary.
         The nested dictionary is flattened by concatenating the keys with a specified separator and
         returning a new dictionary with the flattened keys and corresponding values.

        :param d:the input dictionary
        :param parent_key:used for concatenating keys
        :param sep:the separator used for key concatenation).
        :return:new dictionary where the keys are flattened using a specified separator.
        """
        items = []

        for k, v in d.items():
            new_key = f'{parent_key}{sep}{k}' if parent_key else k
            if isinstance(v, dict):
               items.extend(self.flatten_dict(v, new_key, sep=sep).items())
            items.append((new_key, v))
        return dict(items)

if __name__ == "__main__":
    c = ConfigParser()
    c.read_config("sample.yaml")
    c.write_config(config, "sample.yaml", ".env")
    c.set_os_config(config)


