// 用于统一矿石及产物的配方和标签

ServerEvents.tags('item', event => {
    event.add("forge:ores/aluminum", "createindustry:bauxite")
    event.add("forge:ores/diamond", "#spelunkery:diamond_ores")
    event.add("forge:ores/coal", "#spelunkery:coal_ores")
    event.add("forge:ores/emerald", "#spelunkery:emerald_ores")
    event.add("forge:ores/lapis", "#spelunkery:lapis_ores")
    event.add("forge:ores/redstone", "#spelunkery:redstone_ores")
    event.add("forge:ores/gold", "#spelunkery:gold_ores")
    event.add("forge:ores/iron", "#spelunkery:iron_ores")
    event.add("forge:ores/zinc", "#spelunkery:zinc_ores")
    event.add("forge:ores/lead", "#spelunkery:lead_ores")
    event.add("forge:ores/silver", "#spelunkery:silver_ores")
})