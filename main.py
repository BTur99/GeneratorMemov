from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))

if text_type == 1:
    bottom_text = input('Введите нижний текст: ')
    top_text = ""
elif text_type == 2:
    top_text = input('Введите верхний текст: ')
    bottom_text = input('Введите нижний текст: ')
else:
    print('перезапустите программу')
    quit()

print(top_text, bottom_text)

memes = ['kot_like.jpg', 'kot_zloi.jpg', 'Кот_в_банке.jpg', 'sad_cat.jpg']

print('Выберите картинку для мема: ')
for i in range(len(memes)):
    print(i, memes[i])

meme_number = int(input('Введите номер картинки: '))
image = Image.open(memes[meme_number])
width, height = image.size

draw = ImageDraw.Draw(image)


font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)

draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill='black')

draw.text(((width - text[2]) / 2, (height - text[3] - 10)), bottom_text, font=font, fill='black')

image.save('new_meme.jpg')
