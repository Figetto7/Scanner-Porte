import argparse

class ScanCLI:
    """
    Parser CLI per Scan
    """
    @staticmethod
    def parse_arguments():
        parser=argparse.ArgumentParser(description="Scan - TCP Scanner")
        parser.add_argument("--ip",required=True, help="IP da scansionare")
        parser.add_argument("--start", type=int, default=1, help="Porta Iniziale")
        parser.add_argument("--end", type=int, default=1024, help="Porta finale")
        parser.add_argument("--output", default="report.txt", help="File di output")
        return parser.parse_args()