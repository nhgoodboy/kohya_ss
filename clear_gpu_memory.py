#!/usr/bin/env python3
"""
GPU显存清理脚本
用于释放PyTorch和CUDA占用的GPU显存
"""

import gc
import torch

def clear_gpu_memory():
    """清理GPU显存"""
    print("🚀 开始清理GPU显存...")
    
    # 检查CUDA是否可用
    if not torch.cuda.is_available():
        print("❌ CUDA不可用，无法清理GPU显存")
        return
    
    # 显示清理前的显存状态
    print(f"📊 清理前GPU显存使用:")
    for i in range(torch.cuda.device_count()):
        allocated = torch.cuda.memory_allocated(i) / 1024**3  # GB
        reserved = torch.cuda.memory_reserved(i) / 1024**3    # GB
        print(f"   GPU {i}: 已分配 {allocated:.2f}GB, 已保留 {reserved:.2f}GB")
    
    # 清理步骤
    print("\n🧹 执行清理步骤:")
    
    # 1. 清空缓存
    print("   1. 清空CUDA缓存...")
    torch.cuda.empty_cache()
    
    # 2. 强制垃圾回收
    print("   2. 执行垃圾回收...")
    gc.collect()
    
    # 3. 同步CUDA操作
    print("   3. 同步CUDA操作...")
    torch.cuda.synchronize()
    
    # 4. 再次清空缓存
    print("   4. 再次清空缓存...")
    torch.cuda.empty_cache()
    
    # 显示清理后的显存状态
    print(f"\n📈 清理后GPU显存使用:")
    for i in range(torch.cuda.device_count()):
        allocated = torch.cuda.memory_allocated(i) / 1024**3  # GB
        reserved = torch.cuda.memory_reserved(i) / 1024**3    # GB
        print(f"   GPU {i}: 已分配 {allocated:.2f}GB, 已保留 {reserved:.2f}GB")
    
    print("\n✅ GPU显存清理完成!")

if __name__ == "__main__":
    clear_gpu_memory() 