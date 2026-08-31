import os
import pygame

# 1. 目标图片路径
img_path = r"D:\python代码汇总\alien_invasion\images\alien.bmp"

if not os.path.exists(img_path):
    print(f"❌ 未找到图片文件，请检查路径: {img_path}")
else:
    # 2. 初始化 pygame 并加载原图
    pygame.init()
    original_image = pygame.image.load(img_path)
    orig_rect = original_image.get_rect()
    print(f"📷 原图尺寸: 宽度 = {orig_rect.width} 像素, 高度 = {orig_rect.height} 像素")

    # 3. 计算等比例缩放（对于 1200x800 屏幕，外星人宽度设为 60 像素最合适）
    target_width = 60
    scale_ratio = target_width / orig_rect.width
    target_height = int(orig_rect.height * scale_ratio)

    # 4. 高质量平滑缩放
    resized_image = pygame.transform.smoothscale(
        original_image, (target_width, target_height)
    )

    # 5. 覆盖保存为 BMP 格式
    pygame.image.save(resized_image, img_path)
    print(
        f"✅ 缩放成功！新尺寸为: {target_width} x {target_height} 像素，已覆盖保存！"
    )