# Network Security Scanner

A Python-based network reconnaissance and vulnerability assessment tool built as part of the Network Security Implementation unit (ITNE2005R) at Victorian Institute of Technology.

## What it does

- **Host discovery** — resolves hostnames to IP addresses
- **Port scanning** — concurrent TCP scanning across common and custom port ranges
- **Service detection** — identifies services running on open ports
- **Banner grabbing** — captures service banners for version identification
- **Risk assessment** — flags critical and high-risk services with remediation notes
- **Report generation** — outputs plain-text and JSON reports

## Risk flags included

| Port | Service | Risk Level |
|------|---------|------------|
| 23 | Telnet | CRITICAL |
| 445 | SMB | CRITICAL |
| 6379 | Redis | CRITICAL |
| 27017 | MongoDB | CRITICAL |
| 21 | FTP | HIGH |
| 3389 | RDP | HIGH |
| 5900 | VNC | HIGH |
| 135 | MS-RPC | HIGH |

## Usage

```bash
# Scan using default common ports
python3 scanner.py 192.168.1.1

# Scan a custom port range
python3 scanner.py 192.168.1.1 1-1024

# Scan a hostname
python3 scanner.py scanme.nmap.org
```

## Output

The tool generates two output files per scan:
- `scan_TIMESTAMP.txt` — human-readable security report
- `scan_TIMESTAMP.json` — machine-readable results for further processing

## Example output

```
======================================================================
  NETWORK SECURITY SCAN REPORT
======================================================================
  Target       : 192.168.1.1 (192.168.1.1)
  Scan Time    : 2025-06-01T14:32:11
  Ports Scanned: 20
  Open Ports   : 3
  Critical     : 1
  High Risk    : 1
======================================================================

  OPEN PORTS & RISK ASSESSMENT
  ------------------------------------------------------------------
  Port  : 22/tcp  (SSH)
  State : OPEN
  Risk  : INFO
  Note  : No known critical risk.

  Port  : 80/tcp  (HTTP)
  State : OPEN
  Risk  : INFO
  Note  : No known critical risk.

  Port  : 445/tcp  (SMB)
  State : OPEN
  Risk  : CRITICAL
  Note  : SMB exposed. Associated with EternalBlue (CVE-2017-0144).
```

## Requirements

- Python 3.8+
- No external libraries required (standard library only)

## Skills demonstrated

- Network programming with Python `socket` library
- Concurrent execution with `ThreadPoolExecutor`
- Vulnerability assessment and risk rating methodology
- Security report writing
- CVE awareness and risk classification

## Disclaimer

This tool is intended for **authorised use only** on networks you own or have explicit permission to test. Unauthorised scanning is illegal.

---

*Shamama Nashrah Hossain — Bachelor of IT and Systems (Cybersecurity), VIT*
