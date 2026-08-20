import qrcode


def main():
    song = "https://www.youtube.com/watch?v=pry-ZU6StYk&list=RDpry-ZU6StYk&start_radio=1"
    qr = qrcode.QRCode(version = 1, box_size = 6, border = 5)
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color = "purple", back_color = "black")
    img.save("youtube-qr.png")

if __name__ == "__main__":
    main()
