# Domain Checker

Check if domains are registered or available using python-whois.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Check domains from default file (domains.txt)
```bash
./check_domains.sh
```

### Check domains from a file
```bash
./check_domains.sh domains.txt
```

### Check a single domain
```bash
./check_domains.sh example.com
```

### Check multiple domains
```bash
./check_domains.sh example.com google.com test123xyz.com
```

Example `domains.txt`:
```
example.com
google.com
test123xyz.com
# Comments are ignored
```

## Output

```
example.com: not available
google.com: not available
test123xyz.com: available
```

## Python API

```python
from check_domain import is_domain_registered

if is_domain_registered("example.com"):
    print("Domain is registered")
else:
    print("Domain is available")
```
