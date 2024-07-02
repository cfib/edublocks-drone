const droneColor = "#1DB954";

Blockly.Blocks['init'] = {
    init: function() {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['plant_tree'] = {
    init: function() {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['ascend'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("duration"), "duration"));
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['descend'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("duration"), "duration"));
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};

Blockly.Blocks['move'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([["North","N"], ["North East","NE"], ["East","E"], ["South East","SE"], ["South","S"], ["South West","SW"], ["West","W"], ["North West","NW"]]), "direction")
          .appendField(new Blockly.FieldVariable("duration"), "duration"));
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(droneColor);
    }
};
