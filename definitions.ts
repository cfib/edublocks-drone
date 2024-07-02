const droneColor = "#1DB954";

Blockly.Blocks['init_drone'] = {
    init: function() {
     this.appendDummyInput()
          .appendField("Initialize Drone");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['start_game'] = {
    init: function() {
     this.appendDummyInput()
          .appendField("Start Game");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['plant_tree'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("Plant Tree");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['ascend'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("ascend for")
          .appendField(new Blockly.FieldNumber(1), "duration");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['descend'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("descend for")
          .appendField(new Blockly.FieldNumber(1), "duration");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['move'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("move")
          .appendField(new Blockly.FieldDropdown([["North","N"], ["North East","NE"], ["East","E"], ["South East","SE"], ["South","S"], ["South West","SW"], ["West","W"], ["North West","NW"]]), "direction")
          .appendField("for")
          .appendField(new Blockly.FieldNumber(1), "duration");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};
