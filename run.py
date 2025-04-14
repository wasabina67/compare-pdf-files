from pdf2image import convert_from_path
from PIL import ImageChops, ImageStat


def pdf_to_images(path, dpi=300):
    return convert_from_path(path, dpi=dpi)


def main():
    sample1_pdf_path = "./docs/sample1.pdf"
    sample2_pdf_path = "./docs/sample2.pdf"

    sample1_images = pdf_to_images(sample1_pdf_path)
    sample2_images = pdf_to_images(sample2_pdf_path)

    if len(sample1_images) != len(sample2_images):
        print("PDFs have a different number of pages.")
        return

    for index in range(len(sample1_images)):
        img1 = sample1_images[index].convert("RGB")
        img2 = sample2_images[index].convert("RGB")
        diff = ImageChops.difference(img1, img2)

        stat = ImageStat.Stat(diff)
        if stat.sum == [0, 0, 0]:
            print(f"Page {index + 1}: No differences found.")
        else:
            print(f"Page {index + 1}: Differences detected.")
            diff.save(f"diff_page_{index + 1}.png")


if __name__ == "__main__":
    main()
