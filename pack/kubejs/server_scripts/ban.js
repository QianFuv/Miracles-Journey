// 用于 Ban 物品

ServerEvents.recipes(event => {
    // MoreMinecartsAndRails 的区块加载器系列物品&方块
    // 区块晶石块
    event.remove({ output: "moreminecarts:chunkrodite_block" })
    // 区块加载器矿车
    event.remove({ output: "moreminecarts:minecart_with_chunk_loader" })
    // 区块加载器
    event.remove({ output: "moreminecarts:chunk_loader" })

    // ImmersiveEngineering 的粗铝土系列物品&方块
    // 粗铝土
    event.remove({ output: "immersiveengineering:raw_aluminum" })
    // 粗铝土块
    event.remove({ output: "immersiveengineering:raw_block_aluminum" })
})