MARKER = '''\
integration: Mark integration tests
unit: Mark unit tests
high: High Priority
medium: Medium Priority
low: Low Priority
'''

def pytest_configure(config):
    map(lambda line: config.addinivalue_line('markers',line),MARKER.split("\n"))

