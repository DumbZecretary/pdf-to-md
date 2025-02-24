# https://github.com/VikParuchuri/marker?tab=readme-ov-file
from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered


class Converter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Converter, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.config_parser = ConfigParser({
                "output_format": "markdown",
                "ADDITIONAL_KEY": "VALUE"
            })
            self.converter = PdfConverter(
                config=self.config_parser.generate_config_dict(),
                artifact_dict=create_model_dict(),
                processor_list=self.config_parser.get_processors(),
                renderer=self.config_parser.get_renderer(),
                llm_service=self.config_parser.get_llm_service()
            )
            self.initialized = True

    def execute(self, pdf_path: str | bytes) -> str | None:
        try:
            if isinstance(pdf_path, bytes):
                with open("temp.pdf", "wb") as f:
                    f.write(pdf_path)
                    execute_path = "temp.pdf"
            elif isinstance(pdf_path, str):
                execute_path = pdf_path
            else:
                return None
            rendered = self.converter(execute_path)
            text, _, images = text_from_rendered(rendered)
            return text
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
