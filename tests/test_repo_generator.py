"""Regression tests for reproducible Kodi repository ZIPs."""
import hashlib
import os
from pathlib import Path
import tempfile
import unittest

import _repo_generator


class RepositoryZipTests(unittest.TestCase):
    def test_source_timestamps_do_not_change_generated_zip(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            addon = root / "service.introskip"
            addon.mkdir(parents=True)
            manifest = addon / "addon.xml"
            manifest.write_text("<addon id='service.introskip' />", encoding="utf-8")

            generator = _repo_generator.Generator.__new__(_repo_generator.Generator)
            generator.release_path = str(root)
            generator.zips_path = str(root / "zips")
            original = manifest.stat()
            output = Path(generator.zips_path) / "service.introskip" / "service.introskip-0.0.32.zip"

            try:
                generator._create_zip("service.introskip", "service.introskip", "0.0.32")
                first_hash = hashlib.sha256(output.read_bytes()).hexdigest()
                os.utime(
                    manifest,
                    ns=(original.st_atime_ns, original.st_mtime_ns + 2_000_000_000),
                )
                output.unlink()
                generator._create_zip("service.introskip", "service.introskip", "0.0.32")
                second_hash = hashlib.sha256(output.read_bytes()).hexdigest()
            finally:
                os.utime(manifest, ns=(original.st_atime_ns, original.st_mtime_ns))

            self.assertEqual(first_hash, second_hash)


if __name__ == "__main__":
    unittest.main()
