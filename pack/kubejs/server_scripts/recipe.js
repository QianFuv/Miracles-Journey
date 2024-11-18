// 用于添加、修改物品配方

ServerEvents.recipes(event => {
    // 焰矢扫帚
    event.replaceInput(
        { output: "witchmobility:firebolt_broom_item" },
        "minecraft:stick",
        "minecraft:blaze_rod"
    )
    
    // 银箭扫帚
    event.replaceInput(
        { output: "witchmobility:silver_arrow_broom_item" },
        "minecraft:hay_block",
        "minecraft:nether_star"
    )

    // 粗制绿宝石碎片
    event.replaceInput(
        { output: "villagertools:restock" },
        "minecraft:emerald",
        "minecraft:emerald_block"
    )

    // 镀层升级
    event.replaceInput(
        { output: "modulargolems:coating" },
        "create:zinc_ingot",
        "minecraft:netherite_scrap"
    )

    // 空白唱片
    event.shaped(
        Item.of("etched:blank_music_disc", 1),
        [
            "AAA",
            "A A",
            "AAA"
        ],
        {
            A: "create_dd:rubber"
        }
    )
})