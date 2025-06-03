_base_ = [
    '../../../configs/_base_/models/upernet_swin.py',
    '../../../configs/_base_/datasets/whs.py', '../../../configs/_base_/default_runtime.py',
    '../../../configs/_base_/schedules/schedule_160k.py'
]
model = dict(
    pretrained='pretrain/swin_tiny_patch4_window7_224.pth',
    backbone=dict(
        embed_dims=96,
        depths=[2, 2, 6, 2],
        num_heads=[3, 6, 12, 24],
        window_size=7,
        use_abs_pos_embed=False,
        drop_path_rate=0.3,
        patch_norm=True),
    decode_head=dict(in_channels=[96, 192, 384, 768], num_classes=150),
    auxiliary_head=dict(in_channels=384, num_classes=150))

# optimizer
optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.00006,
    betas=(0.9, 0.999),
    weight_decay=0.01,
    paramwise_cfg=dict(
        custom_keys={
            'pos_block': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.),
            'head': dict(lr_mult=10.)
        }))

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)
data = dict(samples_per_gpu=1, workers_per_gpu=1)

total_iters = 40000
checkpoint_config = dict(by_epoch=False, interval=800)
evaluation = dict(interval=800, metric='mDice', pre_eval=True)

work_dir = './experiments/MSCL_SwinUNet_160k_WHS/results/'
workflow = [('train', 1), ('val', 1)]
