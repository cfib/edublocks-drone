import requests
import enum
import time
import math

class LedMatrixButtonPress(enum.IntFlag):
    BUTTON_Z          = 0x00020000  # nunchuk
    BUTTON_C          = 0x00010000  # nunchuk
    BUTTON_PLUS       = 0x00001000 
    BUTTON_UP         = 0x00000800  # vertical orientation
    BUTTON_DOWN       = 0x00000400 
    BUTTON_RIGHT      = 0x00000200
    BUTTON_LEFT       = 0x00000100
    BUTTON_HOME       = 0x00000080
    BUTTON_MINUS      = 0x00000010
    BUTTON_A          = 0x00000008
    BUTTON_B          = 0x00000004
    BUTTON_ONE        = 0x00000002
    BUTTON_TWO        = 0x00000001
    NO_BUTTON         = 0x00000000
    
class LedMatrixDirectionsY(enum.IntFlag):
    NORTH = LedMatrixButtonPress.BUTTON_UP
    SOUTH = LedMatrixButtonPress.BUTTON_DOWN
    NONE  = LedMatrixButtonPress.NO_BUTTON
    
class LedMatrixDirectionsX(enum.IntFlag):
    EAST  = LedMatrixButtonPress.BUTTON_LEFT
    WEST  = LedMatrixButtonPress.BUTTON_RIGHT
    NONE  = LedMatrixButtonPress.NO_BUTTON
    
class LedMatrixGameState(enum.IntEnum):
    GAME_STATE_RESET_PLAYFIELD = 1
    GAME_STATE_WAIT_START      = 2
    GAME_STATE_GAME            = 4
    GAME_STATE_FINAL           = 8

class LedMatrix:
    def __init__(self, base_uri):
        self.uri = base_uri
        
        
    def get_game_state(self):
        r = requests.get(self.uri+'/status')
        if r.ok:
            return LedMatrixGameState(r.json()['state'])
        else:
            print(r.text)
            
    def get_position(self):
        r = requests.get(self.uri+'/status')
        if r.ok:
            return (int(r.json()['x']), int(r.json()['y']), int(r.json()['z']))
        else:
            print(r.text)
        return None, None, None
        
    def get_flags(self):
        r = requests.get(self.uri+'/status')
        if r.ok:
            return (int(r.json()['planting']), int(r.json()['battery']), int(r.json()['plantable']))
        else:
            print(r.text)
        return None, None, None
            
    def push_key(self, button : LedMatrixButtonPress, delay : float = 0.02):
        r1= self.press_key(button)
        time.sleep(delay)
        r2 = self.release_key()
        return r1 and r2
        
    def press_key(self, button : LedMatrixButtonPress):
        r = requests.get(self.uri+f'/command/0x{button:04x}')
        print(r.url)
        return r.ok
    
    def release_key(self):
        r = requests.get(self.uri+f'/command/0x{LedMatrixButtonPress.NO_BUTTON:08x}')
        return r.ok
        
    def start_game(self):
        if self.get_game_state() == LedMatrixGameState.GAME_STATE_GAME:
            # stop current game
            self.push_key(LedMatrixButtonPress.BUTTON_ONE | LedMatrixButtonPress.BUTTON_TWO)
            # reset game
            self.push_key(LedMatrixButtonPress.BUTTON_A)
        elif self.get_game_state() == LedMatrixGameState.GAME_STATE_FINAL:
            # reset game
            self.push_key(LedMatrixButtonPress.BUTTON_A)
        elif self.get_game_state() == LedMatrixGameState.GAME_STATE_RESET_PLAYFIELD:
            time.sleep(0.1) # will be in GAME_STATE_WAIT_START immediately
            assert(self.get_game_state() == LedMatrixGameState.GAME_STATE_WAIT_START)
        elif self.get_game_state() == LedMatrixGameState.GAME_STATE_WAIT_START:
            pass
        self.push_key(LedMatrixButtonPress.BUTTON_A)
        time.sleep(0.2)
        assert(self.get_game_state() == LedMatrixGameState.GAME_STATE_GAME), self.get_game_state()
        
    def ascend(self, delta : float):
        self.press_key(LedMatrixButtonPress.BUTTON_PLUS)
        time.sleep(delta)
        self.release_key()
            
        
    def descend(self, delta : float):
        self.press_key(LedMatrixButtonPress.BUTTON_MINUS)
        time.sleep(delta)
        self.release_key()
            
    def move(self, direction, delta : float):
        
        direction_x, direction_y = {'N':  (LedMatrixDirectionsX.NONE, LedMatrixDirectionsY.NORTH),
                                    'NE': (LedMatrixDirectionsX.EAST, LedMatrixDirectionsY.NORTH),
                                    'E':  (LedMatrixDirectionsX.EAST, LedMatrixDirectionsY.NONE),
                                    'SE': (LedMatrixDirectionsX.EAST, LedMatrixDirectionsY.SOUTH),
                                    'S':  (LedMatrixDirectionsX.NONE, LedMatrixDirectionsY.SOUTH),
                                    'SW': (LedMatrixDirectionsX.WEST, LedMatrixDirectionsY.SOUTH),
                                    'W':  (LedMatrixDirectionsX.WEST, LedMatrixDirectionsY.NONE),
                                    'NW': (LedMatrixDirectionsX.WEST, LedMatrixDirectionsY.NORTH)}.get(direction.upper(), (LedMatrixDirectionsX.NONE, LedMatrixDirectionsY.NONE))
    
        print('x',direction_x)
        print('y',direction_y)
        self.press_key(direction_x | direction_y)
        if direction_x and direction_y:
            delta *= 1/math.sqrt(2)
        time.sleep(delta)
        self.release_key()
        while True:
            x0, y0, z0 = self.get_position()
            time.sleep(0.1)
            x1, y1, z1 = self.get_position()
            if x0 == x1 and y0 == y1:
                break
        
        
    def plant_tree(self, check : bool, checkBatt : bool = False):
        if check:
            x,  y,  z = self.get_position()
            pt, bt, p = self.get_flags()
            if z < 4 or not pt or not p:
                return False
            if checkBatt and bt:
                return False
        return self.push_key(LedMatrixButtonPress.BUTTON_B)
