scoreboard players enable @a get_head
execute as @a[scores={get_head=1..}] at @s run function allplayerheads:handle_trigger
scoreboard players set @a[scores={get_head=1..}] get_head 0
