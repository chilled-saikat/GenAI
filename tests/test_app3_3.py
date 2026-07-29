import importlib.util
import pathlib
import unittest


class GenerateBotReplyTests(unittest.TestCase):
    def load_module(self):
        module_path = pathlib.Path(__file__).resolve().parents[1] / "app3.3.py"
        spec = importlib.util.spec_from_file_location("app3_3", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_returns_friendly_message_when_generate_content_fails(self):
        module = self.load_module()

        class FakeClient:
            class models:
                @staticmethod
                def generate_content(**kwargs):
                    raise RuntimeError("503 unavailable")

        result = module.generate_bot_reply("Hello", client_instance=FakeClient(), retries=1)

        self.assertIn("Sorry", result)
        self.assertIn("unavailable", result.lower())


if __name__ == "__main__":
    unittest.main()
