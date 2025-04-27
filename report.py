from typing import List
from logger import Logger

class ReportGenerator:
    """
    Generatore di report delle porte aperte
    """
    def __init__(self, output_file:str="report.txt"):
        self.output_file=output_file
        self.logger=Logger()
    def generate(self, ip:str, openports:List[int])->None:
        """
        Scrive un report su file
        Args: IP scansionato, Lista porte aperte
        """
        try:
            with open(self.output_file, "w") as f:
                f.write(f"Scan Report\n")
                f.write(f"Target:{ip}\n")
                f.write(f"Open Ports:\n")
                for port in openports:
                    f.write(f"- Porta {port}\n")
            self.logger.info(f"Report salvato in {self.output_file}")
        except Exception as e:
            self.logger.error(f"Errore generando report {e}")
