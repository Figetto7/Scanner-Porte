from scanner import Scanner
from report import ReportGenerator
from cli import ScanCLI

def main():
    args=ScanCLI.parse_arguments()
    scanner=Scanner(ip=args.ip, startp=args.start, endp=args.end)
    openports=scanner.scan()

    if openports:
        print(f"\n[+] Porte aperte su {args.ip}:{openports}")
    else:
        print("\n[-] Nessuna porta aperta trovata")
    report=ReportGenerator(output_file=args.output)
    report.generate(args.ip, openports)

if __name__=="__main__":
    main()