 # -*- coding: utf-8 -*-
"""
Flux LoRA 训练配置文件 - 带中文注释版本
该文件包含了 Flux LoRA 训练的所有配置参数及其详细说明
"""

flux_training_config = {
    # === 基础模型配置 ===
    "LoRA_type": "Flux1",  # LoRA 类型，指定为 Flux1 模型
    "LyCORIS_preset": "full",  # LyCORIS 预设模式，"full" 表示完整模式
    "pretrained_model_name_or_path": "D:/workspace/models/flux/flux1-dev.safetensors",  # 预训练模型路径
    "ae": "D:/workspace/models/flux/ae.sft",  # 自编码器（AutoEncoder）模型路径
    "clip_l": "D:/workspace/models/flux/clip_l.safetensors",  # CLIP 文本编码器模型路径
    "t5xxl": "D:/workspace/models/flux/t5xxl_fp16.safetensors",  # T5 文本编码器模型路径
    "vae": "",  # VAE 模型路径（空表示使用默认）
    
    # === 训练基础参数 ===
    "learning_rate": 0.0003,  # 学习率，控制模型参数更新的步长
    "unet_lr": 0.0003,  # UNet 网络的学习率
    "text_encoder_lr": 0,  # 文本编码器的学习率（0表示不训练文本编码器）
    "t5xxl_lr": 0,  # T5 文本编码器的学习率
    "optimizer": "AdamW8bit",  # 优化器类型，AdamW8bit 节省显存
    "optimizer_args": "",  # 优化器额外参数
    "lr_scheduler": "constant",  # 学习率调度器类型
    "lr_scheduler_args": "",  # 学习率调度器参数
    "lr_scheduler_num_cycles": 1,  # 学习率调度器循环次数
    "lr_scheduler_power": 1,  # 学习率调度器功率
    "lr_scheduler_type": "",  # 学习率调度器类型（额外）
    "lr_warmup": 0,  # 学习率预热步数
    "lr_warmup_steps": 0,  # 学习率预热步数（具体数值）
    
    # === 训练轮数和步数 ===
    "epoch": 5,  # 训练轮数
    "max_train_epochs": 0,  # 最大训练轮数（0表示使用 epoch 设置）
    "max_train_steps": 4000,  # 最大训练步数
    "train_batch_size": 1,  # 训练批次大小
    "gradient_accumulation_steps": 1,  # 梯度累积步数
    
    # === LoRA 网络配置 ===
    "network_dim": 16,  # LoRA 网络维度（秩）
    "network_alpha": 16,  # LoRA 网络 alpha 值，影响 LoRA 强度
    "network_dropout": 0,  # LoRA 网络dropout率
    "network_weights": "",  # 预训练 LoRA 权重路径
    "module_dropout": 0,  # 模块dropout率
    "rank_dropout": 0,  # 秩dropout率
    "rank_dropout_scale": false,  # 是否缩放秩dropout
    "conv_dim": 1,  # 卷积层维度
    "conv_alpha": 1,  # 卷积层 alpha 值
    
    # === 高级 LoRA 配置 ===
    "block_alphas": "",  # 块级别的 alpha 值
    "block_dims": "",  # 块级别的维度
    "block_lr_zero_threshold": "",  # 块学习率零阈值
    "conv_block_alphas": "",  # 卷积块 alpha 值
    "conv_block_dims": "",  # 卷积块维度
    "down_lr_weight": "",  # 下采样层学习率权重
    "mid_lr_weight": "",  # 中间层学习率权重
    "up_lr_weight": "",  # 上采样层学习率权重
    "train_blocks": "all",  # 训练的块（"all" 表示所有块）
    
    # === 数据集配置 ===
    "train_data_dir": "D:/workspace/kohya_ss/dataset/",  # 训练数据目录
    "reg_data_dir": "",  # 正则化数据目录
    "dataset_config": "",  # 数据集配置文件路径
    "caption_extension": ".txt",  # 标题文件扩展名
    "caption_dropout_rate": 0,  # 标题丢弃率
    "caption_dropout_every_n_epochs": 0,  # 每N轮丢弃标题
    "shuffle_caption": false,  # 是否打乱标题
    "weighted_captions": false,  # 是否使用加权标题
    "keep_tokens": 0,  # 保留的标记数量
    "max_token_length": 225,  # 最大标记长度
    "t5xxl_max_token_length": 512,  # T5 最大标记长度
    
    # === 图像处理配置 ===
    "max_resolution": "1024,1024",  # 最大分辨率
    "min_bucket_reso": 256,  # 最小桶分辨率
    "max_bucket_reso": 2048,  # 最大桶分辨率
    "bucket_reso_steps": 64,  # 桶分辨率步长
    "bucket_no_upscale": true,  # 桶不上采样
    "enable_bucket": true,  # 启用桶采样
    "random_crop": false,  # 随机裁剪
    "flip_aug": false,  # 翻转增强
    "color_aug": false,  # 颜色增强
    
    # === 内存和性能优化 ===
    "mixed_precision": "bf16",  # 混合精度类型
    "full_bf16": true,  # 完全使用 bf16
    "full_fp16": false,  # 完全使用 fp16
    "fp8_base": true,  # 使用 fp8 基础模型
    "fp8_base_unet": false,  # UNet 使用 fp8
    "save_precision": "bf16",  # 保存精度
    "gradient_checkpointing": true,  # 梯度检查点（节省显存）
    "mem_eff_attn": false,  # 内存高效注意力
    "mem_eff_save": false,  # 内存高效保存
    "cache_latents": true,  # 缓存潜在变量
    "cache_latents_to_disk": true,  # 缓存潜在变量到磁盘
    "flux1_cache_text_encoder_outputs": true,  # 缓存文本编码器输出
    "flux1_cache_text_encoder_outputs_to_disk": true,  # 缓存文本编码器输出到磁盘
    "lowvram": false,  # 低显存模式
    "highvram": false,  # 高显存模式
    "cpu_offload_checkpointing": false,  # CPU 卸载检查点
    
    # === 训练行为配置 ===
    "train_on_input": true,  # 在输入上训练
    "train_norm": false,  # 训练归一化层
    "stop_text_encoder_training": 0,  # 停止文本编码器训练的步数
    "train_t5xxl": false,  # 是否训练 T5 编码器
    "apply_t5_attn_mask": true,  # 应用 T5 注意力掩码
    "clip_skip": 1,  # CLIP 跳过层数
    
    # === 噪声和损失配置 ===
    "noise_offset": 0.05,  # 噪声偏移
    "noise_offset_type": "Original",  # 噪声偏移类型
    "noise_offset_random_strength": false,  # 随机噪声偏移强度
    "adaptive_noise_scale": 0,  # 自适应噪声比例
    "multires_noise_iterations": 0,  # 多分辨率噪声迭代次数
    "multires_noise_discount": 0.3,  # 多分辨率噪声折扣
    "ip_noise_gamma": 0,  # IP 噪声 gamma 值
    "ip_noise_gamma_random_strength": false,  # 随机 IP 噪声 gamma 强度
    "loss_type": "l2",  # 损失函数类型
    "huber_c": 0.1,  # Huber 损失参数 c
    "huber_schedule": "snr",  # Huber 调度类型
    "min_snr_gamma": 7,  # 最小信噪比 gamma
    "debiased_estimation_loss": false,  # 去偏估计损失
    "masked_loss": false,  # 掩码损失
    "prior_loss_weight": 1,  # 先验损失权重
    "v_pred_like_loss": 0,  # V 预测损失
    "scale_v_pred_loss_like_noise_pred": false,  # 缩放 V 预测损失
    
    # === 时间步配置 ===
    "min_timestep": 0,  # 最小时间步
    "max_timestep": 1000,  # 最大时间步
    "timestep_sampling": "sigmoid",  # 时间步采样方法
    "discrete_flow_shift": 3,  # 离散流偏移
    "guidance_scale": 1,  # 引导比例
    "model_prediction_type": "raw",  # 模型预测类型
    
    # === 保存和输出配置 ===
    "output_dir": "D:/workspace/kohya_ss/outputs/",  # 输出目录
    "output_name": "Flux_Clay_Style_Lora",  # 输出模型名称
    "save_model_as": "safetensors",  # 保存模型格式
    "save_every_n_epochs": 1,  # 每N轮保存一次
    "save_every_n_steps": 200,  # 每N步保存一次
    "save_last_n_steps": 0,  # 保存最后N步
    "save_last_n_steps_state": 0,  # 保存最后N步的状态
    "save_state": false,  # 保存训练状态
    "save_state_on_train_end": false,  # 训练结束时保存状态
    "save_state_to_huggingface": false,  # 保存状态到 HuggingFace
    "save_as_bool": false,  # 布尔值保存方式
    
    # === 采样和验证配置 ===
    "sample_every_n_epochs": 0,  # 每N轮采样一次
    "sample_every_n_steps": 200,  # 每N步采样一次
    "sample_prompts": "abstract college thesis project, portraiture, thread, clay, sand, dirt, colorful, vibrant, abstraction, crystal --w 832 --h 1216 --s 20 --l 4 --d 42",  # 采样提示词
    "sample_sampler": "euler",  # 采样器类型
    
    # === 日志和监控配置 ===
    "logging_dir": "D:/workspace/kohya_ss/logs/",  # 日志目录
    "log_config": false,  # 记录配置
    "log_tracker_name": "",  # 日志跟踪器名称
    "log_tracker_config": "",  # 日志跟踪器配置
    "log_with": "",  # 日志记录工具
    "wandb_api_key": "",  # Weights & Biases API 密钥
    "wandb_run_name": "",  # WandB 运行名称
    
    # === 分布式训练配置 ===
    "multi_gpu": false,  # 多GPU训练
    "num_machines": 1,  # 机器数量
    "num_processes": 1,  # 进程数量
    "main_process_port": 0,  # 主进程端口
    "gpu_ids": "",  # GPU ID列表
    "num_cpu_threads_per_process": 2,  # 每进程CPU线程数
    "max_data_loader_n_workers": 0,  # 数据加载器最大工作线程数
    "persistent_data_loader_workers": false,  # 持久化数据加载器工作线程
    
    # === HuggingFace 配置 ===
    "huggingface_repo_id": "",  # HuggingFace 仓库ID
    "huggingface_repo_type": "",  # HuggingFace 仓库类型
    "huggingface_repo_visibility": "",  # HuggingFace 仓库可见性
    "huggingface_token": "",  # HuggingFace 访问令牌
    "huggingface_path_in_repo": "",  # HuggingFace 仓库内路径
    "resume_from_huggingface": "",  # 从 HuggingFace 恢复训练
    "async_upload": false,  # 异步上传
    
    # === 训练恢复配置 ===
    "resume": "",  # 恢复训练路径
    
    # === 梯度和优化配置 ===
    "max_grad_norm": 1,  # 最大梯度范数
    "scale_weight_norms": 0,  # 缩放权重范数
    "constrain": 0,  # 约束参数
    
    # === 高级网络配置 ===
    "enable_all_linear": false,  # 启用所有线性层
    "split_mode": false,  # 分割模式
    "split_qkv": false,  # 分割查询-键-值
    "use_tucker": false,  # 使用Tucker分解
    "use_scalar": false,  # 使用标量
    "use_cp": false,  # 使用CP分解
    "decompose_both": false,  # 分解两者
    "factor": -1,  # 因子
    "dim_from_weights": false,  # 从权重获取维度
    "unit": 1,  # 单位
    "dora_wd": false,  # DoRA权重衰减
    "bypass_mode": false,  # 绕过模式
    
    # === 特殊维度配置 ===
    "single_dim": "",  # 单一维度
    "single_mod_dim": "",  # 单一模组维度
    "in_dims": "",  # 输入维度
    "img_attn_dim": "",  # 图像注意力维度
    "img_mlp_dim": "",  # 图像MLP维度
    "img_mod_dim": "",  # 图像模组维度
    "txt_attn_dim": "",  # 文本注意力维度
    "txt_mlp_dim": "",  # 文本MLP维度
    "txt_mod_dim": "",  # 文本模组维度
    
    # === LoRA Plus 配置 ===
    "loraplus_lr_ratio": 0,  # LoRA Plus 学习率比例
    "loraplus_text_encoder_lr_ratio": 0,  # LoRA Plus 文本编码器学习率比例
    "loraplus_unet_lr_ratio": 0,  # LoRA Plus UNet 学习率比例
    
    # === 技术配置 ===
    "flux1_checkbox": true,  # Flux1 复选框
    "xformers": "sdpa",  # xformers 类型（sdpa = Scaled Dot Product Attention）
    "sdxl": false,  # 是否为SDXL模型
    "sdxl_cache_text_encoder_outputs": true,  # SDXL缓存文本编码器输出
    "sdxl_no_half_vae": true,  # SDXL不使用半精度VAE
    "v2": false,  # 是否为v2模型
    "v_parameterization": false,  # V参数化
    "model_list": "custom",  # 模型列表类型
    "rescaled": false,  # 重新缩放
    "vae_batch_size": 0,  # VAE批次大小
    
    # === 动态优化配置 ===
    "dynamo_backend": "no",  # Dynamo后端
    "dynamo_mode": "default",  # Dynamo模式
    "dynamo_use_dynamic": false,  # 使用动态Dynamo
    "dynamo_use_fullgraph": false,  # 使用完整图Dynamo
    
    # === 其他配置 ===
    "seed": 42,  # 随机种子
    "training_comment": "",  # 训练注释
    "additional_parameters": "",  # 额外参数
    "extra_accelerate_launch_args": "",  # 额外的accelerate启动参数
    "metadata_author": "",  # 元数据作者
    "metadata_description": "",  # 元数据描述
    "metadata_license": "",  # 元数据许可证
    "metadata_tags": "",  # 元数据标签
    "metadata_title": "",  # 元数据标题
}

# 配置文件使用说明：
"""
1. 基础配置：设置model路径、学习率、训练步数等核心参数
2. LoRA配置：调整network_dim和network_alpha来控制LoRA强度
3. 内存优化：启用gradient_checkpointing和缓存选项来节省显存
4. 数据处理：配置分辨率、桶采样等图像处理参数
5. 保存设置：设置保存频率和输出格式
6. 采样验证：配置训练过程中的图像采样参数
"""