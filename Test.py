from cnocr import CnOcr

# ocr = CnOcr()  # 所有参数都使用默认值
# out = ocr.ocr("input\\4045-kirmaiu1893378.jpg")
#
# # 结果处理
# results = ''
# for output in out:
#     result = output['text']
#     results = results + str(result) + '\n'
# print(results)

# 创建 OCR 实例
ocr = CnOcr()

# 调用 OCR 方法
out = ocr.ocr('input\\4045-kirmaiu1893378.jpg')  # 去掉多余的参数

# 打印结果
for item in out:
    print(item)