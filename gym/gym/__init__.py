"""
OpenAI Gym simplified clone

Couple ways to run an operation:
  1. use gym.run(Operation)
  2. `python -m gym <filepath> [operation_var_name global-scope Operation]`
"""

from .environment import Environment, EnvironmentFactory, EnvironmentAbstractFactory
from .space import Space, UnlabelledSpace
from .strategy import Strategy
from .operation import Operation
from .view import View

def run(operation: Operation):
    return operation.operate()

if __name__ == "__main__":
    import runpy
    import sys
    def main(operation_file, operation_name="operation"):
        _globals = runpy.run_path(operation_file)
        return run(_globals[operation_name])
    main(*sys.argv[1:])