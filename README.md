# EU Covid-19 vaccine certificate unpack
Decode the EU Covid-19 vaccine certificate

## Prerequisites
For this script works, some libraries are necessary, to install them, type 
```bash
pip install base45, cbor2, zlib, cose, pyzbar
```

Additionally, on Mac you need [zbar](https://pypi.org/project/pyzbar/), it can be installed via `brew install zbar`.

## Usages
```
usage: index.py [-h] [-o] input

positional arguments:
  input         The image to read the QR code from

optional arguments:
  -h, --help    show this help message and exit
  -o, --output  Create a file with the decoded data
```


```bash
index.py -o ./myPass.png
```

## Example: 
Example on Emmanuel Macron's health pass: ( *"psss, using his pass will get you a heavy penalty --"* )

```json
{
    "1": "CNAM",
    "4": 1686693600,
    "6": 1629240036,
    "-260": {
        "1": {
            "v": [
                {
                    "ci": "URN:UVCI:01:FR:NR1EHPUK8IH0#I",
                    "co": "FR",
                    "dn": 1,
                    "dt": "2021-07-13",
                    "is": "CNAM",
                    "ma": "ORG-100030215",
                    "mp": "EU/1/20/1528",
                    "sd": 1,
                    "tg": "840539006",
                    "vp": "J07BX03"
                }
            ],
            "dob": "1977-12-21",
            "nam": {
                "fn": "MACRON",
                "gn": "EMMANUEL",
                "fnt": "MACRON",
                "gnt": "EMMANUEL"
            },
            "ver": "1.3.0"
        }
    }
}
```
