# Scanner-Porte
Un  piccole Scanner Porte in Python
## Funzionalità
Scansione di porte TCP su IP specifici.
Range di porte personalizzabile.
Report dei risultati su file.
Log degli eventi (sia su file che su console).
Interfaccia a linea di comando (CLI) intuitiva.
## Installazione
Assicurati di avere Python 3.7+ installato.
git clone https:[//github.com/tuo-username/scan-tcp-scanner.git](https://github.com/Figetto7/Scanner-Porte.git)
## Utilizzo
Esegui il programma passando i parametri desiderati:python main.py --ip 192.168.1.1 --start 20 --end 100 --output risultato.txt
## Parametri 
--ip : (obbligatorio) IP da scansionare.
--start : Porta iniziale da cui partire (default: 1).
--end : Porta finale da cui terminare (default: 1024).
--output : Nome del file di output del report (default: report.txt).
