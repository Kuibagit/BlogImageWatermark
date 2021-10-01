# BlogImageWatermark
Add watermark to blog images


待添加的图片放到目录：sourceimg\image\
水印图片放到目录：resources

修改 58行：
```python
draw.text((im.size[0] / 2, im.size[1] / 2), u'自定内容', fill=(0, 0, 0), font=font)
```

[usage] <input>
etc: python3 watermark.py all


****Reference****
https://zmister.com/archives/990.html
