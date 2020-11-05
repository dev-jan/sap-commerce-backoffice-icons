# Full Tutorial: How to define icons in Backoffice for own types?

This tutorial will guide you to set a icon to a custom SAP Commerce typ.

1. Create an additional CSS file for Backoffice in your Backoffice extension.
   Path:
   
   ```[YOUR-EXTENSION]/resources/cockpitng/cng/css/[YOUR-EXTENSION-NAME]_common.css```

   This css file will be automatically added to the Backoffice by name
   definition. Because of this, it's important to name it correctly.

2. Create the icon sprite with this tool (see [here](../README.md)) and place it
   in:
   
   ```[YOUR-EXTENSION>/resources/cockpitng/cng/css/images/[IMAGENAME].png```

3. Add a CSS rule to link the image with the explorer-tree node. It has to look
   like this:
   
   ```
    div.yw-explorerTree .y-tree-icon-hmc_typenode_someTypeName .y-tree-icon {
        background-image: url("images/someTypeIcon.png");
    }
   ```
   
   The middle part of the CSS selector is constructed in the following way:
   ```y-tree-icon-[TYPE-NODE-ID]```. The [TYPE-NODE-ID] can be found in your
   backoffice config. Example:
   ```
    <context component="explorer-tree" merge-by="module">
        <n:explorer-tree>
            <n:navigation-node id="hmc_treenode_system">
                <n:type-node id="hmc_typenode_someTypeName" code="someTypeName" />
            </n:navigation-node>
        </n:explorer-tree>
    </context>
   ```
   Here the [TYPE-NODE-ID] will be "hmc_typenode_someTypeName", so the CSS
   selector will be "y-tree-icon-hmc_typenode_someTypeName".

4. Reload the Backoffice and force-reload your browser styles (Ctrl + F5)

5. The icon should now be displayed in front of the typ name :)
