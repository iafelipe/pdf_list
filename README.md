# PDF_list

A simple CLI tool that I made for myself using PyPDF that allows me to manipulate and merge PDF files using Python list-like indexing.

## Installation

If you want to use it, you can clone the repository and install it locally using pip:

```bash
git clone https://github.com/iafelipe/pdf_list.git
cd pdf_list
pip install .
```

## Usage

```
usage: pdf_list [-h] [-o OUTPUT] filename[index] [filename[index] ...]

Manipulate and merge PDF files using Python list-like indexing. 

indexing options:
  [start:stop:step]
  [start:stop]
  [start:]
  [:stop]
  [::step]
  [index1,index2,...] - no spaces
  [:], [] or no index (all pages)

note: 0-based indexing and exclusive stop

positional arguments:
  filename[index]             pdf file(s) with index (file extension is optional)

options:
  -h, --help                  show this help message and exit
  -o OUTPUT, --output OUTPUT  Output file name (default: out.pdf)
```

## Examples

### Concatenation

Concatenate all pages of file1.pdf and file2.pdf into a single file:

```bash
pdf_list file1.pdf file2.pdf
```

Concatenate the first 3 pages of file1.pdf and the second page of file2.pdf into a single file:
```bash
pdf_list file1.pdf[:3] file2.pdf[1]
```

### Slicing

Select the last page of file1.pdf and save it as last_page.pdf:
```bash
pdf_list file1.pdf[-1] -o last_page.pdf
```

Select the first and last pages of file1.pdf and save it as first_last.pdf:
```bash
pdf_list file1.pdf[0,-1] -o first_last.pdf
```

### Copying

Create a copy of file1.pdf and save it as copy.pdf:
```bash
pdf_list file1.pdf -o copy.pdf
```

## Troubleshooting

Depending on your system, you may need to separate the `file[index]` with quotes:
```bash
pdf_list "file1.pdf[:3]" "file2.pdf[1]"
```