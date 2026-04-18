# AllPlayerHeads

A Minecraft datapack that lets you get any custom head off [minecraft-heads.com](https://minecraft-heads.com), without using any plugins or mods.

## How to use

All 91,820 custom heads available at Minecraft Heads are included here. In order to get one, you must:

### 1. Install the datapack

Do this by getting the zip off modrinth for your minecraft version, and putting it into either `.minecraft/datapacks/` if you are are on singleplayer, or on servers put it in `worlds/datapacks/`.

### 2. Make sure normal players are able to run `/trigger`

This is true by default, but if you have a permissions plugin you should make sure that's the case.

### 3. Find the head you want

Go on [minecraft-heads.com](https://minecraft-heads.com) and pick a head.

### 4. Copy the Minecraft URL

Scroll down towards "For Developers:" and copy the Minecraft URL

### 5. Go to the converter website

The datapack takes a number, not a string, so you will need to convert it at the [the converter tool](https://nouxinf.github.io/allplayerheads/).

### 6. Fill in the appropriate fields

You must select the correct version of the datapack, which you can find out by running `/trigger version`. You also take the Minecraft URL you retrieved earlier.
Now, you will have a number, that could be from 1 to around 91 thousand. You must run this command:

```mcfunction
/trigger get_head set 999
```

Replace 999 with the number provided by the website.
Now, the player head will appear in your inventory!

If however, the converter fails in giving you a number, then the custom head is likely new, and is not present in the version you are on. The only solution is to wait until this datapack is updated and update it.

If the command given fails, then first make sure it is typed correctly and the version is correct, then [make an issue on the GitHub](https://github.com/nouxinf/allplayerheads/issues/new/choose).
