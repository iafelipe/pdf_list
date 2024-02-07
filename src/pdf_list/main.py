import argparse
from argparse import RawTextHelpFormatter
from typing import BinaryIO

from pypdf import PageRange, PdfWriter


def get_pdf(filename: str) -> BinaryIO:
    return open(f"{filename}", "rb")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pdf_list",
        description="""Manipulate e merge PDF files using list-like indexing \n\nindexing options:
  [start:stop:step]
  [start:stop]
  [start:]
  [:stop]
  [::step]
  [index1,index2,...] - no spaces
  [:], [] or no index (all pages)\n
note: 0-based indexing and exclusive stop""",
        formatter_class=lambda prog: RawTextHelpFormatter(prog, max_help_position=30),
        epilog="example: pdf-list file.pdf[1:3] file2.pdf[::2] file3.pdf[1,3,5] -o newfile.pdf",
    )

    parser.add_argument(
        "filename",
        nargs="+",
        help="pdf file(s) with index (file extension is optional)",
        metavar="filename[index]",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file name (default: %(default)s)",
        default="out.pdf",
    )

    args = parser.parse_args()
    merger = PdfWriter()

    for file in args.filename:
        filename, _, i = file.partition("[")
        i = i.removesuffix("]")

        if ".pdf" not in filename:
            filename = filename + ".pdf"

        try:
            pdf = get_pdf(filename)

        except FileNotFoundError:
            print(f"File {filename} not found!")
            return

        if i == "":
            pages = PageRange(":")
        else:
            if "," in i:
                pages = eval(f"[{i}]")
            else:
                pages = PageRange(i)

        merger.append(pdf, pages)

    output_filename = args.output
    if ".pdf" not in output_filename:
        output_filename = output_filename + ".pdf"

    output_pdf = open(f"{output_filename}", "wb")
    merger.write(output_pdf)

    merger.close()
    output_pdf.close()


if __name__ == "__main__":
    main()
