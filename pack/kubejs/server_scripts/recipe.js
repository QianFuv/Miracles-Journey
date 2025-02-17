// 用于添加、修改物品配方

ServerEvents.recipes(event => {
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