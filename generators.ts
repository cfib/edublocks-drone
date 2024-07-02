Blockly.Python['init'] = function(block) {
    var code = 'import ledmatrix\n'+
               'm = ledmatrix.LedMatrix("http://192.168.1.1:80")';
    return code;
};

Blockly.Python['start_game'] = function(block) { 
    var code = 'm.start_game()';
    return code;
}

Blockly.Python['ascend'] = function(block) { 
    var duration = Blockly.Python.nameDB_.getName(block.getFieldValue('duration'), Blockly.VARIABLE_CATEGORY_NAME);
    var code = `m.ascend(${duration})`;
    return code;
}

Blockly.Python['descend'] = function(block) { 
    var duration = Blockly.Python.nameDB_.getName(block.getFieldValue('duration'), Blockly.VARIABLE_CATEGORY_NAME);
    var code = `m.descend(${duration})`;
    return code;
}

Blockly.Python['move'] = function(block) { 
    var direction = Blockly.Python.nameDB_.getName(block.getFieldValue('direction'), Blockly.VARIABLE_CATEGORY_NAME);
    var duration  = Blockly.Python.nameDB_.getName(block.getFieldValue('duration'), Blockly.VARIABLE_CATEGORY_NAME);
    var code = `m.move("${direction}",${duration})`;
    return code;
}

Blockly.Python['plant_tree'] = function(block) { 
    var code = 'm.plant_tree()';
    return code;
}
