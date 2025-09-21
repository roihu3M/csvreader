import pytest
from unittest.mock import patch

from app.main import *
from app.read_files import *

test_cases = [
    (
        [""],
        "the following arguments are required: --files, --report"
    ),
    (
        ["main.py", "--files", ""],
        "the following arguments are required: --report"
    ),
    (
        ["main.py", "--report", ""],
        "argument --report: invalid choice: '' (choose from student-performance)"
    ),
    (
        ["main.py", "--files", "", "--report"],
        "argument --report: expected one argument"
    ),
    (
        ["main.py", "--files", "", "--report", "123"],
        "argument --report: invalid choice: '123' (choose from student-performance)"
    ),
    (
        ["main.py", "--files", "--report", "student-performance"],
        ""
    ),
    (
        ["main.py", "--files", "students1.csv", "--report", "student-performance"],
        "student_name"
    )

]

@pytest.mark.parametrize("command, expected_output", test_cases)
def test_argparse(capsys, command, expected_output):
    with patch("sys.argv", command):
        try:
            main(command)
        except SystemExit:
            with pytest.raises(SystemExit):
                main(command)
        captured = capsys.readouterr()
        output = captured.out + captured.err
        print(output)
        assert expected_output in output



def test_file_processing_file_not_found():
    with pytest.raises(FileNotFoundError) as ex_info:
        file_processing_func('X:/asddsadsadsadasadsdsa')
    assert ex_info.type is FileNotFoundError
