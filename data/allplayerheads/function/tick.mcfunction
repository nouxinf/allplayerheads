scoreboard players enable @a get_head
scoreboard players enable @a my_trigger
execute as @a[scores={get_head=1..}] at @s run function allplayerheads:handle_trigger
scoreboard players set @a[scores={get_head=1..}] get_head 0
execute as @a[scores={version=1..}] run function allplayerheads:version
scoreboard players set @a[scores={version=1..}] version 0