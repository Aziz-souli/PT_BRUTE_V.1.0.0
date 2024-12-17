# PT_BRUTE: Path Traversal Bruteforce Tool

**PT_BRUTE** is a powerful command-line tool designed to perform **Path Traversal Bruteforcing** on web servers. It allows you to test for vulnerabilities by trying various file and path combinations while providing flexible options for logging, saving results, and proxy support.

## Installation

You can install **PT_BRUTE** using `pip` from TestPyPI or your local setup:

### From TestPyPI (if uploaded):
```bash
pip install -i https://test.pypi.org/simple/ PT_BRUTE
```

### From Source
Clone the repository and install the package locally:
```bash
git clone https://github.com/Aziz-souli/PT_BRUTE_V.1.0.0.git
cd PT_BRUTE_V.1.0.0
pip install .
```

### Verify Installation
Check if the tool is installed correctly:
```bash
PT_BRUTE -h
```

## Usage

Once installed, you can run **PT_BRUTE** from the terminal:

```bash
PT_BRUTE [-h] [-u URL] [-p PATH] [-l LOG] [-v {1,2,3}] [-CA CERT_PATH] [-A] [-Pr] [-S SAVE]
```

### Options

- `-h`, `--help`: Show the help message and exit  
- `-u URL`, `--url URL`: Target URL  
- `-p PATH`, `--PATH PATH`: Specify a file or path  
- `-l LOG`, `--log LOG`: Specify a log file  
- `-v {1,2,3}`, `--verbose`: Set verbosity level: `1` (low), `2`, `3` (high)  
- `-CA CERT_PATH`, `--cert_path`: CA certificate path  
- `-A`, `--ALL`: Try all combinations  
- `-Pr`, `--PROXY`: Enable proxy support  
- `-S SAVE`, `--SAVE SAVE`: Specify the path to save results  

### Example

1. **Basic Usage**: Perform a Path Traversal attack on a specific URL:
```bash
PT_BRUTE -u https://0a5800650490b8088034596000670052.web-security-academy.net/product?productId=1  -p directory-traversal-cheatsheat.txt -Pr -CA ~/.mitmproxy/mitmproxy-ca-cert.pem -S /home/aziz/Desktop/programming/
```**
```

## Requirements

- Python 3.6 or higher  
- Libraries:  
  - `requests` - For making HTTP requests  
  - `colorama` - For colored terminal text  
  - `beautifulsoup4` - For parsing HTML content  

## License

This project is licensed under the **MIT License**. See the `LICENSE.txt` file for details.

## Author

**Aziz Souli**  
Email: [aziz.souli@enicar.ucar.tn](mailto:aziz.souli@enicar.ucar.tn)  
GitHub: [https://github.com/Aziz-souli/PT_BRUTE_V.1.0.0](https://github.com/Aziz-souli/PT_BRUTE_V.1.0.0)
