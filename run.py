from pdf2image import convert_from_path


def pdf_to_images(path, dpi=300):
    return convert_from_path(path, dpi=dpi)


def main():
    sample1_pdf_path = "sample1.pdf"
    sample2_pdf_path = "sample2.pdf"

    sample1_images = pdf_to_images(sample1_pdf_path)
    sample2_images = pdf_to_images(sample2_pdf_path)

    if len(sample1_images) != len(sample2_images):
        return


if __name__ == "__main__":
    main()
