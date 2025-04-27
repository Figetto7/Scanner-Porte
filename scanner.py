import socket
from typing import List
from logger import Logger

class Scanner:
    """
    Scanner TCP per porte aperte
    """
    def __init__(self, ip:str, startp:int=1, endp:int=1024):
        self.ip=ip
        self.startp=startp
        self.endp=endp
        self.logger=Logger()
    def scan(self) -> List[int]:
        """
        Scansiona le porte TCP su un IP
        Returns:
        Lista porte aperte trovate
        """
        openports=[]
        for port in range(self.startp, self.endp +1):
            if self._connect_port(port):
                openports.append(port)
        return openports
    
    def _connect_port(self, port:int)->bool:
        """
        Tentativo di connessione a porta TCP
        Args: porta da connettere
        Returns: bool: True se aperta, False se chiusa
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result=s.connect_ex((self.ip, port))
                if result==0:
                    self.logger.info(f"[OPEN] Porta {port}")
                    return True
        except Exception as e:
            self.logger.error(f"Errore sulla porta {port}:{e}")
        return False