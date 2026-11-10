import contextlib
import importlib.util
import io
import json
from pathlib import Path
import unittest
from unittest import mock


spec = importlib.util.spec_from_file_location("deploy_macos", Path(__file__).resolve().parents[1] / "cmake/single-app/deploy_macos.py")
deployer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deployer)


class DeploymentReportTests(unittest.TestCase):
    def test_default_report_is_output_not_a_file(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            deployer.emit_report({"qmlModules": [], "compact": True})
        self.assertEqual(json.loads(output.getvalue()), {"qmlModules": [], "compact": True})

    def test_requested_report_is_written_through_provider(self):
        with mock.patch.object(deployer, "write_report_file") as writer:
            deployer.emit_report({"compact": False}, Path("resources/report.json"))
        writer.assert_called_once_with(Path("resources/report.json"), '{\n  "compact": false\n}\n')
