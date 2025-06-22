#!/usr/bin/env python3
"""
修复训练数据标注中的触发词
将 'clay3d style' 替换为 'clay3dstyle_style'
"""

import os
from pathlib import Path

def fix_captions():
    """修复标注文件中的触发词"""
    
    dataset_dir = Path("dataset/5_clay3dstyle_style")
    
    if not dataset_dir.exists():
        print("❌ 数据集目录不存在")
        return
    
    txt_files = list(dataset_dir.glob("*.txt"))
    print(f"🔍 找到 {len(txt_files)} 个标注文件")
    
    fixed_count = 0
    
    for txt_file in txt_files:
        # 读取原始内容
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否需要修复
        if 'clay3d style' in content:
            # 替换错误的触发词
            new_content = content.replace('clay3d style', 'clay3dstyle_style')
            
            # 写回文件
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ 修复: {txt_file.name}")
            fixed_count += 1
        else:
            print(f"⏭️  跳过: {txt_file.name} (已正确)")
    
    print(f"\n🎯 修复完成! 共修复了 {fixed_count} 个文件")
    
    # 验证修复结果
    print("\n📋 修复后的标注示例:")
    sample_file = txt_files[0] if txt_files else None
    if sample_file:
        with open(sample_file, 'r', encoding='utf-8') as f:
            print(f"   {sample_file.name}: {f.read().strip()}")

if __name__ == "__main__":
    fix_captions() 