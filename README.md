# ABAP-NotepadPP

> Professional Notepad++ User Defined Language (UDL) for ABAP / SAP S/4HANA 2023

## Overview

ABAP-NotepadPP is an open-source project that generates a professional User Defined Language (UDL) for Notepad++ from a structured database of ABAP language elements.

Instead of manually editing the XML file, this project automatically generates it from YAML definitions.

The objective is to provide complete syntax highlighting support for modern ABAP, including:

- ABAP 7.58
- SAP S/4HANA 2023
- Open SQL
- Constructor Expressions
- CDS
- RAP
- AMDP
- ABAP Cloud
- Built-in Functions
- Built-in Types

---

## Project Status

Current version:

```
v0.1.0-alpha.1
```

Project state:

- [x] Repository created
- [ ] Build engine
- [ ] YAML parser
- [ ] XML generator
- [ ] First importable UDL
- [ ] Open SQL
- [ ] CDS
- [ ] RAP
- [ ] Release 1.0

---

## Project Structure

```
ABAP-NotepadPP
│
├── build.py
├── pyproject.toml
├── requirements.txt
│
├── keywords/
│
├── templates/
│
├── dist/
│
├── docs/
│
├── tests/
│
└── src/
    └── abap_notepadpp/
```

---

## Requirements

- Python 3.11 or newer

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Build

Generate the Notepad++ UDL:

```bash
python build.py
```

The generated XML will be available in:

```
dist/ABAP_S4HANA2023.xml
```

---

## Roadmap

### Version 0.1

- Project bootstrap
- YAML database
- XML generator
- Importable UDL

### Version 0.2

- Complete ABAP Statements
- Open SQL

### Version 0.3

- Constructor Expressions

### Version 0.4

- CDS

### Version 0.5

- RAP

### Version 0.6

- ABAP Cloud

### Version 1.0

Complete support for SAP S/4HANA 2023 syntax.

---

## License

MIT License

---

## Contributing

Contributions are welcome.

Please open an Issue before submitting a Pull Request for significant changes.

---

## Author

Jesus Gonzalez

```
