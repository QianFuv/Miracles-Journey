// 用于隐藏被 Ban 物品

JEIEvents.hideItems(event => {
    event.hide([
        // MoreMinecartsAndRails 的区块加载器系列物品&方块
        // 区块晶石块
        "moreminecarts:chunkrodite_block",
        // 区块加载器矿车
        "moreminecarts:minecart_with_chunk_loader",
        // 区块加载器
        "moreminecarts:chunk_loader",

        // ImmersiveEngineering 的粗铝土系列物品&方块
        // 粗铝土
        "immersiveengineering:raw_aluminum",
        // 粗铝土块
        "immersiveengineering:raw_block_aluminum"
    ])
})