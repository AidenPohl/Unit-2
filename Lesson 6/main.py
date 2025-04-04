from PIL import Image, ImageFilter, ImageEnhance

orange_tabby = Image.open(r"Unit-2\Lesson 6\orange_tabby.jpg")
blurry_cat = orange_tabby.filter(ImageFilter.GaussianBlur(20))
"blurry_cat.show()"
bw_cat = ImageEnhance.Color(orange_tabby).enhance(0).show()

