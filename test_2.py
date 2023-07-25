import os
import pytest
from config_parser import ConfigParser

@pytest.fixture
def config_reader():
    return ConfigParser()

def test_read_yaml_config(config_reader, tmp_path):
    # Create a temporary YAML file
    file_path = tmp_path / "sample.yaml"
    file_path.write_text("key: value")

    # Call the read_config function
    result = config_reader.read_config(file_path)

    # Assert that the result is correct
    assert result == {"key": "value"}



def test_read_cfg_config(config_reader, tmp_path):
    # Create a temporary CFG file
    file_path = tmp_path / "config.cfg"
    file_path.write_text("[Section]\nkey = value")

    # Call the read_config function
    result = config_reader.read_config(file_path)

    # Assert that the result is correct
    assert result == {"key": "value"}

def test_read_conf_config(config_reader, tmp_path):


    # Test cases Create a temporary CONF file
    file_path = tmp_path / "config.conf"
    file_path.write_text("key = value")

    # Call the read_config function
    result = config_reader.read_config(file_path)

    # Assert that the result is correct
    assert result == {"key": "value"}

def test_read_invalid_config_format(config_reader, tmp_path):
    # Create a temporary invalid file
    file_path = tmp_path / "config.txt"
    file_path.write_text("key = value")

    # Call the read_config function and assert that it raises a ValueError
    with pytest.raises(ValueError):
        config_reader.read_config(file_path)

def test_write_env_config(tmp_path, config_reader):
    # Test case for writing config in .env format:
    config = {
        'key1': 'value1',
        'key2': 'value2'
    }
    file_path = tmp_path / 'sample.yaml'
    file_format = '.env'
    config_reader.write_config(config, file_path, file_format)

    # Read the content of the file and check if it matches the expected output
    with open(file_path, 'r') as file:
        content = file.read()

    expected_content = 'key1=value1\nkey2=value2\n'
    assert content == expected_content

def test_write_json_config(tmp_path, config_reader):
    #Test case for writing config in .json format
    config = {
        'key1': 'value1',
        'key2': 'value2'
    }
    file_path = tmp_path / 'test.json'
    file_format = '.json'
    config_reader.write_config(config, file_path, file_format)

    # Read the content of the file and check if it matches the expected output
    with open(file_path, 'r') as file:
        content = file.read()

    expected_content = json.dumps(config, indent=4)
    assert content == expected_content

def test_set_os_config():
    #  Test case for setting config as environment variables:
    config = {'key1': 'value1', 'key2': 'value2'}

    ConfigParser().set_os_config(config)

    assert os.environ['key1'] == 'value1'
    assert os.environ['key2'] == 'value2'