import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Orange HRM'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'abubakar'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)



