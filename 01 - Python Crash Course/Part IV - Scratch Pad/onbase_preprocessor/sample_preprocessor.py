import os
import sys
import json
import logging

# Preprocessor Exit Codes (sys.exit):
# code | meaning
# -----+-----------------------------------
#  0   | Success
#  1   | Missing arguments
#  2   | Missing input file
#  3   | Missing output directory
#  4   | Processing error
#  5   | Load-time or general Python error

# Command-Line Arguments (sys.argv):
# index | argument
# ------+----------------------------------
#  0    | Program file path
#  1    | %I (input file)
#  2    | %O (output file)

class SamplePreprocessor(object):
    """Model for an example preprocessor"""

    def __init__(self) -> None:
        """Initialize the preprocessor"""
        try:
            app_dir = os.path.dirname(sys.argv[0])
            with open(os.path.join(app_dir, "config.json")) as f:
                settings = json.load(f)
            match settings["log_dir"].lower()[0]:
                case "r":
                    log_dir = app_dir
                case "l":
                    log_dir = os.path.join(app_dir, "logs")
                case _:
                    log_dir = settings["log_dir"]
            match settings["log_level"].lower()[0]:
                case "e":
                    log_level = logging.ERROR
                case "w":
                    log_level = logging.WARN
                case "i":
                    log_level = logging.INFO
                case _:
                    log_level = logging.DEBUG
            self.debug = log_level == logging.DEBUG
            logging.basicConfig(filename=os.path.join(log_dir, "sample_preprocessor.log"), filemode="a",
                                level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
            logging.info("Preprocessor initialized...")
        except Exception as e:
            sys.stderr.write("Error initializing application from config.json")
            sys.stderr.write(e)
            sys.exit(5)

    def process_file(self) -> int:
        """Preprocess the DIP file"""
        try:
            logging.info("Preprocessor started...")
            if len(sys.argv) < 3:
                logging.error("Input and output file command-line arguments are required!")
                return 1
            in_path, out_path = sys.argv[1], sys.argv[2]
            if not os.path.isfile(in_path):
                logging.error(f"Could not find input file: [{in_path}]")
                return 2
            if self.debug:
                logging.debug(f"Input File: [{in_path}]")
            out_dir = os.path.dirname(out_path)
            if not os.path.isdir(out_dir):
                logging.error(f"Could not find output directory: [{out_dir}]")
                return 3
            if self.debug:
                logging.debug(f"Output File: [{out_path}]")
            with open(in_path) as in_file, open(out_path, "w") as out_file:
                for line in in_file.readlines():
                    out_file.write(self.process_line(line))
            return 0
        except Exception as e:
            logging.error(e)
            return 4

    def process_line(self, line: str) -> str:
        """Process the current line from the source file"""
        # TODO: Perform some preprocessing logic on the line
        return(line)

def main():
    """Load and execute the preprocessor"""
    try:
        preprocessor = SamplePreprocessor()
        status = preprocessor.process_file()
        if status == 0:
            logging.info("Preprocessing completed successfully.")
            sys.stdout.write("Preprocessing completed successfully.")
        else:
            logging.error("Preprocessing failed!")
            sys.stderr.write("Preprocessing failed!")
        sys.exit(status)
    except Exception as e:
        sys.stderr.write("Error executing preprocessor")
        sys.stderr.write(e)
        sys.exit(5)

if __name__ == "__main__":
    main()
