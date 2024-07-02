Blockly.Python['init_drone'] = function(block) {
    var code = 'import drone\n'+
               'm = drone.LedMatrix("http://192.168.1.1:80")\n';
    return code;
};

Blockly.Python['start_game'] = function(block) { 
    var code = 'm.start_game()\n';
    return code;
}

Blockly.Python['ascend'] = function(block) { 
    var duration = block.getFieldValue('duration');
    var code = `m.ascend(${duration})\n`;
    return code;
}

Blockly.Python['descend'] = function(block) { 
    var duration = block.getFieldValue('duration');
    var code = `m.descend(${duration})\n`;
    return code;
}

Blockly.Python['move'] = function(block) { 
    var direction = block.getFieldValue('direction');
    var duration  = block.getFieldValue('duration');
    var code = `m.move("${direction}",${duration})\n`;
    return code;
}

Blockly.Python['plant_tree'] = function(block) { 
    var code = 'm.plant_tree()\n';
    return code;
}
