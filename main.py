import os
import sys
import numpy
import sysconfig
import colorama
import asyncio
from inputf.process import input_handler
import inputf.process


def main():
    pass  # Replace With Function Body.


def _process() -> None:
    inputf.process.out_basic_console_start("App")
    inputf.process.handle(input_handler(">>"))


if __name__ == '__main__':
    main()
    _process()  # Safely Close Out any running Processes Inside of main().
