import os

import subprocess
import nbformat

_TEST_DIR = os.path.dirname(__file__)

_EXCLUDE = []

def _notebook_run(path):
    """Execute a notebook via nbconvert and collect output.
       :returns (parsed nb object, execution errors)
    """
    dirname, __ = os.path.split(path)
    os.chdir(dirname)

    in_fn = os.path.split(path)[-1].split('.')[0]
    temp_file_prefix = 'output_' + in_fn
    temp_file_out = temp_file_prefix + '.ipynb'

    args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
      "--ExecutePreprocessor.kernel_name=python",
      "--ExecutePreprocessor.timeout=None",
      "--output", temp_file_prefix, path]
    subprocess.check_call(args)

    nb = nbformat.read(temp_file_out, nbformat.current_nbformat, encoding='UTF-8')

    errors = [output for cell in nb.cells if "outputs" in cell
                     for output in cell["outputs"]\
                     if output.output_type == "error"]
    os.remove(temp_file_out)

    return nb, errors


def test_Welcome_to_TerrainBento():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "Welcome_to_TerrainBento.ipynb"))
    assert errors == []


def test_Introduction_to_terrainbento():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "example_usage/Introduction_to_terrainbento.ipynb"))
    assert errors == []


def test_introduction_to_boundary_conditions():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "example_usage/introduction_to_boundary_conditions.ipynb"))
    assert errors == []


def test_introduction_to_output_writers():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "example_usage/introduction_to_output_writers.ipynb"))
    assert errors == []


def test_model_basic_steady_solution():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "coupled_process_elements/model_basic_steady_solution.ipynb"))
    assert errors == []


def test_model_basic_var_m_steady_solution():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "coupled_process_elements/model_basic_var_m_steady_solution.ipynb"))
    assert errors == []


def test_model_basicCh_steady_solution():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "coupled_process_elements/model_basicCh_steady_solution.ipynb"))
    assert errors == []


def test_model_basicRt_steady_solution():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "coupled_process_elements/model_basicRt_steady_solution.ipynb"))
    assert errors == []


def test_model_basicVs_steady_solution():
    nb, errors = _notebook_run(os.path.join(_TEST_DIR, "coupled_process_elements/model_basicVs_steady_solution.ipynb"))
    assert errors == []
