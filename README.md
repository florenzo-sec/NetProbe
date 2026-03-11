# NetProbe

A multithreaded TCP port scanner written in Python. NetProbe performs TCP connect scans against a target host, reporting which ports are open or closed with color-coded terminal output.

## Features

- TCP connect scanning with configurable port ranges
- Multithreaded scanning via `ThreadPoolExecutor` for concurrent port checks
- Flexible port specification: individual ports, ranges, or a mix of both
- Color-coded output (green for open, red for closed) using colorama
- Configurable thread pool size

## Requirements

- Python 3.x
- colorama (`pip install colorama`)

All other dependencies (`socket`, `argparse`, `concurrent.futures`) are part of the Python standard library.

## Installation

```bash
git clone <repository-url>
cd NetProbe
pip install colorama
```

## Usage

```
python netprobe.py <host> -p <ports> [-t <threads>]
```

### Arguments

| Argument | Flag | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `host` | positional | Yes | -- | Target hostname or IP address |
| `port` | `-p` / `--port` | Yes | -- | Ports to scan (see format below) |
| `threads` | `-t` / `--threads` | No | 10 | Max number of concurrent threads |

### Port Format

- Individual ports: `22,80,443`
- Range: `22-443`
- Mixed: `22,80-90,443,8080`

### Examples

```bash
# Scan specific ports
python netprobe.py 192.168.1.1 -p 22,80,443

# Scan a range of ports
python netprobe.py 192.168.1.1 -p 1-1024

# Scan with more threads
python netprobe.py 192.168.1.1 -p 1-1024 -t 50

# Mixed port specification
python netprobe.py 192.168.1.1 -p 22,80-90,443,8080 -t 20
```

### Sample Output

```
Scanning 192.168.1.1 using 10 threads.
[OPEN]    22
[CLOSED]  23
[OPEN]    80
[CLOSED]  443
```

## Project Structure

```
NetProbe/
├── netprobe.py      # Main entry point and port scanning logic
├── args.py          # CLI argument parsing and port format handling
├── requirements.txt # Python dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

### Module Overview

**`netprobe.py`** -- Contains the `port_scan(host, p)` function which creates a TCP socket, attempts a connection with a 2-second timeout, and prints the result. The main block orchestrates concurrent scanning using `ThreadPoolExecutor`.

**`args.py`** -- Contains two functions:
- `args()` -- Defines and parses CLI arguments via `argparse`.
- `parse_ports(ports_arg)` -- Converts the port string (e.g. `"22,80-90,443"`) into a list of integer port numbers.

## How It Works

1. CLI arguments are parsed to extract the target host, port specification, and thread count.
2. The port string is parsed into a list of individual port numbers.
3. A `ThreadPoolExecutor` is created with the specified number of worker threads.
4. For each port, a `port_scan` task is submitted to the thread pool.
5. Each task creates a TCP socket, sets a 2-second timeout, and calls `connect_ex()` on the target.
6. A return value of `0` means the port is open; any other value means it is closed.
7. Results are printed to the terminal with color coding.

## License

This project does not currently specify a license.
